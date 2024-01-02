# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openscenario_msgs/position.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from openscenario_msgs import orientation_pb2 as openscenario__msgs_dot_orientation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n openscenario_msgs/position.proto\x12\x0copenscenairo\x1a#openscenario_msgs/orientation.proto\"\xe0\x04\n\x08Position\x12\x33\n\x0eworld_position\x18\x01 \x01(\x0b\x32\x1b.openscenairo.WorldPosition\x12\x44\n\x17relative_world_position\x18\x02 \x01(\x0b\x32#.openscenairo.RelativeWorldPosition\x12\x46\n\x18relative_object_position\x18\x03 \x01(\x0b\x32$.openscenairo.RelativeObjectPosition\x12\x31\n\rroad_position\x18\x04 \x01(\x0b\x32\x1a.openscenairo.RoadPosition\x12\x42\n\x16relative_road_position\x18\x05 \x01(\x0b\x32\".openscenairo.RelativeRoadPosition\x12\x31\n\rlane_position\x18\x06 \x01(\x0b\x32\x1a.openscenairo.LanePosition\x12\x42\n\x16relative_lane_position\x18\x07 \x01(\x0b\x32\".openscenairo.RelativeLanePosition\x12\x33\n\x0eroute_position\x18\x08 \x01(\x0b\x32\x1b.openscenairo.RoutePosition\x12/\n\x0cgeo_position\x18\t \x01(\x0b\x32\x19.openscenairo.GeoPosition\x12=\n\x13trajectory_position\x18\n \x01(\x0b\x32 .openscenairo.TrajectoryPosition\"Q\n\rWorldPosition\x12\t\n\x01h\x18\x01 \x01(\x01\x12\t\n\x01p\x18\x02 \x01(\x01\x12\t\n\x01r\x18\x03 \x01(\x01\x12\t\n\x01x\x18\x04 \x02(\x01\x12\t\n\x01y\x18\x05 \x02(\x01\x12\t\n\x01z\x18\x06 \x01(\x01\"{\n\x0cLanePosition\x12\x0f\n\x07lane_id\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x01\x12\x0f\n\x07road_id\x18\x03 \x02(\t\x12\t\n\x01s\x18\x04 \x02(\x01\x12.\n\x0borientation\x18\x05 \x01(\x0b\x32\x19.openscenairo.Orientation\"\x17\n\x15RelativeWorldPosition\"\r\n\x0bGeoPosition\"\x18\n\x16RelativeObjectPosition\"\x16\n\x14RelativeLanePosition\"\x0f\n\rRoutePosition\"\x0e\n\x0cRoadPosition\"\x16\n\x14RelativeRoadPosition\"\x14\n\x12TrajectoryPosition')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'openscenario_msgs.position_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_POSITION']._serialized_start=88
  _globals['_POSITION']._serialized_end=696
  _globals['_WORLDPOSITION']._serialized_start=698
  _globals['_WORLDPOSITION']._serialized_end=779
  _globals['_LANEPOSITION']._serialized_start=781
  _globals['_LANEPOSITION']._serialized_end=904
  _globals['_RELATIVEWORLDPOSITION']._serialized_start=906
  _globals['_RELATIVEWORLDPOSITION']._serialized_end=929
  _globals['_GEOPOSITION']._serialized_start=931
  _globals['_GEOPOSITION']._serialized_end=944
  _globals['_RELATIVEOBJECTPOSITION']._serialized_start=946
  _globals['_RELATIVEOBJECTPOSITION']._serialized_end=970
  _globals['_RELATIVELANEPOSITION']._serialized_start=972
  _globals['_RELATIVELANEPOSITION']._serialized_end=994
  _globals['_ROUTEPOSITION']._serialized_start=996
  _globals['_ROUTEPOSITION']._serialized_end=1011
  _globals['_ROADPOSITION']._serialized_start=1013
  _globals['_ROADPOSITION']._serialized_end=1027
  _globals['_RELATIVEROADPOSITION']._serialized_start=1029
  _globals['_RELATIVEROADPOSITION']._serialized_end=1051
  _globals['_TRAJECTORYPOSITION']._serialized_start=1053
  _globals['_TRAJECTORYPOSITION']._serialized_end=1073
# @@protoc_insertion_point(module_scope)