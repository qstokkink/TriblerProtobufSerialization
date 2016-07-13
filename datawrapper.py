class Wrapper:

    """Class to wrap Protocol Buffers output
        classes, automatically converts 
        internal unicode strings to normal
        strings.
    """

    def __init__(self, pb_field):
        """Set up wrapper using a protobuf
            field object.
        """
        self.innerdict = {}
        self.innerlist = []
        self.wrapped = pb_field
        if hasattr(pb_field, 'DESCRIPTOR'):
            for field in pb_field.DESCRIPTOR.fields:
                value = getattr(pb_field, field.name)
                if self._is_non_native(value):
                    self.innerdict[field.name] = Wrapper(value)
                    if self.innerdict[field.name].innerlist:
                        self.innerdict[field.name] = self.innerdict[field.name].innerlist
                else:
                    self.innerdict[field.name] = self._unicode_to_str(value)
        elif self._is_non_native(pb_field):
            for x in list(pb_field):
                if self._is_non_native(x):
                    value = Wrapper(x)
                    if value.innerlist:
                        self.innerlist.append(value.innerlist)
                    else:
                        self.innerlist.append(value)
                else:
                    self.innerlist.append(self._unicode_to_str(x))
        else:
            # We should not be wrapping native datatypes
            raise RuntimeError()

    def _is_non_native(self, o):
        return (hasattr(o, 'DESCRIPTOR') or hasattr(o, 'append') or hasattr(o, 'MergeFrom'))

    def _unicode_to_str(self, s):
        """Convert an internal unicode string
            to a normal string.

            :param s: string to convert
        """
        if isinstance(s, unicode):
            return "".join([chr(ord(c)) for c in s])
        return s

    def ListFields(self):
        """Overwrite ListFields to produce the corrected
            output (disallows accidental bypass).
        """
        return [(self.wrapped.DESCRIPTOR if hasattr(self.wrapped, 'DESCRIPTOR') else None, self.innerdict[key]) for key in self.innerdict]

    def __getattr__(self, name):
        """Overwrite getattr to provide the same
            functionality as protobuf.

            :param name: name of the attribute to get
        """
        if name in self.innerdict:
            return self.innerdict[name]
        elif hasattr(self.wrapped, name):
            return getattr(self.wrapped, name)
        else:
            raise AttributeError
