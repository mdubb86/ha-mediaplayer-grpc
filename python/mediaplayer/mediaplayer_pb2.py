# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediaplayer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediaplayer.proto',
  package='mediaplayer',
  syntax='proto3',
  serialized_options=b'\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001Z\036github.com/mdubb86/mediaplayer',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11mediaplayer.proto\x12\x0bmediaplayer\"\x1e\n\x0cSetVolumeReq\x12\x0e\n\x06volume\x18\x01 \x01(\x02\"\x0e\n\x0cSetVolumeRes\"\x12\n\x10StreamUpdatesReq\"\'\n\x06Update\x12\x0e\n\x06volume\x18\x01 \x01(\x02\x12\r\n\x05muted\x18\x02 \x01(\x08\x32\x9b\x01\n\x0bMediaPlayer\x12\x43\n\tSetVolume\x12\x19.mediaplayer.SetVolumeReq\x1a\x19.mediaplayer.SetVolumeRes\"\x00\x12G\n\rStreamUpdates\x12\x1d.mediaplayer.StreamUpdatesReq\x1a\x13.mediaplayer.Update\"\x00\x30\x01\x42P\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01Z\x1egithub.com/mdubb86/mediaplayerb\x06proto3'
)




_SETVOLUMEREQ = _descriptor.Descriptor(
  name='SetVolumeReq',
  full_name='mediaplayer.SetVolumeReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='volume', full_name='mediaplayer.SetVolumeReq.volume', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=64,
)


_SETVOLUMERES = _descriptor.Descriptor(
  name='SetVolumeRes',
  full_name='mediaplayer.SetVolumeRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=80,
)


_STREAMUPDATESREQ = _descriptor.Descriptor(
  name='StreamUpdatesReq',
  full_name='mediaplayer.StreamUpdatesReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=100,
)


_UPDATE = _descriptor.Descriptor(
  name='Update',
  full_name='mediaplayer.Update',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='volume', full_name='mediaplayer.Update.volume', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='muted', full_name='mediaplayer.Update.muted', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=141,
)

DESCRIPTOR.message_types_by_name['SetVolumeReq'] = _SETVOLUMEREQ
DESCRIPTOR.message_types_by_name['SetVolumeRes'] = _SETVOLUMERES
DESCRIPTOR.message_types_by_name['StreamUpdatesReq'] = _STREAMUPDATESREQ
DESCRIPTOR.message_types_by_name['Update'] = _UPDATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetVolumeReq = _reflection.GeneratedProtocolMessageType('SetVolumeReq', (_message.Message,), {
  'DESCRIPTOR' : _SETVOLUMEREQ,
  '__module__' : 'mediaplayer_pb2'
  # @@protoc_insertion_point(class_scope:mediaplayer.SetVolumeReq)
  })
_sym_db.RegisterMessage(SetVolumeReq)

SetVolumeRes = _reflection.GeneratedProtocolMessageType('SetVolumeRes', (_message.Message,), {
  'DESCRIPTOR' : _SETVOLUMERES,
  '__module__' : 'mediaplayer_pb2'
  # @@protoc_insertion_point(class_scope:mediaplayer.SetVolumeRes)
  })
_sym_db.RegisterMessage(SetVolumeRes)

StreamUpdatesReq = _reflection.GeneratedProtocolMessageType('StreamUpdatesReq', (_message.Message,), {
  'DESCRIPTOR' : _STREAMUPDATESREQ,
  '__module__' : 'mediaplayer_pb2'
  # @@protoc_insertion_point(class_scope:mediaplayer.StreamUpdatesReq)
  })
_sym_db.RegisterMessage(StreamUpdatesReq)

Update = _reflection.GeneratedProtocolMessageType('Update', (_message.Message,), {
  'DESCRIPTOR' : _UPDATE,
  '__module__' : 'mediaplayer_pb2'
  # @@protoc_insertion_point(class_scope:mediaplayer.Update)
  })
_sym_db.RegisterMessage(Update)


DESCRIPTOR._options = None

_MEDIAPLAYER = _descriptor.ServiceDescriptor(
  name='MediaPlayer',
  full_name='mediaplayer.MediaPlayer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=144,
  serialized_end=299,
  methods=[
  _descriptor.MethodDescriptor(
    name='SetVolume',
    full_name='mediaplayer.MediaPlayer.SetVolume',
    index=0,
    containing_service=None,
    input_type=_SETVOLUMEREQ,
    output_type=_SETVOLUMERES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamUpdates',
    full_name='mediaplayer.MediaPlayer.StreamUpdates',
    index=1,
    containing_service=None,
    input_type=_STREAMUPDATESREQ,
    output_type=_UPDATE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MEDIAPLAYER)

DESCRIPTOR.services_by_name['MediaPlayer'] = _MEDIAPLAYER

# @@protoc_insertion_point(module_scope)
