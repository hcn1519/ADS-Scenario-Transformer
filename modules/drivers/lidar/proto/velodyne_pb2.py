# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/drivers/lidar/proto/velodyne.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/drivers/lidar/proto/velodyne.proto',
  package='apollo.drivers.velodyne',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n*modules/drivers/lidar/proto/velodyne.proto\x12\x17\x61pollo.drivers.velodyne\x1a!modules/common/proto/header.proto\"-\n\x0eVelodynePacket\x12\r\n\x05stamp\x18\x01 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\xb3\x02\n\x0cVelodyneScan\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12-\n\x05model\x18\x02 \x01(\x0e\x32\x1e.apollo.drivers.velodyne.Model\x12+\n\x04mode\x18\x03 \x01(\x0e\x32\x1d.apollo.drivers.velodyne.Mode\x12<\n\x0b\x66iring_pkts\x18\x04 \x03(\x0b\x32\'.apollo.drivers.velodyne.VelodynePacket\x12\x41\n\x10positioning_pkts\x18\x05 \x03(\x0b\x32\'.apollo.drivers.velodyne.VelodynePacket\x12\n\n\x02sn\x18\x06 \x01(\t\x12\x13\n\x08\x62\x61setime\x18\x07 \x01(\x04:\x01\x30*r\n\x05Model\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nHDL64E_S3S\x10\x01\x12\x0e\n\nHDL64E_S3D\x10\x02\x12\r\n\tHDL64E_S2\x10\x03\x12\n\n\x06HDL32E\x10\x04\x12\t\n\x05VLP16\x10\x05\x12\n\n\x06VLP32C\x10\x06\x12\n\n\x06VLS128\x10\x07*)\n\x04Mode\x12\r\n\tSTRONGEST\x10\x01\x12\x08\n\x04LAST\x10\x02\x12\x08\n\x04\x44UAL\x10\x03')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,])

_MODEL = _descriptor.EnumDescriptor(
  name='Model',
  full_name='apollo.drivers.velodyne.Model',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HDL64E_S3S', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HDL64E_S3D', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HDL64E_S2', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HDL32E', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VLP16', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VLP32C', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VLS128', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=463,
  serialized_end=577,
)
_sym_db.RegisterEnumDescriptor(_MODEL)

Model = enum_type_wrapper.EnumTypeWrapper(_MODEL)
_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='apollo.drivers.velodyne.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STRONGEST', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAST', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUAL', index=2, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=579,
  serialized_end=620,
)
_sym_db.RegisterEnumDescriptor(_MODE)

Mode = enum_type_wrapper.EnumTypeWrapper(_MODE)
UNKNOWN = 0
HDL64E_S3S = 1
HDL64E_S3D = 2
HDL64E_S2 = 3
HDL32E = 4
VLP16 = 5
VLP32C = 6
VLS128 = 7
STRONGEST = 1
LAST = 2
DUAL = 3



_VELODYNEPACKET = _descriptor.Descriptor(
  name='VelodynePacket',
  full_name='apollo.drivers.velodyne.VelodynePacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stamp', full_name='apollo.drivers.velodyne.VelodynePacket.stamp', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='apollo.drivers.velodyne.VelodynePacket.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=151,
)


_VELODYNESCAN = _descriptor.Descriptor(
  name='VelodyneScan',
  full_name='apollo.drivers.velodyne.VelodyneScan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.drivers.velodyne.VelodyneScan.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='apollo.drivers.velodyne.VelodyneScan.model', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='apollo.drivers.velodyne.VelodyneScan.mode', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='firing_pkts', full_name='apollo.drivers.velodyne.VelodyneScan.firing_pkts', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='positioning_pkts', full_name='apollo.drivers.velodyne.VelodyneScan.positioning_pkts', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sn', full_name='apollo.drivers.velodyne.VelodyneScan.sn', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='basetime', full_name='apollo.drivers.velodyne.VelodyneScan.basetime', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=461,
)

_VELODYNESCAN.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_VELODYNESCAN.fields_by_name['model'].enum_type = _MODEL
_VELODYNESCAN.fields_by_name['mode'].enum_type = _MODE
_VELODYNESCAN.fields_by_name['firing_pkts'].message_type = _VELODYNEPACKET
_VELODYNESCAN.fields_by_name['positioning_pkts'].message_type = _VELODYNEPACKET
DESCRIPTOR.message_types_by_name['VelodynePacket'] = _VELODYNEPACKET
DESCRIPTOR.message_types_by_name['VelodyneScan'] = _VELODYNESCAN
DESCRIPTOR.enum_types_by_name['Model'] = _MODEL
DESCRIPTOR.enum_types_by_name['Mode'] = _MODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VelodynePacket = _reflection.GeneratedProtocolMessageType('VelodynePacket', (_message.Message,), dict(
  DESCRIPTOR = _VELODYNEPACKET,
  __module__ = 'modules.drivers.lidar.proto.velodyne_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.velodyne.VelodynePacket)
  ))
_sym_db.RegisterMessage(VelodynePacket)

VelodyneScan = _reflection.GeneratedProtocolMessageType('VelodyneScan', (_message.Message,), dict(
  DESCRIPTOR = _VELODYNESCAN,
  __module__ = 'modules.drivers.lidar.proto.velodyne_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.velodyne.VelodyneScan)
  ))
_sym_db.RegisterMessage(VelodyneScan)


# @@protoc_insertion_point(module_scope)
