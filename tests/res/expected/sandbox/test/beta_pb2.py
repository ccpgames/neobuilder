# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sandbox/test/beta.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sandbox.test import alpha_pb2 as sandbox_dot_test_dot_alpha__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17sandbox/test/beta.proto\x12\x0csandbox.test\x1a\x18sandbox/test/alpha.proto\"k\n\x0b\x42\x65taMessage\x12\x11\n\tmy_string\x18\x01 \x01(\t\x12\x11\n\tmy_number\x18\x02 \x01(\x05\x12\x36\n\x12my_foreign_message\x18\x03 \x01(\x0b\x32\x1a.sandbox.test.AlphaMessageb\x06proto3')



_BETAMESSAGE = DESCRIPTOR.message_types_by_name['BetaMessage']
BetaMessage = _reflection.GeneratedProtocolMessageType('BetaMessage', (_message.Message,), {
  'DESCRIPTOR' : _BETAMESSAGE,
  '__module__' : 'sandbox.test.beta_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.BetaMessage)
  })
_sym_db.RegisterMessage(BetaMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BETAMESSAGE._serialized_start=67
  _BETAMESSAGE._serialized_end=174
# @@protoc_insertion_point(module_scope)
