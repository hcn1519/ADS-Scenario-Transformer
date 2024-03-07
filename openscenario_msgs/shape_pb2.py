# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openscenario_msgs/shape.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from openscenario_msgs import position_pb2 as openscenario__msgs_dot_position__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dopenscenario_msgs/shape.proto\x12\x0copenscenario\x1a openscenario_msgs/position.proto\"\x7f\n\x05Shape\x12(\n\x08polyline\x18\x01 \x01(\x0b\x32\x16.openscenario.Polyline\x12(\n\x08\x63lothoid\x18\x02 \x01(\x0b\x32\x16.openscenario.Clothoid\x12\"\n\x05nurbs\x18\x03 \x01(\x0b\x32\x13.openscenario.Nurbs\"2\n\x08Polyline\x12&\n\x08vertices\x18\x01 \x03(\x0b\x32\x14.openscenario.Vertex\"@\n\x06Vertex\x12\x0c\n\x04time\x18\x01 \x01(\x01\x12(\n\x08position\x18\x02 \x02(\x0b\x32\x16.openscenario.Position\"\n\n\x08\x43lothoid\"\x07\n\x05Nurbs\"V\n\x0c\x43ontrolPoint\x12\x0c\n\x04time\x18\x01 \x01(\x01\x12\x0e\n\x06weight\x18\x02 \x01(\x01\x12(\n\x08position\x18\x03 \x02(\x0b\x32\x16.openscenario.Position')



_SHAPE = DESCRIPTOR.message_types_by_name['Shape']
_POLYLINE = DESCRIPTOR.message_types_by_name['Polyline']
_VERTEX = DESCRIPTOR.message_types_by_name['Vertex']
_CLOTHOID = DESCRIPTOR.message_types_by_name['Clothoid']
_NURBS = DESCRIPTOR.message_types_by_name['Nurbs']
_CONTROLPOINT = DESCRIPTOR.message_types_by_name['ControlPoint']
Shape = _reflection.GeneratedProtocolMessageType('Shape', (_message.Message,), {
  'DESCRIPTOR' : _SHAPE,
  '__module__' : 'openscenario_msgs.shape_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.Shape)
  })
_sym_db.RegisterMessage(Shape)

Polyline = _reflection.GeneratedProtocolMessageType('Polyline', (_message.Message,), {
  'DESCRIPTOR' : _POLYLINE,
  '__module__' : 'openscenario_msgs.shape_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.Polyline)
  })
_sym_db.RegisterMessage(Polyline)

Vertex = _reflection.GeneratedProtocolMessageType('Vertex', (_message.Message,), {
  'DESCRIPTOR' : _VERTEX,
  '__module__' : 'openscenario_msgs.shape_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.Vertex)
  })
_sym_db.RegisterMessage(Vertex)

Clothoid = _reflection.GeneratedProtocolMessageType('Clothoid', (_message.Message,), {
  'DESCRIPTOR' : _CLOTHOID,
  '__module__' : 'openscenario_msgs.shape_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.Clothoid)
  })
_sym_db.RegisterMessage(Clothoid)

Nurbs = _reflection.GeneratedProtocolMessageType('Nurbs', (_message.Message,), {
  'DESCRIPTOR' : _NURBS,
  '__module__' : 'openscenario_msgs.shape_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.Nurbs)
  })
_sym_db.RegisterMessage(Nurbs)

ControlPoint = _reflection.GeneratedProtocolMessageType('ControlPoint', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLPOINT,
  '__module__' : 'openscenario_msgs.shape_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.ControlPoint)
  })
_sym_db.RegisterMessage(ControlPoint)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SHAPE._serialized_start=81
  _SHAPE._serialized_end=208
  _POLYLINE._serialized_start=210
  _POLYLINE._serialized_end=260
  _VERTEX._serialized_start=262
  _VERTEX._serialized_end=326
  _CLOTHOID._serialized_start=328
  _CLOTHOID._serialized_end=338
  _NURBS._serialized_start=340
  _NURBS._serialized_end=347
  _CONTROLPOINT._serialized_start=349
  _CONTROLPOINT._serialized_end=435
# @@protoc_insertion_point(module_scope)
