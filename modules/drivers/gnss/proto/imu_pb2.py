# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/drivers/gnss/proto/imu.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/drivers/gnss/proto/imu.proto',
  package='apollo.drivers.gnss',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n$modules/drivers/gnss/proto/imu.proto\x12\x13\x61pollo.drivers.gnss\x1a!modules/common/proto/header.proto\x1a#modules/common/proto/geometry.proto\"\xca\x01\n\x03Imu\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x18\n\x10measurement_time\x18\x02 \x01(\x01\x12\x1b\n\x10measurement_span\x18\x03 \x01(\x02:\x01\x30\x12\x33\n\x13linear_acceleration\x18\x04 \x01(\x0b\x32\x16.apollo.common.Point3D\x12\x30\n\x10\x61ngular_velocity\x18\x05 \x01(\x0b\x32\x16.apollo.common.Point3D')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,modules_dot_common_dot_proto_dot_geometry__pb2.DESCRIPTOR,])




_IMU = _descriptor.Descriptor(
  name='Imu',
  full_name='apollo.drivers.gnss.Imu',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.drivers.gnss.Imu.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='measurement_time', full_name='apollo.drivers.gnss.Imu.measurement_time', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='measurement_span', full_name='apollo.drivers.gnss.Imu.measurement_span', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linear_acceleration', full_name='apollo.drivers.gnss.Imu.linear_acceleration', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular_velocity', full_name='apollo.drivers.gnss.Imu.angular_velocity', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=134,
  serialized_end=336,
)

_IMU.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_IMU.fields_by_name['linear_acceleration'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
_IMU.fields_by_name['angular_velocity'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
DESCRIPTOR.message_types_by_name['Imu'] = _IMU
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Imu = _reflection.GeneratedProtocolMessageType('Imu', (_message.Message,), dict(
  DESCRIPTOR = _IMU,
  __module__ = 'modules.drivers.gnss.proto.imu_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.gnss.Imu)
  ))
_sym_db.RegisterMessage(Imu)


# @@protoc_insertion_point(module_scope)
