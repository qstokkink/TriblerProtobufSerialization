class SerializerException(Exception):

    """Parent Exception for all Exceptions raised by the 
        Serializer class.
    """

    pass

class MessageNameTooLongException(SerializerException):

    """Exception for when the name of a message is too long,
        ergo longer than 20 characters.
    """

    pass

class UnknownMessageException(SerializerException):

    """Exception for when a message of unknown name is to be
        serialized. Probably a programmer typo.
    """

    pass

class FieldTooLongException(SerializerException):

    """Exception for when the amount of bytes used by serialized
        data surpasses the allowed amount of bytes.
    """

    pass

class FieldNotDefinedException(SerializerException):

    """Exception for when a field definition is not supplied 
        when serializing.
    """

    pass

class FieldWrongTypeException(SerializerException):

    """Exception for when the type of the serialized object
        does not match the definition in the Protobuf message.
    """

    pass

class FieldLengthUnsupportedException(SerializerException):

    """Exception for when the length option is forced upon a type
        which does not support it. Only string, int and long are
        supported.
    """

    pass
