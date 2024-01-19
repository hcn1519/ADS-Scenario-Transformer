# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apollo_msgs/basic_msgs/error_code.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'apollo_msgs/basic_msgs/error_code.proto\x12\rapollo.common\"I\n\x08StatusPb\x12\x30\n\nerror_code\x18\x01 \x01(\x0e\x32\x18.apollo.common.ErrorCode:\x02OK\x12\x0b\n\x03msg\x18\x02 \x01(\t*\x99\x08\n\tErrorCode\x12\x06\n\x02OK\x10\x00\x12\x12\n\rCONTROL_ERROR\x10\xe8\x07\x12\x17\n\x12\x43ONTROL_INIT_ERROR\x10\xe9\x07\x12\x1a\n\x15\x43ONTROL_COMPUTE_ERROR\x10\xea\x07\x12\x18\n\x13\x43ONTROL_ESTOP_ERROR\x10\xeb\x07\x12\x1a\n\x15PERFECT_CONTROL_ERROR\x10\xec\x07\x12\x11\n\x0c\x43\x41NBUS_ERROR\x10\xd0\x0f\x12\x1a\n\x15\x43\x41N_CLIENT_ERROR_BASE\x10\xb4\x10\x12(\n#CAN_CLIENT_ERROR_OPEN_DEVICE_FAILED\x10\xb5\x10\x12\x1f\n\x1a\x43\x41N_CLIENT_ERROR_FRAME_NUM\x10\xb6\x10\x12!\n\x1c\x43\x41N_CLIENT_ERROR_SEND_FAILED\x10\xb7\x10\x12!\n\x1c\x43\x41N_CLIENT_ERROR_RECV_FAILED\x10\xb8\x10\x12\x17\n\x12LOCALIZATION_ERROR\x10\xb8\x17\x12\x1b\n\x16LOCALIZATION_ERROR_MSG\x10\x9c\x18\x12\x1d\n\x18LOCALIZATION_ERROR_LIDAR\x10\x80\x19\x12\x1d\n\x18LOCALIZATION_ERROR_INTEG\x10\xe4\x19\x12\x1c\n\x17LOCALIZATION_ERROR_GNSS\x10\xc8\x1a\x12\x15\n\x10PERCEPTION_ERROR\x10\xa0\x1f\x12\x18\n\x13PERCEPTION_ERROR_TF\x10\xa1\x1f\x12\x1d\n\x18PERCEPTION_ERROR_PROCESS\x10\xa2\x1f\x12\x15\n\x10PERCEPTION_FATAL\x10\xa3\x1f\x12\x1a\n\x15PERCEPTION_ERROR_NONE\x10\xa4\x1f\x12\x1d\n\x18PERCEPTION_ERROR_UNKNOWN\x10\xa5\x1f\x12\x15\n\x10PREDICTION_ERROR\x10\x88\'\x12\x13\n\x0ePLANNING_ERROR\x10\xf0.\x12\x1d\n\x18PLANNING_ERROR_NOT_READY\x10\xf1.\x12\x15\n\x10HDMAP_DATA_ERROR\x10\xd8\x36\x12\x12\n\rROUTING_ERROR\x10\xc0>\x12\x1a\n\x15ROUTING_ERROR_REQUEST\x10\xc1>\x12\x1b\n\x16ROUTING_ERROR_RESPONSE\x10\xc2>\x12\x1c\n\x17ROUTING_ERROR_NOT_READY\x10\xc3>\x12\x11\n\x0c\x45ND_OF_INPUT\x10\xa8\x46\x12\x15\n\x10HTTP_LOGIC_ERROR\x10\x90N\x12\x17\n\x12HTTP_RUNTIME_ERROR\x10\x91N\x12\x17\n\x12RELATIVE_MAP_ERROR\x10\xf8U\x12\x1b\n\x16RELATIVE_MAP_NOT_READY\x10\xf9U\x12\x16\n\x11\x44RIVER_ERROR_GNSS\x10\xe0]\x12\x1a\n\x15\x44RIVER_ERROR_VELODYNE\x10\xc8\x65\x12\x17\n\x12STORYTELLING_ERROR\x10\xb0m')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'apollo_msgs.basic_msgs.error_code_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ERRORCODE']._serialized_start=134
  _globals['_ERRORCODE']._serialized_end=1183
  _globals['_STATUSPB']._serialized_start=58
  _globals['_STATUSPB']._serialized_end=131
# @@protoc_insertion_point(module_scope)
