# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openscenario_msgs/boundingbox.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#openscenario_msgs/boundingbox.proto\x12\x0copenscenario\"a\n\x0b\x42oundingBox\x12$\n\x06\x63\x65nter\x18\x01 \x02(\x0b\x32\x14.openscenario.Center\x12,\n\ndimensions\x18\x02 \x02(\x0b\x32\x18.openscenario.Dimensions\")\n\x06\x43\x65nter\x12\t\n\x01x\x18\x01 \x02(\x01\x12\t\n\x01y\x18\x02 \x02(\x01\x12\t\n\x01z\x18\x03 \x02(\x01\";\n\nDimensions\x12\x0e\n\x06height\x18\x01 \x02(\x01\x12\x0e\n\x06length\x18\x02 \x02(\x01\x12\r\n\x05width\x18\x03 \x02(\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'openscenario_msgs.boundingbox_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOUNDINGBOX._serialized_start=53
  _BOUNDINGBOX._serialized_end=150
  _CENTER._serialized_start=152
  _CENTER._serialized_end=193
  _DIMENSIONS._serialized_start=195
  _DIMENSIONS._serialized_end=254
# @@protoc_insertion_point(module_scope)
