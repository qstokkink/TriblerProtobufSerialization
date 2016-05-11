"""This is a modified version of automatic output.
The avoids repackaging existing code.
"""

import sys
from google.protobuf import descriptor as _descriptor
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
  name='defaults.proto',
  package='',
  serialized_pb=_b('\n\x0e\x64\x65\x66\x61ults.proto\n\x06length\x12\x1d.google.protobuf.FieldOptions\x18\xe9\x07 \x01(\x05')
  ,
  dependencies=[])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LENGTH_FIELD_NUMBER = 1001
length = _descriptor.FieldDescriptor(
  name='length', full_name='length', index=0,
  number=1001, type=5, cpp_type=1, label=1,
  has_default_value=False, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)

DESCRIPTOR.extensions_by_name['length'] = length

descriptor_pb2.FieldOptions.RegisterExtension(length)
