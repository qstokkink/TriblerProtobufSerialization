import google.protobuf
import logging
from struct import pack, unpack_from, calcsize
from struct import error as struct_error
import sys

import messages
from exception import *

class Serializer:

    """Class to serialize data by means of Protocol Buffers message
        definitions.
    """

    def __init__(self, autoload=True):
        """Initialize a new Serializer.

            :param autoload: call load_definitions after initialization
        """
        self.header_size = 20
        self.messages = {}
        self.message_hashes = {}
        self.message_rhashes = {}
        self.handlers = {}
        self.remainder = ""
        if autoload:
            self.load_definitions()

    def _hash_name(self, name, length=None):
        """Fit a name to a certain length.

            :param name: the name to hash
            :param length: fit to something else than header_size
            :returns: the hashed name
        """
        if not length:
            length = self.header_size
        hashed = name[:min(length, len(name))]
        for x in range(length, len(name), length):
            rem = min(x+length,len(name))-x
            for i in range(rem):
                hashed = hashed[:i] + chr(ord(name[x + i]) ^ ord(hashed[i])) + hashed[i+1:]
        return hashed

    def load_definitions(self):
        """Load the protobuffers definitions from the messages module.
        """
        for module in messages.MESSAGES:
            names = module.DESCRIPTOR.message_types_by_name
            prefix = module.__name__.split('.')[-1]
            for message_name in names:
                hashed_name = self._hash_name(prefix + message_name)
                if hashed_name in self.messages:
                    logging.warning("Serializer read duplicate message!" +
                                        "Overwriting definition of " + message_name)
                self.messages[hashed_name] = getattr(module, message_name)
                self.message_hashes[hashed_name] = message_name
                self.message_rhashes[message_name] = hashed_name

    def add_handler(self, name, callback):
        """Add a callback to be fired when a certain message type has been
            received.

            :param name: the name of the messages to handle
            :param callback: the function to be called with the message
        """
        if not (name in self.handlers):
            self.handlers[name] = []
        self.handlers[name].append(callback)

    def _fuzzy_module_name_eq(self, module, package_name):
        """Given a package name, check if it resembles a module.

            Accepts packages names as:
                - Full python class path
                - Full python class path minus '_pb2'
                - Python class/.proto name
                - .proto name
                - .proto package

            :param module: the python module to check
            :param package_name: the name to equate
            :returns: whether name and the module equate
        """
        return ((module.__name__ == package_name) or 
                (module.__name__.replace('_pb2', '') == package_name) or 
                (module.DESCRIPTOR.name == package_name) or 
                (module.DESCRIPTOR.name.replace('.proto', '') == package_name) or
                (module.DESCRIPTOR.package == package_name))

    def add_package_handler(self, package_name, cls):
        """Add a handler which handles all messages for a certain package.
            Callbacks will be performed with cls member function of the name:
                on_<lowercase message name>()

            :param package_name: the name of the package of the messages
            :param cls: the callback class
        """
        for module in messages.MESSAGES:
            if self._fuzzy_module_name_eq(module, package_name):
                for name in module.DESCRIPTOR.message_types_by_name:
                    self.add_handler(name, getattr(cls, 'on_' + name.lower()))

    def __gt_by_type(self, value, setting):
        """Check if a value has a length in bytes, shorter than some setting.
            Note that this is the worst-case length, as values can be packed.

            :param value: the value to check (string, int or long)
            :param setting: the maximum length in bytes
            :returns: if the value was larger than the setting
        """
        if value == "":
            return False
        if isinstance(value, str) or isinstance(value, unicode):
            return len(value) > setting
        # Recognize 0 as an int
        try:
            p = int(value)
            if p == 0:
                return False # 0 is always allowed
        except ValueError:
            pass
        if isinstance(value, int) or isinstance(value, long):
            max_long = 0
            if value > 0:
                max_long = (1 << (8*setting-1))-1
                return value > max_long
            elif value < 0:
                max_long = -(1 << (8*setting-1))
                return value < max_long
        raise FieldLengthUnsupportedException("Tried to apply length(" +
                                str(setting) + ") option to " + str(value) +
                                ", not a string, int or long")

    def _check_field_length(self, field, value, options=None):
        """Check if a field has a valid value set.
            Throws a FieldTooLongException if it doesn't.

            :param field: the field descriptor object
            :param value: the value set for the field
        """
        options = options if options else field.GetOptions()
        for (option, setting) in options.ListFields():
            if option.name == "length":
                if self.__gt_by_type(value, setting):
                    if hasattr(field, "name"):
                        raise FieldTooLongException("The field '" + field.name +
                            "' is bigger than the allowed " + str(setting) + " bytes")
                    else:
                        raise FieldTooLongException("List element '" + str(value) +
                            "' is bigger than the allowed " + str(setting) + " bytes")

    def _checked_set(self, struct, field, value):
        """Assign a value to a field and check 
            all custom options.

            :param struct: the protobuf (nested) struct
            :param field: the field name to set
            :param value: the value to set it to
        """
        setattr(struct, field, value)
        self._check_field_length(struct.DESCRIPTOR.fields_by_name[field], value)

    def _get_options(self, struct, field):
        """Get options for a field, if the struct supports it.

            :param struct: the struct holding the descriptor
            :param field: the name of the field to get the options for
        """
        return struct.DESCRIPTOR.fields_by_name[field].GetOptions() if hasattr(struct, "DESCRIPTOR") else None

    def _process_value(self, value):
        """Convert a value to a value which protobuf supports.
            Currently only binary strings need special treat-
            ment.

            :param value: the value to convert
        """
        if isinstance(value, str):
            try:
                value.decode('ascii')
            except UnicodeDecodeError:
                return unicode(''.join([unichr(ord(c)) for c in value]))
        return value

    def _map_onto(self, field_struct, value, options=None):
        """Set a field in a Protocol Buffers struct
            to a certain value.

            For example:
                _map_onto(a.b, (1, 2))
            Sets:
                a.b[0] = 1
                a.b[1] = 2

            :param field_struct: the protobuf (nested) struct
            :param value: the value to set it to
            :param options: options for list types
        """
        if isinstance(value, list):
            # Fill 'repeated' structure
            # a.b = [1, 2]
            #   a.b.add() = 1
            #   a.b.add() = 2
            for sub in value:
                if hasattr(field_struct, "add"):
                    nested = field_struct.add()
                    # Composite lists will never
                    # need to be set by us
                    self._map_onto(nested, sub)
                else:
                    # Scalar lists will always
                    # need to be set by us
                    field_struct.append(self._process_value(sub))
                    if options:
                        self._check_field_length(field_struct, sub, options)
        elif isinstance(value, dict):
            # Fill message structure
            # a.b = {c: 1, d: 2}
            #   a.b.c = 1
            #   a.b.d = 2
            for key in value:
                nested = getattr(field_struct, key)
                r = self._map_onto(nested, value[key], self._get_options(field_struct, key))
                if r:
                    self._checked_set(field_struct, key, r[0])
        elif isinstance(value, tuple):
            # Fill message structure (in order)
            # a.b = (1, 2)
            #   a.b.c = 1
            #   a.b.d = 2
            fields = field_struct.DESCRIPTOR.fields
            for i in range(len(value)):
                nested = getattr(field_struct, fields[i].name)
                r = self._map_onto(nested, value[i], self._get_options(field_struct, fields[i].name))
                if r:
                    self._checked_set(field_struct, fields[i].name, r[0])
        else:
            return [self._process_value(value), ]

    def _unspecify_name(self, name):
        """In case of overlapping messages a user will want
            to specify which package to use.
            For example:
                'B.A' instead of 'A'
            when both 'B.A' and 'C.A' exist.

            This function retrieves the reverse hash of
            otherwise overlapping message names.

            :param: the name to unspecify
        """
        unspec = None
        path = name.split('.')[0]
        for module in messages.MESSAGES:
            if self._fuzzy_module_name_eq(module, path):
                prefix = module.__name__.split('.')[-1]
                return self._hash_name(prefix + name[len(path)+1:])

    def serialize(self, name, *args, **kwargs):
        """Serialize a message of a certain type.

            :param name: the name of the message to serialize
            :param args: the fields of the message in order
            :param kwargs: the (remaining) fields of the message by field name
            :returns: the serialization as a binary string 
        """ 
        if not (name in self.message_rhashes):
            unspec = self._unspecify_name(name)
            if not unspec or not (unspec in self.messages):
                raise UnknownMessageException("Tried to provide serialization for " + 
                                            "unknown message '" + name + "'")
            name = unspec
        else:
            name = self.message_rhashes[name]
        struct = self.messages[name]()
        index = 0
        for field in struct.DESCRIPTOR.fields:
            # Loop through the fields in order of definition
            # If we can't, the fields have to be initialized by the
            #   keyword arguments
            value = args[index] if index < len(args) else kwargs.get(field.name)
            # dict.get() returns None if the entry was not found
            if value == None:
                raise FieldNotDefinedException("The field '" + field.name +
                    "' was not defined when serializing a '" + name + "'")
            try:
                r = self._map_onto(getattr(struct, field.name), value, self._get_options(struct, field.name))
                if r:
                    self._checked_set(struct, field.name, r[0])
            except TypeError, e:
                raise FieldWrongTypeException("Tried to set the field '" + field.name +
                    "' to " + str(e).replace('has type', 'which has the type'))
            except ValueError, e:
                raise FieldWrongTypeException("Tried to set the field '" + field.name +
                    "' but " + str(e))
            index += 1
        return pack(str(self.header_size) + 's', name) + struct.SerializePartialToString()

    def _forward_message(self, name, message):
        """Forward a message to its appropriate handlers

            :param name: the message name/type
            :param message: the actual message object
        """
        unhashed = self.message_hashes[name]
        if unhashed in self.handlers:
            for handler in self.handlers[unhashed]:
                handler(message)

    def _unserialize_header(self, data, persistent_start):
        """Find a message header in given data.

            :param data: the data buffer
            :param persistent_start: keep popping from the stream until a
                                        valid header appears 
            :returns: the header name (or ""), the garbage prefix length
        """
        name = ""
        sbuffer = data
        # Skip characters until a valid message id appears
        while len(sbuffer) > self.header_size:
            (header, ) = unpack_from(str(self.header_size) + 's', sbuffer)
            header = header.replace('\x00','')
            if header in self.messages:
                name = header
                break
            if not persistent_start:
                break
            sbuffer = sbuffer[1:]
        return name, len(data) - len(sbuffer)

    def _unserialize_body(self, data, struct, persistent_end):
        """Try to read a valid Protocol Buffers definition from
            the start of the data.

            :param data: the data buffer
            :param struct: the empty data container
            :param persistent_end: keep popping from the end of
                            the data until a message can be read
            :returns: is valid, the message struct, its length
        """
        initialized = False
        while len(data) > 0:
            try:
                # MergeFromString will ignore all data after it
                # has finished parsing a message from the start
                # of the data. By default `message + garbage`
                # will parse `message` perfectly fine.
                # This becomes a problem when `garbage` contains
                # another message.
                struct.ParseFromString(data)
                initialized = True
                break
            except google.protobuf.message.DecodeError, e:
                if str(e).startswith("Trunc"):
                    break
            if not persistent_end:
                break
            data = data[:-1]
        return initialized, struct, len(struct.SerializePartialToString())

    def unserialize(self, data, persistent_start=True, 
                    persistent_end=True, keep_remainder=False):
        """Given some data, try to read serializations from it.

            :param data: the raw binary data to interpret
            :param persistent_start: while unserializable pop the first character
            :param persistent_end: while unserializable pop the last character
            :param keep_remainder: feed the data after a valid entry 
                                    to the next call
            :returns: all of the read messages in the data
        """
        # Consume the previous remainder
        data = self.remainder + data
        self.remainder = ''
        # Get the message id
        name, start_skip = self._unserialize_header(data, persistent_start)
        if not name:
            if keep_remainder:
                self.remainder = data
            return
        # The message id is valid
        sbuffer = data[start_skip+self.header_size:]
        initialized, struct, actual_size = self._unserialize_body(sbuffer, 
                                                        self.messages[name](), 
                                                        persistent_end)
        if (not initialized) or ((not persistent_end) and (len(sbuffer) != actual_size)):
            # Possible illegal header
            if persistent_start:
                self.unserialize(data[start_skip+self.header_size:], persistent_start, persistent_end, keep_remainder)
            # If the other call could not clear the remainder, keep it
            if (self.remainder == data[start_skip+self.header_size:]) and keep_remainder:
                self.remainder = data[start_skip:]
            return
        # Forward the (now valid) struct to the handlers
        return_list = [(self.message_hashes[name], struct)]
        self._forward_message(name, struct)
        # If we have leftovers, store them
        if start_skip + self.header_size + actual_size < len(data):
            self.remainder = data[start_skip + self.header_size + actual_size:]
        # If there might still be a message to read
        if len(self.remainder) > 0:
            return_list.append(self.unserialize('', persistent_start, persistent_end, keep_remainder))
        return return_list

