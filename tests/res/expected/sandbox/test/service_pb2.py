# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sandbox/test/service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1asandbox/test/service.proto\x12\x0csandbox.test\" \n\x0cHelloRequest\x12\x10\n\x08greeting\x18\x01 \x01(\t\"\x1e\n\rHelloResponse\x12\r\n\x05reply\x18\x01 \x01(\t\"5\n\x0fGreetingMessage\x12\x10\n\x08greeting\x18\x01 \x01(\t\x12\x10\n\x08language\x18\x02 \x01(\t\"G\n\x12NestedHelloRequest\x12\x31\n\nmy_message\x18\x01 \x01(\x0b\x32\x1d.sandbox.test.GreetingMessage\"F\n\x13NestedHelloResponse\x12/\n\x08my_reply\x18\x01 \x01(\x0b\x32\x1d.sandbox.test.GreetingMessage\"\x13\n\x11\x45mptyHelloRequest\"\x14\n\x12\x45mptyHelloResponse\"\"\n\nAddRequest\x12\t\n\x01x\x18\x01 \x01(\x03\x12\t\n\x01y\x18\x02 \x01(\x03\"\x1d\n\x0b\x41\x64\x64Response\x12\x0e\n\x06result\x18\x01 \x01(\x03\"\'\n\x0fSubtractRequest\x12\t\n\x01x\x18\x01 \x01(\x03\x12\t\n\x01y\x18\x02 \x01(\x03\"\"\n\x10SubtractResponse\x12\x0e\n\x06result\x18\x01 \x01(\x03\".\n\x16IntegerDivisionRequest\x12\t\n\x01x\x18\x01 \x01(\x03\x12\t\n\x01y\x18\x02 \x01(\x03\"<\n\x17IntegerDivisionResponse\x12\x0e\n\x06result\x18\x01 \x01(\x03\x12\x11\n\tremainder\x18\x02 \x01(\x03\x32\xf6\x01\n\rSimpleService\x12@\n\x05Hello\x12\x1a.sandbox.test.HelloRequest\x1a\x1b.sandbox.test.HelloResponse\x12R\n\x0bNestedHello\x12 .sandbox.test.NestedHelloRequest\x1a!.sandbox.test.NestedHelloResponse\x12O\n\nEmptyHello\x12\x1f.sandbox.test.EmptyHelloRequest\x1a .sandbox.test.EmptyHelloResponse2\xed\x01\n\x04Math\x12:\n\x03\x41\x64\x64\x12\x18.sandbox.test.AddRequest\x1a\x19.sandbox.test.AddResponse\x12I\n\x08Subtract\x12\x1d.sandbox.test.SubtractRequest\x1a\x1e.sandbox.test.SubtractResponse\x12^\n\x0fIntegerDivision\x12$.sandbox.test.IntegerDivisionRequest\x1a%.sandbox.test.IntegerDivisionResponseb\x06proto3')



_HELLOREQUEST = DESCRIPTOR.message_types_by_name['HelloRequest']
_HELLORESPONSE = DESCRIPTOR.message_types_by_name['HelloResponse']
_GREETINGMESSAGE = DESCRIPTOR.message_types_by_name['GreetingMessage']
_NESTEDHELLOREQUEST = DESCRIPTOR.message_types_by_name['NestedHelloRequest']
_NESTEDHELLORESPONSE = DESCRIPTOR.message_types_by_name['NestedHelloResponse']
_EMPTYHELLOREQUEST = DESCRIPTOR.message_types_by_name['EmptyHelloRequest']
_EMPTYHELLORESPONSE = DESCRIPTOR.message_types_by_name['EmptyHelloResponse']
_ADDREQUEST = DESCRIPTOR.message_types_by_name['AddRequest']
_ADDRESPONSE = DESCRIPTOR.message_types_by_name['AddResponse']
_SUBTRACTREQUEST = DESCRIPTOR.message_types_by_name['SubtractRequest']
_SUBTRACTRESPONSE = DESCRIPTOR.message_types_by_name['SubtractResponse']
_INTEGERDIVISIONREQUEST = DESCRIPTOR.message_types_by_name['IntegerDivisionRequest']
_INTEGERDIVISIONRESPONSE = DESCRIPTOR.message_types_by_name['IntegerDivisionResponse']
HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'sandbox.test.service_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

HelloResponse = _reflection.GeneratedProtocolMessageType('HelloResponse', (_message.Message,), {
  'DESCRIPTOR' : _HELLORESPONSE,
  '__module__' : 'sandbox.test.service_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.HelloResponse)
  })
_sym_db.RegisterMessage(HelloResponse)

GreetingMessage = _reflection.GeneratedProtocolMessageType('GreetingMessage', (_message.Message,), {
  'DESCRIPTOR' : _GREETINGMESSAGE,
  '__module__' : 'sandbox.test.service_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.GreetingMessage)
  })
