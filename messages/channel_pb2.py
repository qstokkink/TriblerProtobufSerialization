# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: channel.proto

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
  name='channel.proto',
  package='',
  serialized_pb=_b('\n\rchannel.proto\x1a\x0e\x64\x65\x66\x61ults.proto\"8\n\x07\x43hannel\x12\x12\n\x04name\x18\x01 \x02(\tB\x04\xc8>\xff\x01\x12\x19\n\x0b\x64\x65scription\x18\x02 \x02(\tB\x04\xc8>\xff\x07\"\x97\x01\n\x07Torrent\x12\x15\n\x08infohash\x18\x01 \x02(\tB\x03\xc8>\x14\x12\x11\n\ttimestamp\x18\x02 \x02(\x04\x12\x0c\n\x04name\x18\x03 \x02(\t\x12\x1c\n\x05\x66iles\x18\x04 \x03(\x0b\x32\r.Torrent.File\x12\x10\n\x08trackers\x18\x05 \x03(\t\x1a$\n\x04\x46ile\x12\x0c\n\x04path\x18\x01 \x02(\t\x12\x0e\n\x06length\x18\x02 \x02(\x03\"\x82\x02\n\x07\x43omment\x12\x0c\n\x04text\x18\x01 \x02(\t\x12\x11\n\ttimestamp\x18\x02 \x02(\x03\x12\x1b\n\x0eplaylistpacket\x18\x03 \x02(\tB\x03\xc8>\x14\x12\x15\n\x08infohash\x18\x04 \x02(\tB\x03\xc8>\x14\x12\x17\n\nreplytomid\x18\x05 \x02(\tB\x03\xc8>\x14\x12\x19\n\x11replytoglobaltime\x18\x06 \x02(\x03\x12\x1a\n\rreplyaftermid\x18\x07 \x02(\tB\x03\xc8>\x14\x12\x1c\n\x14replyafterglobaltime\x18\x08 \x02(\x03\x12\x18\n\x0bplaylistmid\x18\t \x02(\tB\x03\xc8>\x14\x12\x1a\n\x12playlistglobaltime\x18\n \x02(\x03\"\xb0\x01\n\x0cModification\x12\x18\n\x10modificationtype\x18\x01 \x02(\t\x12\x1f\n\x11modificationvalue\x18\x02 \x02(\tB\x04\xc8>\xff\x07\x12\x11\n\ttimestamp\x18\x03 \x02(\x03\x12\x10\n\x03mid\x18\x04 \x02(\tB\x03\xc8>\x14\x12\x12\n\nglobaltime\x18\x05 \x02(\x03\x12\x14\n\x07prevmid\x18\x06 \x02(\tB\x03\xc8>\x14\x12\x16\n\x0eprevglobaltime\x18\x07 \x02(\x03\"N\n\x0fPlaylistTorrent\x12\x15\n\x08infohash\x18\x01 \x02(\tB\x03\xc8>\x14\x12\x10\n\x03mid\x18\x02 \x02(\tB\x03\xc8>\x14\x12\x12\n\nglobaltime\x18\x03 \x02(\x04\")\n\x0eMissingChannel\x12\x17\n\x0fincludeSnapshot\x18\x01 \x02(\x08\"u\n\nModeration\x12\x12\n\x04text\x18\x01 \x02(\tB\x04\xc8>\xff\x07\x12\x11\n\ttimestamp\x18\x02 \x02(\x03\x12\x10\n\x08severity\x18\x03 \x02(\x03\x12\x15\n\x08\x63\x61usemid\x18\x04 \x02(\tB\x03\xc8>\x14\x12\x17\n\x0f\x63\x61useglobaltime\x18\x05 \x02(\x03\"J\n\x0bMarkTorrent\x12\x15\n\x08infohash\x18\x01 \x02(\tB\x03\xc8>\x14\x12\x11\n\ttimestamp\x18\x02 \x02(\x03\x12\x11\n\x04type\x18\x03 \x02(\tB\x03\xc8>\x18\"9\n\x08Playlist\x12\x12\n\x04name\x18\x01 \x02(\tB\x04\xc8>\xff\x01\x12\x19\n\x0b\x64\x65scription\x18\x02 \x02(\tB\x04\xc8>\xff\x07')
  ,
  dependencies=[defaults_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CHANNEL = _descriptor.Descriptor(
  name='Channel',
  full_name='Channel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Channel.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\377\001'))),
    _descriptor.FieldDescriptor(
      name='description', full_name='Channel.description', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\377\007'))),
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
  serialized_start=33,
  serialized_end=89,
)


