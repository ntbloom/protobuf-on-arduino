# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: raincounter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='raincounter.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11raincounter.proto\"f\n\nDataPacket\x12*\n\npacketType\x18\x01 \x01(\x0e\x32\x16.DataPacket.PacketType\x12\r\n\x05value\x18\x02 \x01(\x05\"\x1d\n\nPacketType\x12\x0f\n\x0bTEMPERATURE\x10\x00\"\x9b\x01\n\x0b\x45ventPacket\x12+\n\npacketType\x18\x01 \x01(\x0e\x32\x17.EventPacket.PacketType\"_\n\nPacketType\x12\x10\n\x0cTIPPER_CLICK\x10\x00\x12\x0e\n\nSOFT_RESET\x10\x01\x12\x0e\n\nHARD_RESET\x10\x02\x12\x0f\n\x0bSTART_PAUSE\x10\x03\x12\x0e\n\nSTOP_PAUSE\x10\x04\x62\x06proto3'
)



_DATAPACKET_PACKETTYPE = _descriptor.EnumDescriptor(
  name='PacketType',
  full_name='DataPacket.PacketType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TEMPERATURE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=94,
  serialized_end=123,
)
_sym_db.RegisterEnumDescriptor(_DATAPACKET_PACKETTYPE)

_EVENTPACKET_PACKETTYPE = _descriptor.EnumDescriptor(
  name='PacketType',
  full_name='EventPacket.PacketType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TIPPER_CLICK', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SOFT_RESET', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HARD_RESET', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='START_PAUSE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STOP_PAUSE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=186,
  serialized_end=281,
)
_sym_db.RegisterEnumDescriptor(_EVENTPACKET_PACKETTYPE)


_DATAPACKET = _descriptor.Descriptor(
  name='DataPacket',
  full_name='DataPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='packetType', full_name='DataPacket.packetType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='DataPacket.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DATAPACKET_PACKETTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=123,
)


_EVENTPACKET = _descriptor.Descriptor(
  name='EventPacket',
  full_name='EventPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='packetType', full_name='EventPacket.packetType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EVENTPACKET_PACKETTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=281,
)

_DATAPACKET.fields_by_name['packetType'].enum_type = _DATAPACKET_PACKETTYPE
_DATAPACKET_PACKETTYPE.containing_type = _DATAPACKET
_EVENTPACKET.fields_by_name['packetType'].enum_type = _EVENTPACKET_PACKETTYPE
_EVENTPACKET_PACKETTYPE.containing_type = _EVENTPACKET
DESCRIPTOR.message_types_by_name['DataPacket'] = _DATAPACKET
DESCRIPTOR.message_types_by_name['EventPacket'] = _EVENTPACKET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataPacket = _reflection.GeneratedProtocolMessageType('DataPacket', (_message.Message,), {
  'DESCRIPTOR' : _DATAPACKET,
  '__module__' : 'raincounter_pb2'
  # @@protoc_insertion_point(class_scope:DataPacket)
  })
_sym_db.RegisterMessage(DataPacket)

EventPacket = _reflection.GeneratedProtocolMessageType('EventPacket', (_message.Message,), {
  'DESCRIPTOR' : _EVENTPACKET,
  '__module__' : 'raincounter_pb2'
  # @@protoc_insertion_point(class_scope:EventPacket)
  })
_sym_db.RegisterMessage(EventPacket)


# @@protoc_insertion_point(module_scope)