_sym_db.RegisterMessage(GreetingMessage)

NestedHelloRequest = _reflection.GeneratedProtocolMessageType('NestedHelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _NESTEDHELLOREQUEST,
  '__module__' : 'sandbox.test.service_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.NestedHelloRequest)
  })
_sym_db.RegisterMessage(NestedHelloRequest)

NestedHelloResponse = _reflection.GeneratedProtocolMessageType('NestedHelloResponse', (_message.Message,), {
  'DESCRIPTOR' : _NESTEDHELLORESPONSE,
  '__module__' : 'sandbox.test.service_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.NestedHelloResponse)
  })
_sym_db.RegisterMessage(NestedHelloResponse)

EmptyHelloRequest = _reflection.GeneratedProtocolMessageType('EmptyHelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYHELLOREQUEST,
  '__module__' : 'sandbox.test.service_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.EmptyHelloRequest)
  })
_sym_db.RegisterMessage(EmptyHelloRequest)

EmptyHelloResponse = _reflection.GeneratedProtocolMessageType('EmptyHelloResponse', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYHELLORESPONSE,
  '__module__' : 'sandbox.test.service_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.EmptyHelloResponse)
  })
_sym_db.RegisterMessage(EmptyHelloResponse)

AddRequest = _reflection.GeneratedProtocolMessageType('AddRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDREQUEST,
  '__module__' : 'sandbox.test.service_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.AddRequest)
  })
_sym_db.RegisterMessage(AddRequest)

AddResponse = _reflection.GeneratedProtocolMessageType('AddResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESPONSE,
  '__module__' : 'sandbox.test.service_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.AddResponse)
  })
_sym_db.RegisterMessage(AddResponse)

SubtractRequest = _reflection.GeneratedProtocolMessageType('SubtractRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBTRACTREQUEST,
  '__module__' : 'sandbox.test.service_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.SubtractRequest)
  })
_sym_db.RegisterMessage(SubtractRequest)

SubtractResponse = _reflection.GeneratedProtocolMessageType('SubtractResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBTRACTRESPONSE,
  '__module__' : 'sandbox.test.service_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.SubtractResponse)
  })
_sym_db.RegisterMessage(SubtractResponse)

IntegerDivisionRequest = _reflection.GeneratedProtocolMessageType('IntegerDivisionRequest', (_message.Message,), {
  'DESCRIPTOR' : _INTEGERDIVISIONREQUEST,
  '__module__' : 'sandbox.test.service_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.IntegerDivisionRequest)
  })
_sym_db.RegisterMessage(IntegerDivisionRequest)

IntegerDivisionResponse = _reflection.GeneratedProtocolMessageType('IntegerDivisionResponse', (_message.Message,), {
  'DESCRIPTOR' : _INTEGERDIVISIONRESPONSE,
  '__module__' : 'sandbox.test.service_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.IntegerDivisionResponse)
  })
_sym_db.RegisterMessage(IntegerDivisionResponse)

_SIMPLESERVICE = DESCRIPTOR.services_by_name['SimpleService']
_MATH = DESCRIPTOR.services_by_name['Math']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HELLOREQUEST._serialized_start=44
  _HELLOREQUEST._serialized_end=76
  _HELLORESPONSE._serialized_start=78
  _HELLORESPONSE._serialized_end=108
  _GREETINGMESSAGE._serialized_start=110
  _GREETINGMESSAGE._serialized_end=163
  _NESTEDHELLOREQUEST._serialized_start=165
  _NESTEDHELLOREQUEST._serialized_end=236
  _NESTEDHELLORESPONSE._serialized_start=238
  _NESTEDHELLORESPONSE._serialized_end=308
  _EMPTYHELLOREQUEST._serialized_start=310
  _EMPTYHELLOREQUEST._serialized_end=329
  _EMPTYHELLORESPONSE._serialized_start=331
  _EMPTYHELLORESPONSE._serialized_end=351
  _ADDREQUEST._serialized_start=353
  _ADDREQUEST._serialized_end=387
  _ADDRESPONSE._serialized_start=389
  _ADDRESPONSE._serialized_end=418
  _SUBTRACTREQUEST._serialized_start=420
  _SUBTRACTREQUEST._serialized_end=459
  _SUBTRACTRESPONSE._serialized_start=461
  _SUBTRACTRESPONSE._serialized_end=495
  _INTEGERDIVISIONREQUEST._serialized_start=497
  _INTEGERDIVISIONREQUEST._serialized_end=543
  _INTEGERDIVISIONRESPONSE._serialized_start=545
  _INTEGERDIVISIONRESPONSE._serialized_end=605
  _SIMPLESERVICE._serialized_start=608
  _SIMPLESERVICE._serialized_end=854
  _MATH._serialized_start=857
  _MATH._serialized_end=1094
# @@protoc_insertion_point(module_scope)