_TORRENT_FILE = _descriptor.Descriptor(
  name='File',
  full_name='Torrent.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='Torrent.File.path', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='length', full_name='Torrent.File.length', index=1,
      number=2, type=3, cpp_type=2, label=2,
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
  serialized_start=207,
  serialized_end=243,
)

_TORRENT = _descriptor.Descriptor(
  name='Torrent',
  full_name='Torrent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='infohash', full_name='Torrent.infohash', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Torrent.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Torrent.name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='files', full_name='Torrent.files', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trackers', full_name='Torrent.trackers', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TORRENT_FILE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=243,
)


_COMMENT = _descriptor.Descriptor(
  name='Comment',
  full_name='Comment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='Comment.text', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Comment.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='playlistpacket', full_name='Comment.playlistpacket', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))),
    _descriptor.FieldDescriptor(
      name='infohash', full_name='Comment.infohash', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))),
    _descriptor.FieldDescriptor(
      name='replytomid', full_name='Comment.replytomid', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))),
    _descriptor.FieldDescriptor(
      name='replytoglobaltime', full_name='Comment.replytoglobaltime', index=5,
      number=6, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='replyaftermid', full_name='Comment.replyaftermid', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))),
    _descriptor.FieldDescriptor(
      name='replyafterglobaltime', full_name='Comment.replyafterglobaltime', index=7,
      number=8, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='playlistmid', full_name='Comment.playlistmid', index=8,
      number=9, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))),
    _descriptor.FieldDescriptor(
      name='playlistglobaltime', full_name='Comment.playlistglobaltime', index=9,
      number=10, type=3, cpp_type=2, label=2,
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
  serialized_start=246,
  serialized_end=504,
)


_MODIFICATION = _descriptor.Descriptor(
  name='Modification',
  full_name='Modification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='modificationtype', full_name='Modification.modificationtype', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modificationvalue', full_name='Modification.modificationvalue', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\377\007'))),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Modification.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mid', full_name='Modification.mid', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))),
    _descriptor.FieldDescriptor(
      name='globaltime', full_name='Modification.globaltime', index=4,
      number=5, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prevmid', full_name='Modification.prevmid', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))),
    _descriptor.FieldDescriptor(
      name='prevglobaltime', full_name='Modification.prevglobaltime', index=6,
      number=7, type=3, cpp_type=2, label=2,
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
  serialized_start=507,
  serialized_end=683,
)


_PLAYLISTTORRENT = _descriptor.Descriptor(
  name='PlaylistTorrent',
  full_name='PlaylistTorrent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='infohash', full_name='PlaylistTorrent.infohash', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))),
    _descriptor.FieldDescriptor(
      name='mid', full_name='PlaylistTorrent.mid', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))),
    _descriptor.FieldDescriptor(
      name='globaltime', full_name='PlaylistTorrent.globaltime', index=2,
      number=3, type=4, cpp_type=4, label=2,
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
  serialized_start=685,
  serialized_end=763,
)


_MISSINGCHANNEL = _descriptor.Descriptor(
  name='MissingChannel',
  full_name='MissingChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='includeSnapshot', full_name='MissingChannel.includeSnapshot', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=765,
  serialized_end=806,
)


