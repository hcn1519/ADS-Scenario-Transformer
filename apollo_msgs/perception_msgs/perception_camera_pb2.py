# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apollo_msgs/perception_msgs/perception_camera.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_msgs.basic_msgs import geometry_pb2 as apollo__msgs_dot_basic__msgs_dot_geometry__pb2
from apollo_msgs.basic_msgs import header_pb2 as apollo__msgs_dot_basic__msgs_dot_header__pb2
from apollo_msgs.perception_msgs import perception_obstacle_pb2 as apollo__msgs_dot_perception__msgs_dot_perception__obstacle__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3apollo_msgs/perception_msgs/perception_camera.proto\x12\x18\x61pollo.perception.camera\x1a%apollo_msgs/basic_msgs/geometry.proto\x1a#apollo_msgs/basic_msgs/header.proto\x1a\x35\x61pollo_msgs/perception_msgs/perception_obstacle.proto\"n\n\x12LaneLineCubicCurve\x12\x15\n\rlongitude_min\x18\x01 \x01(\x02\x12\x15\n\rlongitude_max\x18\x02 \x01(\x02\x12\t\n\x01\x61\x18\x03 \x01(\x02\x12\t\n\x01\x62\x18\x04 \x01(\x02\x12\t\n\x01\x63\x18\x05 \x01(\x02\x12\t\n\x01\x64\x18\x06 \x01(\x02\"W\n\tEndPoints\x12%\n\x05start\x18\x01 \x01(\x0b\x32\x16.apollo.common.Point2D\x12#\n\x03\x65nd\x18\x02 \x01(\x0b\x32\x16.apollo.common.Point2D\"\xaf\x04\n\x0e\x43\x61meraLaneLine\x12\x34\n\x04type\x18\x01 \x01(\x0e\x32&.apollo.perception.camera.LaneLineType\x12@\n\x08pos_type\x18\x02 \x01(\x0e\x32..apollo.perception.camera.LaneLinePositionType\x12H\n\x12\x63urve_camera_coord\x18\x03 \x01(\x0b\x32,.apollo.perception.camera.LaneLineCubicCurve\x12G\n\x11\x63urve_image_coord\x18\x04 \x01(\x0b\x32,.apollo.perception.camera.LaneLineCubicCurve\x12\x36\n\x16\x63urve_camera_point_set\x18\x05 \x03(\x0b\x32\x16.apollo.common.Point3D\x12\x35\n\x15\x63urve_image_point_set\x18\x06 \x03(\x0b\x32\x16.apollo.common.Point2D\x12@\n\x13image_end_point_set\x18\x07 \x03(\x0b\x32#.apollo.perception.camera.EndPoints\x12\x10\n\x08track_id\x18\x08 \x01(\x05\x12\x12\n\nconfidence\x18\t \x01(\x02\x12;\n\x08use_type\x18\n \x01(\x0e\x32).apollo.perception.camera.LaneLineUseType\">\n\x10\x43\x61meraCalibrator\x12\x13\n\x0bpitch_angle\x18\x01 \x01(\x02\x12\x15\n\rcamera_height\x18\x02 \x01(\x02\"\xad\x03\n\x0e\x43\x61meraObstacle\x12\x37\n\x08obstacle\x18\x01 \x01(\x0b\x32%.apollo.perception.PerceptionObstacle\x12\x41\n\x04type\x18\x15 \x01(\x0e\x32\x33.apollo.perception.camera.CameraObstacle.CameraType\x12\x12\n\ntype_probs\x18\x16 \x03(\x02\x12*\n\nupper_left\x18\x17 \x01(\x0b\x32\x16.apollo.common.Point2D\x12+\n\x0blower_right\x18\x18 \x01(\x0b\x32\x16.apollo.common.Point2D\x12*\n\nkey_points\x18\x19 \x03(\x0b\x32\x16.apollo.common.Point2D\x12\x15\n\rdebug_message\x18\x1a \x03(\t\"o\n\nCameraType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x13\n\x0fUNKNOWN_MOVABLE\x10\x01\x12\x15\n\x11UNKNOWN_UNMOVABLE\x10\x02\x12\x0e\n\nPEDESTRIAN\x10\x03\x12\x0b\n\x07\x42ICYCLE\x10\x04\x12\x0b\n\x07VEHICLE\x10\x05\"\xe2\x02\n\x0b\x43\x61meraDebug\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x14\n\x0csource_topic\x18\x02 \x01(\t\x12I\n\nerror_code\x18\x03 \x01(\x0e\x32).apollo.perception.camera.CameraErrorCode:\nERROR_NONE\x12\x45\n\x11\x63\x61mera_calibrator\x18\x04 \x01(\x0b\x32*.apollo.perception.camera.CameraCalibrator\x12\x41\n\x0f\x63\x61mera_laneline\x18\x05 \x03(\x0b\x32(.apollo.perception.camera.CameraLaneLine\x12\x41\n\x0f\x63\x61mera_obstacle\x18\x06 \x03(\x0b\x32(.apollo.perception.camera.CameraObstacle*4\n\x0f\x43\x61meraErrorCode\x12\x0e\n\nERROR_NONE\x10\x00\x12\x11\n\rERROR_UNKNOWN\x10\x01*V\n\x0cLaneLineType\x12\x10\n\x0cWHITE_DASHED\x10\x00\x12\x0f\n\x0bWHITE_SOLID\x10\x01\x12\x11\n\rYELLOW_DASHED\x10\x02\x12\x10\n\x0cYELLOW_SOLID\x10\x03*\x88\x02\n\x14LaneLinePositionType\x12\x19\n\x0c\x42OLLARD_LEFT\x10\xfb\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x18\n\x0b\x46OURTH_LEFT\x10\xfc\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x17\n\nTHIRD_LEFT\x10\xfd\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1a\n\rADJACENT_LEFT\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x15\n\x08\x45GO_LEFT\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\r\n\tEGO_RIGHT\x10\x01\x12\x12\n\x0e\x41\x44JACENT_RIGHT\x10\x02\x12\x0f\n\x0bTHIRD_RIGHT\x10\x03\x12\x10\n\x0c\x46OURTH_RIGHT\x10\x04\x12\x11\n\rBOLLARD_RIGHT\x10\x05\x12\t\n\x05OTHER\x10\x06\x12\x0b\n\x07UNKNOWN\x10\x07*(\n\x0fLaneLineUseType\x12\x08\n\x04REAL\x10\x00\x12\x0b\n\x07VIRTUAL\x10\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'apollo_msgs.perception_msgs.perception_camera_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_CAMERAERRORCODE']._serialized_start=1828
  _globals['_CAMERAERRORCODE']._serialized_end=1880
  _globals['_LANELINETYPE']._serialized_start=1882
  _globals['_LANELINETYPE']._serialized_end=1968
  _globals['_LANELINEPOSITIONTYPE']._serialized_start=1971
  _globals['_LANELINEPOSITIONTYPE']._serialized_end=2235
  _globals['_LANELINEUSETYPE']._serialized_start=2237
  _globals['_LANELINEUSETYPE']._serialized_end=2277
  _globals['_LANELINECUBICCURVE']._serialized_start=212
  _globals['_LANELINECUBICCURVE']._serialized_end=322
  _globals['_ENDPOINTS']._serialized_start=324
  _globals['_ENDPOINTS']._serialized_end=411
  _globals['_CAMERALANELINE']._serialized_start=414
  _globals['_CAMERALANELINE']._serialized_end=973
  _globals['_CAMERACALIBRATOR']._serialized_start=975
  _globals['_CAMERACALIBRATOR']._serialized_end=1037
  _globals['_CAMERAOBSTACLE']._serialized_start=1040
  _globals['_CAMERAOBSTACLE']._serialized_end=1469
  _globals['_CAMERAOBSTACLE_CAMERATYPE']._serialized_start=1358
  _globals['_CAMERAOBSTACLE_CAMERATYPE']._serialized_end=1469
  _globals['_CAMERADEBUG']._serialized_start=1472
  _globals['_CAMERADEBUG']._serialized_end=1826
# @@protoc_insertion_point(module_scope)
