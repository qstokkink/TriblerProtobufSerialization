# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: allchannel.proto

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
  name='allchannel.proto',
  package='',
  serialized_pb=_b('\n\x10\x61llchannel.proto\x1a\x0e\x64\x65\x66\x61ults.proto\"k\n\x0b\x43hannelCast\x12&\n\x08torrents\x18\x01 \x03(\x0b\x32\x14.ChannelCast.Torrent\x1a\x34\n\x07Torrent\x12\x10\n\x03\x63id\x18\x01 \x02(\tB\x03\xc8>\x14\x12\x17\n\ninfohashes\x18\x02 \x03(\tB\x03\xc8>\x14\"y\n\x12\x43hannelCastRequest\x12-\n\x08torrents\x18\x01 \x03(\x0b\x32\x1b.ChannelCastRequest.Torrent\x1a\x34\n\x07Torrent\x12\x10\n\x03\x63id\x18\x01 \x02(\tB\x03\xc8>\x14\x12\x17\n\ninfohashes\x18\x02 \x03(\tB\x03\xc8>\x14\"!\n\rChannelSearch\x12\x10\n\x08keywords\x18\x01 \x03(\t\"\x91\x01\n\x15\x43hannelSearchResponse\x12\x10\n\x08keywords\x18\x01 \x03(\t\x12\x30\n\x08torrents\x18\x02 \x03(\x0b\x32\x1e.ChannelSearchResponse.Torrent\x1a\x34\n\x07Torrent\x12\x10\n\x03\x63id\x18\x01 \x02(\tB\x03\xc8>\x14\x12\x17\n\ninfohashes\x18\x02 \x03(\tB\x03\xc8>\x14\"B\n\x08Votecast\x12\x10\n\x03\x63id\x18\x01 \x02(\tB\x03\xc8>\x14\x12\x11\n\x04vote\x18\x02 \x02(\x05\x42\x03\xc8>\x02\x12\x11\n\ttimestamp\x18\x03 \x02(\x03')
  ,
  dependencies=[defaults_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CHANNELCAST_TORRENT = _descriptor.Descriptor(
  name='Torrent',
  full_name='ChannelCast.Torrent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cid', full_name='ChannelCast.Torrent.cid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))),
    _descriptor.FieldDescriptor(
      name='infohashes', full_name='ChannelCast.Torrent.infohashes', index=1,
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

_CHANNELCAST = _descriptor.Descriptor(
  name='ChannelCast',
  full_name='ChannelCast',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='torrents', full_name='ChannelCast.torrents', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CHANNELCAST_TORRENT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=143,
)


_CHANNELCASTREQUEST_TORRENT = _descriptor.Descriptor(
  name='Torrent',
  full_name='ChannelCastRequest.Torrent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cid', full_name='ChannelCastRequest.Torrent.cid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))),
    _descriptor.FieldDescriptor(
      name='infohashes', full_name='ChannelCastRequest.Torrent.infohashes', index=1,
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

_CHANNELCASTREQUEST = _descriptor.Descriptor(
  name='ChannelCastRequest',
  full_name='ChannelCastRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='torrents', full_name='ChannelCastRequest.torrents', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CHANNELCASTREQUEST_TORRENT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=266,
)


_CHANNELSEARCH = _descriptor.Descriptor(
  name='ChannelSearch',
  full_name='ChannelSearch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keywords', full_name='ChannelSearch.keywords', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=268,
  serialized_end=301,
)


_CHANNELSEARCHRESPONSE_TORRENT = _descriptor.Descriptor(
  name='Torrent',
  full_name='ChannelSearchResponse.Torrent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cid', full_name='ChannelSearchResponse.Torrent.cid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))),
    _descriptor.FieldDescriptor(
      name='infohashes', full_name='ChannelSearchResponse.Torrent.infohashes', index=1,
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

_CHANNELSEARCHRESPONSE = _descriptor.Descriptor(
  name='ChannelSearchResponse',
  full_name='ChannelSearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keywords', full_name='ChannelSearchResponse.keywords', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='torrents', full_name='ChannelSearchResponse.torrents', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CHANNELSEARCHRESPONSE_TORRENT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=304,
  serialized_end=449,
)


_VOTECAST = _descriptor.Descriptor(
  name='Votecast',
  full_name='Votecast',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cid', full_name='Votecast.cid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))),
    _descriptor.FieldDescriptor(
      name='vote', full_name='Votecast.vote', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\002'))),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Votecast.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=2,
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
  serialized_start=451,
  serialized_end=517,
)

_CHANNELCAST_TORRENT.containing_type = _CHANNELCAST
_CHANNELCAST.fields_by_name['torrents'].message_type = _CHANNELCAST_TORRENT
_CHANNELCASTREQUEST_TORRENT.containing_type = _CHANNELCASTREQUEST
_CHANNELCASTREQUEST.fields_by_name['torrents'].message_type = _CHANNELCASTREQUEST_TORRENT
_CHANNELSEARCHRESPONSE_TORRENT.containing_type = _CHANNELSEARCHRESPONSE
_CHANNELSEARCHRESPONSE.fields_by_name['torrents'].message_type = _CHANNELSEARCHRESPONSE_TORRENT
DESCRIPTOR.message_types_by_name['ChannelCast'] = _CHANNELCAST
DESCRIPTOR.message_types_by_name['ChannelCastRequest'] = _CHANNELCASTREQUEST
DESCRIPTOR.message_types_by_name['ChannelSearch'] = _CHANNELSEARCH
DESCRIPTOR.message_types_by_name['ChannelSearchResponse'] = _CHANNELSEARCHRESPONSE
DESCRIPTOR.message_types_by_name['Votecast'] = _VOTECAST

ChannelCast = _reflection.GeneratedProtocolMessageType('ChannelCast', (_message.Message,), dict(

  Torrent = _reflection.GeneratedProtocolMessageType('Torrent', (_message.Message,), dict(
    DESCRIPTOR = _CHANNELCAST_TORRENT,
    __module__ = 'allchannel_pb2'
    # @@protoc_insertion_point(class_scope:ChannelCast.Torrent)
    ))
  ,
  DESCRIPTOR = _CHANNELCAST,
  __module__ = 'allchannel_pb2'
  # @@protoc_insertion_point(class_scope:ChannelCast)
  ))
_sym_db.RegisterMessage(ChannelCast)
_sym_db.RegisterMessage(ChannelCast.Torrent)

ChannelCastRequest = _reflection.GeneratedProtocolMessageType('ChannelCastRequest', (_message.Message,), dict(

  Torrent = _reflection.GeneratedProtocolMessageType('Torrent', (_message.Message,), dict(
    DESCRIPTOR = _CHANNELCASTREQUEST_TORRENT,
    __module__ = 'allchannel_pb2'
    # @@protoc_insertion_point(class_scope:ChannelCastRequest.Torrent)
    ))
  ,
  DESCRIPTOR = _CHANNELCASTREQUEST,
  __module__ = 'allchannel_pb2'
  # @@protoc_insertion_point(class_scope:ChannelCastRequest)
  ))
_sym_db.RegisterMessage(ChannelCastRequest)
_sym_db.RegisterMessage(ChannelCastRequest.Torrent)

ChannelSearch = _reflection.GeneratedProtocolMessageType('ChannelSearch', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELSEARCH,
  __module__ = 'allchannel_pb2'
  # @@protoc_insertion_point(class_scope:ChannelSearch)
  ))
_sym_db.RegisterMessage(ChannelSearch)

ChannelSearchResponse = _reflection.GeneratedProtocolMessageType('ChannelSearchResponse', (_message.Message,), dict(

  Torrent = _reflection.GeneratedProtocolMessageType('Torrent', (_message.Message,), dict(
    DESCRIPTOR = _CHANNELSEARCHRESPONSE_TORRENT,
    __module__ = 'allchannel_pb2'
    # @@protoc_insertion_point(class_scope:ChannelSearchResponse.Torrent)
    ))
  ,
  DESCRIPTOR = _CHANNELSEARCHRESPONSE,
  __module__ = 'allchannel_pb2'
  # @@protoc_insertion_point(class_scope:ChannelSearchResponse)
  ))
_sym_db.RegisterMessage(ChannelSearchResponse)
_sym_db.RegisterMessage(ChannelSearchResponse.Torrent)

Votecast = _reflection.GeneratedProtocolMessageType('Votecast', (_message.Message,), dict(
  DESCRIPTOR = _VOTECAST,
  __module__ = 'allchannel_pb2'
  # @@protoc_insertion_point(class_scope:Votecast)
  ))
_sym_db.RegisterMessage(Votecast)


_CHANNELCAST_TORRENT.fields_by_name['cid'].has_options = True
_CHANNELCAST_TORRENT.fields_by_name['cid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))
_CHANNELCAST_TORRENT.fields_by_name['infohashes'].has_options = True
_CHANNELCAST_TORRENT.fields_by_name['infohashes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))
_CHANNELCASTREQUEST_TORRENT.fields_by_name['cid'].has_options = True
_CHANNELCASTREQUEST_TORRENT.fields_by_name['cid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))
_CHANNELCASTREQUEST_TORRENT.fields_by_name['infohashes'].has_options = True
_CHANNELCASTREQUEST_TORRENT.fields_by_name['infohashes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))
_CHANNELSEARCHRESPONSE_TORRENT.fields_by_name['cid'].has_options = True
_CHANNELSEARCHRESPONSE_TORRENT.fields_by_name['cid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))
_CHANNELSEARCHRESPONSE_TORRENT.fields_by_name['infohashes'].has_options = True
_CHANNELSEARCHRESPONSE_TORRENT.fields_by_name['infohashes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))
_VOTECAST.fields_by_name['cid'].has_options = True
_VOTECAST.fields_by_name['cid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))
_VOTECAST.fields_by_name['vote'].has_options = True
_VOTECAST.fields_by_name['vote']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\002'))
# @@protoc_insertion_point(module_scope)