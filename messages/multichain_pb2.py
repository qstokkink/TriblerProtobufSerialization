# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: multichain.proto

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
  name='multichain.proto',
  package='',
  serialized_pb=_b('\n\x10multichain.proto\x1a\x0e\x64\x65\x66\x61ults.proto\"\x9b\x02\n\tSignature\x12\n\n\x02up\x18\x01 \x02(\r\x12\x0c\n\x04\x64own\x18\x02 \x02(\r\x12\x18\n\x10totaluprequester\x18\x03 \x02(\x04\x12\x1a\n\x12totaldownrequester\x18\x04 \x02(\x04\x12\x1f\n\x17sequencenumberrequester\x18\x05 \x02(\x05\x12\"\n\x15previoushashrequester\x18\x06 \x02(\tB\x03\xc8> \x12\x18\n\x10totalupresponder\x18\x07 \x02(\x04\x12\x1a\n\x12totaldownresponder\x18\x08 \x02(\x04\x12\x1f\n\x17sequencenumberresponder\x18\t \x02(\x05\x12\"\n\x15previoushashresponder\x18\n \x02(\tB\x03\xc8> \"/\n\x0c\x43rawlRequest\x12\x1f\n\x17requestedsequencenumber\x18\x01 \x02(\x05\"\xa3\x03\n\rCrawlResponse\x12\n\n\x02up\x18\x01 \x02(\r\x12\x0c\n\x04\x64own\x18\x02 \x02(\r\x12\x18\n\x10totaluprequester\x18\x03 \x02(\x04\x12\x1a\n\x12totaldownrequester\x18\x04 \x02(\x04\x12\x1f\n\x17sequencenumberrequester\x18\x05 \x02(\x05\x12\"\n\x15previoushashrequester\x18\x06 \x02(\tB\x03\xc8> \x12\x18\n\x10totalupresponder\x18\x07 \x02(\x04\x12\x1a\n\x12totaldownresponder\x18\x08 \x02(\x04\x12\x1f\n\x17sequencenumberresponder\x18\t \x02(\x05\x12\"\n\x15previoushashresponder\x18\n \x02(\tB\x03\xc8> \x12\x1f\n\x12signaturerequester\x18\x0b \x02(\tB\x03\xc8>J\x12\x1f\n\x12publickeyrequester\x18\x0c \x02(\tB\x03\xc8>@\x12\x1f\n\x12signatureresponder\x18\r \x02(\tB\x03\xc8>J\x12\x1f\n\x12publickeyresponder\x18\x0e \x02(\tB\x03\xc8>@\"\r\n\x0b\x43rawlResume')
  ,
  dependencies=[defaults_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SIGNATURE = _descriptor.Descriptor(
  name='Signature',
  full_name='Signature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='up', full_name='Signature.up', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='down', full_name='Signature.down', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='totaluprequester', full_name='Signature.totaluprequester', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='totaldownrequester', full_name='Signature.totaldownrequester', index=3,
      number=4, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sequencenumberrequester', full_name='Signature.sequencenumberrequester', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='previoushashrequester', full_name='Signature.previoushashrequester', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310> '))),
    _descriptor.FieldDescriptor(
      name='totalupresponder', full_name='Signature.totalupresponder', index=6,
      number=7, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='totaldownresponder', full_name='Signature.totaldownresponder', index=7,
      number=8, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sequencenumberresponder', full_name='Signature.sequencenumberresponder', index=8,
      number=9, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='previoushashresponder', full_name='Signature.previoushashresponder', index=9,
      number=10, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310> '))),
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
  serialized_start=37,
  serialized_end=320,
)


_CRAWLREQUEST = _descriptor.Descriptor(
  name='CrawlRequest',
  full_name='CrawlRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestedsequencenumber', full_name='CrawlRequest.requestedsequencenumber', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=322,
  serialized_end=369,
)


