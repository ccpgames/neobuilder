# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sandbox/test/delta.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sandbox.test import beta_pb2 as sandbox_dot_test_dot_beta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18sandbox/test/delta.proto\x12\x0csandbox.test\x1a\x17sandbox/test/beta.proto\"o\n\x0c\x44\x65ltaMessage\x12\x11\n\tmy_string\x18\x01 \x01(\t\x12\x11\n\tmy_number\x18\x02 \x01(\x05\x12\x39\n\x16my_level_three_message\x18\x03 \x01(\x0b\x32\x19.sandbox.test.BetaMessageb\x06proto3')



_DELTAMESSAGE = DESCRIPTOR.message_types_by_name['DeltaMessage']
DeltaMessage = _reflection.GeneratedProtocolMessageType('DeltaMessage', (_message.Message,), {
  'DESCRIPTOR' : _DELTAMESSAGE,
  '__module__' : 'sandbox.test.delta_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.DeltaMessage)
  })
_sym_db.RegisterMessage(DeltaMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DELTAMESSAGE._serialized_start=67
  _DELTAMESSAGE._serialized_end=178
# @@protoc_insertion_point(module_scope)