_MODERATION = _descriptor.Descriptor(
  name='Moderation',
  full_name='Moderation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='Moderation.text', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\377\007'))),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Moderation.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='severity', full_name='Moderation.severity', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='causemid', full_name='Moderation.causemid', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))),
    _descriptor.FieldDescriptor(
      name='causeglobaltime', full_name='Moderation.causeglobaltime', index=4,
      number=5, type=3, cpp_type=2, label=2,
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
  serialized_start=808,
  serialized_end=925,
)


_MARKTORRENT = _descriptor.Descriptor(
  name='MarkTorrent',
  full_name='MarkTorrent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='infohash', full_name='MarkTorrent.infohash', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='MarkTorrent.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='MarkTorrent.type', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\030'))),
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
  serialized_start=927,
  serialized_end=1001,
)


_PLAYLIST = _descriptor.Descriptor(
  name='Playlist',
  full_name='Playlist',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Playlist.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\377\001'))),
    _descriptor.FieldDescriptor(
      name='description', full_name='Playlist.description', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\377\007'))),
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
  serialized_start=1003,
  serialized_end=1060,
)

_TORRENT_FILE.containing_type = _TORRENT
_TORRENT.fields_by_name['files'].message_type = _TORRENT_FILE
DESCRIPTOR.message_types_by_name['Channel'] = _CHANNEL
DESCRIPTOR.message_types_by_name['Torrent'] = _TORRENT
DESCRIPTOR.message_types_by_name['Comment'] = _COMMENT
DESCRIPTOR.message_types_by_name['Modification'] = _MODIFICATION
DESCRIPTOR.message_types_by_name['PlaylistTorrent'] = _PLAYLISTTORRENT
DESCRIPTOR.message_types_by_name['MissingChannel'] = _MISSINGCHANNEL
DESCRIPTOR.message_types_by_name['Moderation'] = _MODERATION
DESCRIPTOR.message_types_by_name['MarkTorrent'] = _MARKTORRENT
DESCRIPTOR.message_types_by_name['Playlist'] = _PLAYLIST

Channel = _reflection.GeneratedProtocolMessageType('Channel', (_message.Message,), dict(
  DESCRIPTOR = _CHANNEL,
  __module__ = 'channel_pb2'
  # @@protoc_insertion_point(class_scope:Channel)
  ))
_sym_db.RegisterMessage(Channel)

Torrent = _reflection.GeneratedProtocolMessageType('Torrent', (_message.Message,), dict(

  File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), dict(
    DESCRIPTOR = _TORRENT_FILE,
    __module__ = 'channel_pb2'
    # @@protoc_insertion_point(class_scope:Torrent.File)
    ))
  ,
  DESCRIPTOR = _TORRENT,
  __module__ = 'channel_pb2'
  # @@protoc_insertion_point(class_scope:Torrent)
  ))
_sym_db.RegisterMessage(Torrent)
_sym_db.RegisterMessage(Torrent.File)

Comment = _reflection.GeneratedProtocolMessageType('Comment', (_message.Message,), dict(
  DESCRIPTOR = _COMMENT,
  __module__ = 'channel_pb2'
  # @@protoc_insertion_point(class_scope:Comment)
  ))
_sym_db.RegisterMessage(Comment)

Modification = _reflection.GeneratedProtocolMessageType('Modification', (_message.Message,), dict(
  DESCRIPTOR = _MODIFICATION,
  __module__ = 'channel_pb2'
  # @@protoc_insertion_point(class_scope:Modification)
  ))
_sym_db.RegisterMessage(Modification)

PlaylistTorrent = _reflection.GeneratedProtocolMessageType('PlaylistTorrent', (_message.Message,), dict(
  DESCRIPTOR = _PLAYLISTTORRENT,
  __module__ = 'channel_pb2'
  # @@protoc_insertion_point(class_scope:PlaylistTorrent)
  ))
