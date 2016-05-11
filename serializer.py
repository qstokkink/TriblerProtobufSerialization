import google.protobuf
import logging
from struct import pack, unpack_from
from struct import error as struct_error
import sys

import messages
import exceptions

class Serializer:

    """Class to serialize data by means of Protocol Buffers message
        definitions.
    """

    def __init__(self, autoload=True):
        """Initialize a new Serializer.

            :param autoload: call load_definitions after initialization
        """
        self.messages = {}
        self.handlers = {}
        self.remainder = ""
        if autoload:
            self.load_definitions()

    def load_definitions(self):
        """Load the protobuffers definitions from the messages module.
        """
        for module in messages.MESSAGES:
            names = module.DESCRIPTOR.message_types_by_name
            for message_name in names:
                if message_name in self.messages:
                    logging.warning("Serializer read duplicate message!" +
                                        "Overwriting definition of " + message_name)
                self.messages[message_name] = getattr(module, message_name)

    def add_handler(self, name, callback):
        """Add a callback to be fired when a certain message type has been
            received.

            :param name: the name of the messages to handle
            :param callback: the function to be called with the message
        """
        if not (name in self.handlers):
            self.handlers[name] = []
        self.handlers[name].append(callback)

    def add_package_handler(self, package_name, cls):
        """Add a handler which handles all messages for a certain package.
            Callbacks will be performed with cls member function of the name:
                on_<lowercase message name>()

            Accepts packages names as:
                - Full python class path
                - Full python class path minus '_pb2'
                - Python class/.proto name
                - .proto name
                - .proto package

            :param package_name: the name of the package of the messages
            :param cls: the callback class
        """
        for module in messages.MESSAGES:
            if ((module.__name__ == package_name) or 
                (module.__name__.replace('_pb2', '') == package_name) or 
                (module.DESCRIPTOR.name == package_name) or 
                (module.DESCRIPTOR.name.replace('.proto', '') == package_name) or
                (module.DESCRIPTOR.package == package_name)):
                for name in module.DESCRIPTOR.message_types_by_name:
                    self.add_handler(name, getattr(cls, 'on_' + name.lower()))

    def __gt_by_type(self, value, setting):
        """Check if a value has a length in bytes, shorter than some setting.
            Note that this is the worst-case length, as values can be packed.

            :param value: the value to check (string, int or long)
            :param setting: the maximum length in bytes
        """
        if isinstance(value, str):
            # Protobuf uses unicode strings internally
            return len(value.encode('utf-8')) > setting
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

    def check_field_length(self, field, value):
        """Check if a field has a valid value set.
            Throws a FieldTooLongException if it doesn't.

            :param field: the field descriptor object
            :param value: the value set for the field
        """
        for (option, setting) in field.GetOptions().ListFields():
            if option.name == "length":
                if self.__gt_by_type(value, setting):
                    raise FieldTooLongException("The field '" + field.name +
                        "' is bigger than the allowed " + str(setting) + " bytes")

    def serialize(self, name, *args, **kwargs):
        """Serialize a message of a certain type.

            :param name: the name of the message to serialize
            :param args: the fields of the message in order
            :param kwargs: the (remaining) fields of the message by field name
            :returns: the serialization as a binary string 
        """ 
        if not (name in self.messages):
            raise UnknownMessageException("Tried to provide serialization for " + 
                                            "unknown message '" + name + "'")
        if len(name) > 20:
            raise MessageNameTooLongException("The message name " + name +
                                                " is longer than 20 characters")
        struct = self.messages[name]()
        index = 0
        for field in struct.DESCRIPTOR.fields:
            # Loop through the fields in order of definition
            # If we can't, the fields have to be initialized by the
            #   keyword arguments
            value = args[index] if index < len(args) else kwargs.get(field.name)
            # dict.get() returns None if the entry was not found
            if not value:
                raise FieldNotDefinedException("The field '" + field.name +
                    "' was not defined when serializing a '" + name + "'")
            try:
                setattr(struct, field.name, value)
            except TypeError, e:
                raise FieldWrongTypeException("Tried to set the field '" + field.name +
                    "' to " + str(e).replace('has type', 'which has the type'))
            # Check if a custom byte length was specified
            self.check_field_length(field, value)
            index += 1
        return pack('20s', name) + struct.SerializePartialToString()

    def unserialize(self, data, persistent_start=True, 
                    persistent_end=True, keep_remainder=False):
        """Given some data, try to read serializations from it.

            :param data: the raw binary data to interpret
            :param persistent_start: while unserializable pop the first character
            :param persistent_end: while unserializable pop the last character
            :param keep_remainder: feed the data after a valid entry 
                                    to the next call
        """
        data = self.remainder + data
        name = ""
        sbuffer = data
        # Skip characters until a valid message id appears
        while persistent_start and len(sbuffer) > 20:
            (header, ) = unpack_from('20s', sbuffer)
            header = header.replace('\x00','')
            if header in self.messages:
                name = header
                break
            sbuffer = sbuffer[1:]
        if not name:
            if keep_remainder:
                self.remainder = data
            return
        # The message id is valid
        start_skip = len(data) - len(sbuffer)
        sbuffer = sbuffer[20:]
        struct = self.messages[name]()
        while persistent_end and (not struct.IsInitialized()) and (len(sbuffer) > 0):
            try:
                struct.MergeFromString(sbuffer)
            except google.protobuf.message.DecodeError, e:
                # This is nasty, but saves a lot of time
                if 'Truncated' in str(e):
                    # There is not enough message left
                    if keep_remainder:
                        self.remainder = data
                    return
                sbuffer = sbuffer[:-1]
        if not struct.IsInitialized():
            if keep_remainder:
                self.remainder = data
            return
        end_skip = len(data) - len(sbuffer) - start_skip
        # Forward the (now valid) struct to the handlers
        if name in self.handlers:
            for handler in self.handlers[name]:
                handler(struct)
        # If we have leftovers, store them
        if keep_remainder and end_skip:
            self.remainder = data[:-end_skip]