_CRAWLRESPONSE = _descriptor.Descriptor(
  name='CrawlResponse',
  full_name='CrawlResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='up', full_name='CrawlResponse.up', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='down', full_name='CrawlResponse.down', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='totaluprequester', full_name='CrawlResponse.totaluprequester', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='totaldownrequester', full_name='CrawlResponse.totaldownrequester', index=3,
      number=4, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sequencenumberrequester', full_name='CrawlResponse.sequencenumberrequester', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='previoushashrequester', full_name='CrawlResponse.previoushashrequester', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310> '))),
    _descriptor.FieldDescriptor(
      name='totalupresponder', full_name='CrawlResponse.totalupresponder', index=6,
      number=7, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='totaldownresponder', full_name='CrawlResponse.totaldownresponder', index=7,
      number=8, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sequencenumberresponder', full_name='CrawlResponse.sequencenumberresponder', index=8,
      number=9, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='previoushashresponder', full_name='CrawlResponse.previoushashresponder', index=9,
      number=10, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310> '))),
    _descriptor.FieldDescriptor(
      name='signaturerequester', full_name='CrawlResponse.signaturerequester', index=10,
      number=11, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>J'))),
    _descriptor.FieldDescriptor(
      name='publickeyrequester', full_name='CrawlResponse.publickeyrequester', index=11,
      number=12, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>@'))),
    _descriptor.FieldDescriptor(
      name='signatureresponder', full_name='CrawlResponse.signatureresponder', index=12,
      number=13, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>J'))),
    _descriptor.FieldDescriptor(
      name='publickeyresponder', full_name='CrawlResponse.publickeyresponder', index=13,
      number=14, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>@'))),
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
  serialized_start=372,
  serialized_end=791,
)


_CRAWLRESUME = _descriptor.Descriptor(
  name='CrawlResume',
  full_name='CrawlResume',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=793,
  serialized_end=806,
)

DESCRIPTOR.message_types_by_name['Signature'] = _SIGNATURE
DESCRIPTOR.message_types_by_name['CrawlRequest'] = _CRAWLREQUEST
DESCRIPTOR.message_types_by_name['CrawlResponse'] = _CRAWLRESPONSE
DESCRIPTOR.message_types_by_name['CrawlResume'] = _CRAWLRESUME

Signature = _reflection.GeneratedProtocolMessageType('Signature', (_message.Message,), dict(
  DESCRIPTOR = _SIGNATURE,
  __module__ = 'multichain_pb2'
  # @@protoc_insertion_point(class_scope:Signature)
  ))
_sym_db.RegisterMessage(Signature)

CrawlRequest = _reflection.GeneratedProtocolMessageType('CrawlRequest', (_message.Message,), dict(
  DESCRIPTOR = _CRAWLREQUEST,
  __module__ = 'multichain_pb2'
  # @@protoc_insertion_point(class_scope:CrawlRequest)
  ))
_sym_db.RegisterMessage(CrawlRequest)

CrawlResponse = _reflection.GeneratedProtocolMessageType('CrawlResponse', (_message.Message,), dict(
  DESCRIPTOR = _CRAWLRESPONSE,
  __module__ = 'multichain_pb2'
  # @@protoc_insertion_point(class_scope:CrawlResponse)
  ))
_sym_db.RegisterMessage(CrawlResponse)

CrawlResume = _reflection.GeneratedProtocolMessageType('CrawlResume', (_message.Message,), dict(
  DESCRIPTOR = _CRAWLRESUME,
  __module__ = 'multichain_pb2'
  # @@protoc_insertion_point(class_scope:CrawlResume)
  ))
_sym_db.RegisterMessage(CrawlResume)


_SIGNATURE.fields_by_name['previoushashrequester'].has_options = True
_SIGNATURE.fields_by_name['previoushashrequester']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310> '))
_SIGNATURE.fields_by_name['previoushashresponder'].has_options = True
_SIGNATURE.fields_by_name['previoushashresponder']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310> '))
_CRAWLRESPONSE.fields_by_name['previoushashrequester'].has_options = True
_CRAWLRESPONSE.fields_by_name['previoushashrequester']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310> '))
_CRAWLRESPONSE.fields_by_name['previoushashresponder'].has_options = True
_CRAWLRESPONSE.fields_by_name['previoushashresponder']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310> '))
_CRAWLRESPONSE.fields_by_name['signaturerequester'].has_options = True
_CRAWLRESPONSE.fields_by_name['signaturerequester']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>J'))
_CRAWLRESPONSE.fields_by_name['publickeyrequester'].has_options = True
_CRAWLRESPONSE.fields_by_name['publickeyrequester']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>@'))
_CRAWLRESPONSE.fields_by_name['signatureresponder'].has_options = True
_CRAWLRESPONSE.fields_by_name['signatureresponder']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>J'))
_CRAWLRESPONSE.fields_by_name['publickeyresponder'].has_options = True
_CRAWLRESPONSE.fields_by_name['publickeyresponder']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>@'))
# @@protoc_insertion_point(module_scope)