_sym_db.RegisterMessage(PlaylistTorrent)

MissingChannel = _reflection.GeneratedProtocolMessageType('MissingChannel', (_message.Message,), dict(
  DESCRIPTOR = _MISSINGCHANNEL,
  __module__ = 'channel_pb2'
  # @@protoc_insertion_point(class_scope:MissingChannel)
  ))
_sym_db.RegisterMessage(MissingChannel)

Moderation = _reflection.GeneratedProtocolMessageType('Moderation', (_message.Message,), dict(
  DESCRIPTOR = _MODERATION,
  __module__ = 'channel_pb2'
  # @@protoc_insertion_point(class_scope:Moderation)
  ))
_sym_db.RegisterMessage(Moderation)

MarkTorrent = _reflection.GeneratedProtocolMessageType('MarkTorrent', (_message.Message,), dict(
  DESCRIPTOR = _MARKTORRENT,
  __module__ = 'channel_pb2'
  # @@protoc_insertion_point(class_scope:MarkTorrent)
  ))
_sym_db.RegisterMessage(MarkTorrent)

Playlist = _reflection.GeneratedProtocolMessageType('Playlist', (_message.Message,), dict(
  DESCRIPTOR = _PLAYLIST,
  __module__ = 'channel_pb2'
  # @@protoc_insertion_point(class_scope:Playlist)
  ))
_sym_db.RegisterMessage(Playlist)


_CHANNEL.fields_by_name['name'].has_options = True
_CHANNEL.fields_by_name['name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\377\001'))
_CHANNEL.fields_by_name['description'].has_options = True
_CHANNEL.fields_by_name['description']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\377\007'))
_TORRENT.fields_by_name['infohash'].has_options = True
_TORRENT.fields_by_name['infohash']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))
_COMMENT.fields_by_name['playlistpacket'].has_options = True
_COMMENT.fields_by_name['playlistpacket']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))
_COMMENT.fields_by_name['infohash'].has_options = True
_COMMENT.fields_by_name['infohash']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))
_COMMENT.fields_by_name['replytomid'].has_options = True
_COMMENT.fields_by_name['replytomid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))
_COMMENT.fields_by_name['replyaftermid'].has_options = True
_COMMENT.fields_by_name['replyaftermid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))
_COMMENT.fields_by_name['playlistmid'].has_options = True
_COMMENT.fields_by_name['playlistmid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))
_MODIFICATION.fields_by_name['modificationvalue'].has_options = True
_MODIFICATION.fields_by_name['modificationvalue']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\377\007'))
_MODIFICATION.fields_by_name['mid'].has_options = True
_MODIFICATION.fields_by_name['mid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))
_MODIFICATION.fields_by_name['prevmid'].has_options = True
_MODIFICATION.fields_by_name['prevmid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))
_PLAYLISTTORRENT.fields_by_name['infohash'].has_options = True
_PLAYLISTTORRENT.fields_by_name['infohash']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))
_PLAYLISTTORRENT.fields_by_name['mid'].has_options = True
_PLAYLISTTORRENT.fields_by_name['mid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))
_MODERATION.fields_by_name['text'].has_options = True
_MODERATION.fields_by_name['text']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\377\007'))
_MODERATION.fields_by_name['causemid'].has_options = True
_MODERATION.fields_by_name['causemid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))
_MARKTORRENT.fields_by_name['infohash'].has_options = True
_MARKTORRENT.fields_by_name['infohash']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\024'))
_MARKTORRENT.fields_by_name['type'].has_options = True
_MARKTORRENT.fields_by_name['type']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\030'))
_PLAYLIST.fields_by_name['name'].has_options = True
_PLAYLIST.fields_by_name['name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\377\001'))
_PLAYLIST.fields_by_name['description'].has_options = True
_PLAYLIST.fields_by_name['description']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310>\377\007'))
# @@protoc_insertion_point(module_scope)
