# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apollo_msgs/localization_msgs/imu.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_msgs.basic_msgs import header_pb2 as apollo__msgs_dot_basic__msgs_dot_header__pb2
from apollo_msgs.localization_msgs import pose_pb2 as apollo__msgs_dot_localization__msgs_dot_pose__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'apollo_msgs/localization_msgs/imu.proto\x12\x13\x61pollo.localization\x1a#apollo_msgs/basic_msgs/header.proto\x1a(apollo_msgs/localization_msgs/pose.proto\"]\n\x0c\x43orrectedImu\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12&\n\x03imu\x18\x03 \x01(\x0b\x32\x19.apollo.localization.Pose')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'apollo_msgs.localization_msgs.imu_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CORRECTEDIMU._serialized_start=143
  _CORRECTEDIMU._serialized_end=236
# @@protoc_insertion_point(module_scope)
