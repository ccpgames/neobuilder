# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sandbox/test/clones.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19sandbox/test/clones.proto\x12\x0csandbox.test\x1a\x1fgoogle/protobuf/timestamp.proto\"$\n\x08SubThing\x12\x0b\n\x03\x66oo\x18\x01 \x01(\t\x12\x0b\n\x03\x62\x61r\x18\x02 \x01(\t\"\xbb\x01\n\x08ThingOne\x12\x11\n\tmy_string\x18\x01 \x01(\t\x12\x11\n\tmy_number\x18\x02 \x01(\x05\x12\x10\n\x08my_float\x18\x03 \x01(\x02\x12\x30\n\x0cmy_timestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x0bmy_subthing\x18\x05 \x01(\x0b\x32\x16.sandbox.test.SubThing\x12\x18\n\x10my_unique_string\x18\x06 \x01(\t\"\xbc\x01\n\x08ThingTwo\x12\x11\n\tmy_string\x18\x01 \x01(\t\x12\x11\n\tmy_number\x18\x02 \x01(\x05\x12\x10\n\x08my_float\x18\x03 \x01(\x02\x12\x30\n\x0cmy_timestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x0bmy_subthing\x18\x05 \x01(\x0b\x32\x16.sandbox.test.SubThing\x12\x19\n\x11my_special_string\x18\x06 \x01(\tb\x06proto3')



_SUBTHING = DESCRIPTOR.message_types_by_name['SubThing']
_THINGONE = DESCRIPTOR.message_types_by_name['ThingOne']
_THINGTWO = DESCRIPTOR.message_types_by_name['ThingTwo']
SubThing = _reflection.GeneratedProtocolMessageType('SubThing', (_message.Message,), {
  'DESCRIPTOR' : _SUBTHING,
  '__module__' : 'sandbox.test.clones_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.SubThing)
  })
_sym_db.RegisterMessage(SubThing)

ThingOne = _reflection.GeneratedProtocolMessageType('ThingOne', (_message.Message,), {
  'DESCRIPTOR' : _THINGONE,
  '__module__' : 'sandbox.test.clones_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.ThingOne)
  })
_sym_db.RegisterMessage(ThingOne)

ThingTwo = _reflection.GeneratedProtocolMessageType('ThingTwo', (_message.Message,), {
  'DESCRIPTOR' : _THINGTWO,
  '__module__' : 'sandbox.test.clones_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.ThingTwo)
  })
_sym_db.RegisterMessage(ThingTwo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SUBTHING._serialized_start=76
  _SUBTHING._serialized_end=112
  _THINGONE._serialized_start=115
  _THINGONE._serialized_end=302
  _THINGTWO._serialized_start=305
  _THINGTWO._serialized_end=493
# @@protoc_insertion_point(module_scope)
