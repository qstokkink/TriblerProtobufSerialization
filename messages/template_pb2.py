# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: template.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import defaults_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='template.proto',
  package='',
  serialized_pb=_b('\n\x0etemplate.proto\x1a\x0e\x64\x65\x66\x61ults.proto\"\x19\n\x04Text\x12\x11\n\x04text\x18\x01 \x02(\rB\x03\xc8>\x01')
  ,
  dependencies=[defaults_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TEXT = _descriptor.Descriptor(
  name='Text',
  full_name='Text',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='Text.text', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=59,
)

DESCRIPTOR.message_types_by_name['Text'] = _TEXT

Text = _reflection.GeneratedProtocolMessageType('Text', (_message.Message,), dict(
  DESCRIPTOR = _TEXT,
  __module__ = 'template_pb2'
  # @@protoc_insertion_point(class_scope:Text)
  ))
_sym_db.RegisterMessage(Text)


_TEXT.fields_by_name['text'].has_options = True
_TEXT.fields_by_name['text']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\001'))
# @@protoc_insertion_point(module_scope)
