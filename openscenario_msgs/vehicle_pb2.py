# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openscenario_msgs/vehicle.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from openscenario_msgs import boundingbox_pb2 as openscenario__msgs_dot_boundingbox__pb2
from openscenario_msgs import parameter_pb2 as openscenario__msgs_dot_parameter__pb2
from openscenario_msgs import property_pb2 as openscenario__msgs_dot_property__pb2
from openscenario_msgs import role_pb2 as openscenario__msgs_dot_role__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fopenscenario_msgs/vehicle.proto\x12\x0copenscenario\x1a#openscenario_msgs/boundingbox.proto\x1a!openscenario_msgs/parameter.proto\x1a openscenario_msgs/property.proto\x1a\x1copenscenario_msgs/role.proto\"\x87\x04\n\x07Vehicle\x12\x0c\n\x04mass\x18\x01 \x01(\x01\x12\x0f\n\x07model3d\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x02(\t\x12 \n\x04role\x18\x04 \x01(\x0e\x32\x12.openscenario.Role\x12\x37\n\x0fvehicleCategory\x18\x05 \x02(\x0e\x32\x1e.openscenario.Vehicle.Category\x12\x41\n\x15parameterDeclarations\x18\x06 \x03(\x0b\x32\".openscenario.ParameterDeclaration\x12.\n\x0b\x62oundingBox\x18\x07 \x02(\x0b\x32\x19.openscenario.BoundingBox\x12.\n\x0bperformance\x18\x08 \x02(\x0b\x32\x19.openscenario.Performance\x12\"\n\x05\x61xles\x18\t \x02(\x0b\x32\x13.openscenario.Axles\x12,\n\nproperties\x18\n \x02(\x0b\x32\x18.openscenario.Properties\"\x7f\n\x08\x43\x61tegory\x12\x0b\n\x07\x42ICYCLE\x10\x00\x12\x07\n\x03\x42US\x10\x01\x12\x07\n\x03\x43\x41R\x10\x02\x12\r\n\tMOTORBIKE\x10\x03\x12\x0f\n\x0bSEMITRAILER\x10\x04\x12\x0b\n\x07TRAILER\x10\x05\x12\t\n\x05TRAIN\x10\x06\x12\x08\n\x04TRAM\x10\x07\x12\t\n\x05TRUCK\x10\x08\x12\x07\n\x03VAN\x10\t\"\x8b\x01\n\x0bPerformance\x12\x17\n\x0fmaxAcceleration\x18\x01 \x02(\x01\x12\x1b\n\x13maxAccelerationRate\x18\x02 \x01(\x01\x12\x17\n\x0fmaxDeceleration\x18\x03 \x02(\x01\x12\x1b\n\x13maxDecelerationRate\x18\x04 \x01(\x01\x12\x10\n\x08maxSpeed\x18\x05 \x02(\x01\"\x8a\x01\n\x05\x41xles\x12*\n\tfrontAxle\x18\x01 \x02(\x0b\x32\x17.openscenario.FrontAxle\x12(\n\x08rearAxle\x18\x02 \x02(\x0b\x32\x16.openscenario.RearAxle\x12+\n\x0f\x61\x64\x64itionalAxles\x18\x03 \x03(\x0b\x32\x12.openscenario.Axle\"q\n\tFrontAxle\x12\x13\n\x0bmaxSteering\x18\x01 \x02(\x01\x12\x11\n\tpositionX\x18\x02 \x02(\x01\x12\x11\n\tpositionZ\x18\x03 \x02(\x01\x12\x12\n\ntrackWidth\x18\x04 \x02(\x01\x12\x15\n\rwheelDiameter\x18\x05 \x02(\x01\"p\n\x08RearAxle\x12\x13\n\x0bmaxSteering\x18\x01 \x02(\x01\x12\x11\n\tpositionX\x18\x02 \x02(\x01\x12\x11\n\tpositionZ\x18\x03 \x02(\x01\x12\x12\n\ntrackWidth\x18\x04 \x02(\x01\x12\x15\n\rwheelDiameter\x18\x05 \x02(\x01\"l\n\x04\x41xle\x12\x13\n\x0bmaxSteering\x18\x01 \x02(\x01\x12\x11\n\tpositionX\x18\x02 \x02(\x01\x12\x11\n\tpositionZ\x18\x03 \x02(\x01\x12\x12\n\ntrackWidth\x18\x04 \x02(\x01\x12\x15\n\rwheelDiameter\x18\x05 \x02(\x01')



_VEHICLE = DESCRIPTOR.message_types_by_name['Vehicle']
_PERFORMANCE = DESCRIPTOR.message_types_by_name['Performance']
_AXLES = DESCRIPTOR.message_types_by_name['Axles']
_FRONTAXLE = DESCRIPTOR.message_types_by_name['FrontAxle']
_REARAXLE = DESCRIPTOR.message_types_by_name['RearAxle']
_AXLE = DESCRIPTOR.message_types_by_name['Axle']
_VEHICLE_CATEGORY = _VEHICLE.enum_types_by_name['Category']
Vehicle = _reflection.GeneratedProtocolMessageType('Vehicle', (_message.Message,), {
  'DESCRIPTOR' : _VEHICLE,
  '__module__' : 'openscenario_msgs.vehicle_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.Vehicle)
  })
_sym_db.RegisterMessage(Vehicle)

Performance = _reflection.GeneratedProtocolMessageType('Performance', (_message.Message,), {
  'DESCRIPTOR' : _PERFORMANCE,
  '__module__' : 'openscenario_msgs.vehicle_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.Performance)
  })
_sym_db.RegisterMessage(Performance)

Axles = _reflection.GeneratedProtocolMessageType('Axles', (_message.Message,), {
  'DESCRIPTOR' : _AXLES,
  '__module__' : 'openscenario_msgs.vehicle_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.Axles)
  })
_sym_db.RegisterMessage(Axles)

FrontAxle = _reflection.GeneratedProtocolMessageType('FrontAxle', (_message.Message,), {
  'DESCRIPTOR' : _FRONTAXLE,
  '__module__' : 'openscenario_msgs.vehicle_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.FrontAxle)
  })
_sym_db.RegisterMessage(FrontAxle)

RearAxle = _reflection.GeneratedProtocolMessageType('RearAxle', (_message.Message,), {
  'DESCRIPTOR' : _REARAXLE,
  '__module__' : 'openscenario_msgs.vehicle_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.RearAxle)
  })
_sym_db.RegisterMessage(RearAxle)

Axle = _reflection.GeneratedProtocolMessageType('Axle', (_message.Message,), {
  'DESCRIPTOR' : _AXLE,
  '__module__' : 'openscenario_msgs.vehicle_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.Axle)
  })
_sym_db.RegisterMessage(Axle)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VEHICLE._serialized_start=186
  _VEHICLE._serialized_end=705
  _VEHICLE_CATEGORY._serialized_start=578
  _VEHICLE_CATEGORY._serialized_end=705
  _PERFORMANCE._serialized_start=708
  _PERFORMANCE._serialized_end=847
  _AXLES._serialized_start=850
  _AXLES._serialized_end=988
  _FRONTAXLE._serialized_start=990
  _FRONTAXLE._serialized_end=1103
  _REARAXLE._serialized_start=1105
  _REARAXLE._serialized_end=1217
  _AXLE._serialized_start=1219
  _AXLE._serialized_end=1327
# @@protoc_insertion_point(module_scope)
