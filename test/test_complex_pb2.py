# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_complex.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import messages.defaults_pb2 as defaults_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_complex.proto',
  package='',
  serialized_pb=_b('\n\x12test_complex.proto\x1a\x0e\x64\x65\x66\x61ults.proto\"i\n\x0bTestComplex\x12$\n\x07nesteds\x18\x01 \x03(\x0b\x32\x13.TestComplex.Nested\x1a\x34\n\x06Nested\x12\x13\n\x06normal\x18\x01 \x02(\tB\x03\xc8>\x14\x12\x15\n\x08multiple\x18\x02 \x03(\tB\x03\xc8>\x14')
  ,
  dependencies=[defaults_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TESTCOMPLEX_NESTED = _descriptor.Descriptor(
  name='Nested',
  full_name='TestComplex.Nested',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='normal', full_name='TestComplex.Nested.normal', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))),
    _descriptor.FieldDescriptor(
      name='multiple', full_name='TestComplex.Nested.multiple', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))),
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
  serialized_start=91,
  serialized_end=143,
)

_TESTCOMPLEX = _descriptor.Descriptor(
  name='TestComplex',
  full_name='TestComplex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nesteds', full_name='TestComplex.nesteds', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TESTCOMPLEX_NESTED, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=143,
)

_TESTCOMPLEX_NESTED.containing_type = _TESTCOMPLEX
_TESTCOMPLEX.fields_by_name['nesteds'].message_type = _TESTCOMPLEX_NESTED
DESCRIPTOR.message_types_by_name['TestComplex'] = _TESTCOMPLEX

TestComplex = _reflection.GeneratedProtocolMessageType('TestComplex', (_message.Message,), dict(

  Nested = _reflection.GeneratedProtocolMessageType('Nested', (_message.Message,), dict(
    DESCRIPTOR = _TESTCOMPLEX_NESTED,
    __module__ = 'test_complex_pb2'
    # @@protoc_insertion_point(class_scope:TestComplex.Nested)
    ))
  ,
  DESCRIPTOR = _TESTCOMPLEX,
  __module__ = 'test_complex_pb2'
  # @@protoc_insertion_point(class_scope:TestComplex)
  ))
_sym_db.RegisterMessage(TestComplex)
_sym_db.RegisterMessage(TestComplex.Nested)


_TESTCOMPLEX_NESTED.fields_by_name['normal'].has_options = True
_TESTCOMPLEX_NESTED.fields_by_name['normal']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))
_TESTCOMPLEX_NESTED.fields_by_name['multiple'].has_options = True
_TESTCOMPLEX_NESTED.fields_by_name['multiple']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))
# @@protoc_insertion_point(module_scope)
