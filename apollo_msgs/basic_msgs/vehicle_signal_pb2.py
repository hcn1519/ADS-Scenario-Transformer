# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apollo_msgs/basic_msgs/vehicle_signal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+apollo_msgs/basic_msgs/vehicle_signal.proto\x12\rapollo.common\"\xee\x01\n\rVehicleSignal\x12<\n\x0bturn_signal\x18\x01 \x01(\x0e\x32\'.apollo.common.VehicleSignal.TurnSignal\x12\x11\n\thigh_beam\x18\x02 \x01(\x08\x12\x10\n\x08low_beam\x18\x03 \x01(\x08\x12\x0c\n\x04horn\x18\x04 \x01(\x08\x12\x17\n\x0f\x65mergency_light\x18\x05 \x01(\x08\"S\n\nTurnSignal\x12\r\n\tTURN_NONE\x10\x00\x12\r\n\tTURN_LEFT\x10\x01\x12\x0e\n\nTURN_RIGHT\x10\x02\x12\x17\n\x13TURN_HAZARD_WARNING\x10\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'apollo_msgs.basic_msgs.vehicle_signal_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_VEHICLESIGNAL']._serialized_start=63
  _globals['_VEHICLESIGNAL']._serialized_end=301
  _globals['_VEHICLESIGNAL_TURNSIGNAL']._serialized_start=218
  _globals['_VEHICLESIGNAL_TURNSIGNAL']._serialized_end=301
# @@protoc_insertion_point(module_scope)
