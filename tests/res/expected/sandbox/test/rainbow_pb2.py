# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sandbox/test/rainbow.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1asandbox/test/rainbow.proto\x12\x0csandbox.test\x1a\x1fgoogle/protobuf/timestamp.proto\"&\n\nSubMessage\x12\x0b\n\x03\x66oo\x18\x01 \x01(\t\x12\x0b\n\x03\x62\x61r\x18\x02 \x01(\t\"\x9f\x03\n\x0eRainbowMessage\x12\x14\n\x0csimple_field\x18\x01 \x01(\t\x12/\n\rmessage_field\x18\x02 \x01(\x0b\x32\x18.sandbox.test.SubMessage\x12\x13\n\x0bsimple_list\x18\x03 \x03(\t\x12.\n\x0cmessage_list\x18\x04 \x03(\x0b\x32\x18.sandbox.test.SubMessage\x12?\n\nsimple_map\x18\x05 \x03(\x0b\x32+.sandbox.test.RainbowMessage.SimpleMapEntry\x12\x41\n\x0bmessage_map\x18\x06 \x03(\x0b\x32,.sandbox.test.RainbowMessage.MessageMapEntry\x1a\x30\n\x0eSimpleMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aK\n\x0fMessageMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.sandbox.test.SubMessage:\x02\x38\x01\"\x9c\x02\n\x10TimestampMessage\x12\x30\n\x0cmy_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x11my_timestamp_list\x18\x02 \x03(\x0b\x32\x1a.google.protobuf.Timestamp\x12L\n\x10my_timestamp_map\x18\x03 \x03(\x0b\x32\x32.sandbox.test.TimestampMessage.MyTimestampMapEntry\x1aQ\n\x13MyTimestampMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp:\x02\x38\x01\"\xac\x01\n\x0c\x42ytesMessage\x12\x10\n\x08my_bytes\x18\x01 \x01(\x0c\x12\x15\n\rmy_bytes_list\x18\x02 \x03(\x0c\x12@\n\x0cmy_bytes_map\x18\x03 \x03(\x0b\x32*.sandbox.test.BytesMessage.MyBytesMapEntry\x1a\x31\n\x0fMyBytesMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\xa7\x02\n\x08\x41llTypes\x12\x11\n\tmy_string\x18\x01 \x01(\t\x12\x10\n\x08my_float\x18\x02 \x01(\x02\x12\x11\n\tmy_double\x18\x03 \x01(\x01\x12\x10\n\x08my_int32\x18\x04 \x01(\x05\x12\x10\n\x08my_int64\x18\x05 \x01(\x03\x12\x11\n\tmy_uint32\x18\x06 \x01(\r\x12\x11\n\tmy_uint64\x18\x07 \x01(\x04\x12\x11\n\tmy_sint32\x18\x08 \x01(\x11\x12\x11\n\tmy_sint64\x18\t \x01(\x12\x12\x12\n\nmy_fixed32\x18\n \x01(\x07\x12\x12\n\nmy_fixed64\x18\x0b \x01(\x06\x12\x13\n\x0bmy_sfixed32\x18\x0c \x01(\x0f\x12\x13\n\x0bmy_sfixed64\x18\r \x01(\x10\x12\x0f\n\x07my_bool\x18\x0e \x01(\x08\x12\x10\n\x08my_bytes\x18\x0f \x01(\x0c\"\xf6\x02\n\x0c\x41llTypesList\x12\x16\n\x0emy_string_list\x18\x01 \x03(\t\x12\x15\n\rmy_float_list\x18\x02 \x03(\x02\x12\x16\n\x0emy_double_list\x18\x03 \x03(\x01\x12\x15\n\rmy_int32_list\x18\x04 \x03(\x05\x12\x15\n\rmy_int64_list\x18\x05 \x03(\x03\x12\x16\n\x0emy_uint32_list\x18\x06 \x03(\r\x12\x16\n\x0emy_uint64_list\x18\x07 \x03(\x04\x12\x16\n\x0emy_sint32_list\x18\x08 \x03(\x11\x12\x16\n\x0emy_sint64_list\x18\t \x03(\x12\x12\x17\n\x0fmy_fixed32_list\x18\n \x03(\x07\x12\x17\n\x0fmy_fixed64_list\x18\x0b \x03(\x06\x12\x18\n\x10my_sfixed32_list\x18\x0c \x03(\x0f\x12\x18\n\x10my_sfixed64_list\x18\r \x03(\x10\x12\x14\n\x0cmy_bool_list\x18\x0e \x03(\x08\x12\x15\n\rmy_bytes_list\x18\x0f \x03(\x0c\"\xa7\x0b\n\x0b\x41llTypesMap\x12\x41\n\rmy_string_map\x18\x01 \x03(\x0b\x32*.sandbox.test.AllTypesMap.MyStringMapEntry\x12?\n\x0cmy_int32_map\x18\x04 \x03(\x0b\x32).sandbox.test.AllTypesMap.MyInt32MapEntry\x12?\n\x0cmy_int64_map\x18\x05 \x03(\x0b\x32).sandbox.test.AllTypesMap.MyInt64MapEntry\x12\x41\n\rmy_uint32_map\x18\x06 \x03(\x0b\x32*.sandbox.test.AllTypesMap.MyUint32MapEntry\x12\x41\n\rmy_uint64_map\x18\x07 \x03(\x0b\x32*.sandbox.test.AllTypesMap.MyUint64MapEntry\x12\x41\n\rmy_sint32_map\x18\x08 \x03(\x0b\x32*.sandbox.test.AllTypesMap.MySint32MapEntry\x12\x41\n\rmy_sint64_map\x18\t \x03(\x0b\x32*.sandbox.test.AllTypesMap.MySint64MapEntry\x12\x43\n\x0emy_fixed32_map\x18\n \x03(\x0b\x32+.sandbox.test.AllTypesMap.MyFixed32MapEntry\x12\x43\n\x0emy_fixed64_map\x18\x0b \x03(\x0b\x32+.sandbox.test.AllTypesMap.MyFixed64MapEntry\x12\x45\n\x0fmy_sfixed32_map\x18\x0c \x03(\x0b\x32,.sandbox.test.AllTypesMap.MySfixed32MapEntry\x12\x45\n\x0fmy_sfixed64_map\x18\r \x03(\x0b\x32,.sandbox.test.AllTypesMap.MySfixed64MapEntry\x12=\n\x0bmy_bool_map\x18\x0e \x03(\x0b\x32(.sandbox.test.AllTypesMap.MyBoolMapEntry\x1a\x32\n\x10MyStringMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x31\n\x0fMyInt32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x31\n\x0fMyInt64MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a\x32\n\x10MyUint32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x32\n\x10MyUint64MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\x1a\x32\n\x10MySint32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x11\x12\r\n\x05value\x18\x02 \x01(\x11:\x02\x38\x01\x1a\x32\n\x10MySint64MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x12\x12\r\n\x05value\x18\x02 \x01(\x12:\x02\x38\x01\x1a\x33\n\x11MyFixed32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x07\x12\r\n\x05value\x18\x02 \x01(\x07:\x02\x38\x01\x1a\x33\n\x11MyFixed64MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x06\x12\r\n\x05value\x18\x02 \x01(\x06:\x02\x38\x01\x1a\x34\n\x12MySfixed32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x0f\x12\r\n\x05value\x18\x02 \x01(\x0f:\x02\x38\x01\x1a\x34\n\x12MySfixed64MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x10\x12\r\n\x05value\x18\x02 \x01(\x10:\x02\x38\x01\x1a\x30\n\x0eMyBoolMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\"\xad\x0e\n\x11\x41llTypesNestedMap\x12G\n\rmy_string_map\x18\x01 \x03(\x0b\x32\x30.sandbox.test.AllTypesNestedMap.MyStringMapEntry\x12\x45\n\x0cmy_int32_map\x18\x04 \x03(\x0b\x32/.sandbox.test.AllTypesNestedMap.MyInt32MapEntry\x12\x45\n\x0cmy_int64_map\x18\x05 \x03(\x0b\x32/.sandbox.test.AllTypesNestedMap.MyInt64MapEntry\x12G\n\rmy_uint32_map\x18\x06 \x03(\x0b\x32\x30.sandbox.test.AllTypesNestedMap.MyUint32MapEntry\x12G\n\rmy_uint64_map\x18\x07 \x03(\x0b\x32\x30.sandbox.test.AllTypesNestedMap.MyUint64MapEntry\x12G\n\rmy_sint32_map\x18\x08 \x03(\x0b\x32\x30.sandbox.test.AllTypesNestedMap.MySint32MapEntry\x12G\n\rmy_sint64_map\x18\t \x03(\x0b\x32\x30.sandbox.test.AllTypesNestedMap.MySint64MapEntry\x12I\n\x0emy_fixed32_map\x18\n \x03(\x0b\x32\x31.sandbox.test.AllTypesNestedMap.MyFixed32MapEntry\x12I\n\x0emy_fixed64_map\x18\x0b \x03(\x0b\x32\x31.sandbox.test.AllTypesNestedMap.MyFixed64MapEntry\x12K\n\x0fmy_sfixed32_map\x18\x0c \x03(\x0b\x32\x32.sandbox.test.AllTypesNestedMap.MySfixed32MapEntry\x12K\n\x0fmy_sfixed64_map\x18\r \x03(\x0b\x32\x32.sandbox.test.AllTypesNestedMap.MySfixed64MapEntry\x12\x43\n\x0bmy_bool_map\x18\x0e \x03(\x0b\x32..sandbox.test.AllTypesNestedMap.MyBoolMapEntry\x1aL\n\x10MyStringMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.sandbox.test.SubMessage:\x02\x38\x01\x1aK\n\x0fMyInt32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.sandbox.test.SubMessage:\x02\x38\x01\x1aK\n\x0fMyInt64MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.sandbox.test.SubMessage:\x02\x38\x01\x1aL\n\x10MyUint32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.sandbox.test.SubMessage:\x02\x38\x01\x1aL\n\x10MyUint64MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.sandbox.test.SubMessage:\x02\x38\x01\x1aL\n\x10MySint32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x11\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.sandbox.test.SubMessage:\x02\x38\x01\x1aL\n\x10MySint64MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x12\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.sandbox.test.SubMessage:\x02\x38\x01\x1aM\n\x11MyFixed32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x07\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.sandbox.test.SubMessage:\x02\x38\x01\x1aM\n\x11MyFixed64MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x06\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.sandbox.test.SubMessage:\x02\x38\x01\x1aN\n\x12MySfixed32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x0f\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.sandbox.test.SubMessage:\x02\x38\x01\x1aN\n\x12MySfixed64MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x10\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.sandbox.test.SubMessage:\x02\x38\x01\x1aJ\n\x0eMyBoolMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x08\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.sandbox.test.SubMessage:\x02\x38\x01\x62\x06proto3')



_SUBMESSAGE = DESCRIPTOR.message_types_by_name['SubMessage']
_RAINBOWMESSAGE = DESCRIPTOR.message_types_by_name['RainbowMessage']
_RAINBOWMESSAGE_SIMPLEMAPENTRY = _RAINBOWMESSAGE.nested_types_by_name['SimpleMapEntry']
_RAINBOWMESSAGE_MESSAGEMAPENTRY = _RAINBOWMESSAGE.nested_types_by_name['MessageMapEntry']
_TIMESTAMPMESSAGE = DESCRIPTOR.message_types_by_name['TimestampMessage']
_TIMESTAMPMESSAGE_MYTIMESTAMPMAPENTRY = _TIMESTAMPMESSAGE.nested_types_by_name['MyTimestampMapEntry']
_BYTESMESSAGE = DESCRIPTOR.message_types_by_name['BytesMessage']
_BYTESMESSAGE_MYBYTESMAPENTRY = _BYTESMESSAGE.nested_types_by_name['MyBytesMapEntry']
_ALLTYPES = DESCRIPTOR.message_types_by_name['AllTypes']
_ALLTYPESLIST = DESCRIPTOR.message_types_by_name['AllTypesList']
_ALLTYPESMAP = DESCRIPTOR.message_types_by_name['AllTypesMap']
_ALLTYPESMAP_MYSTRINGMAPENTRY = _ALLTYPESMAP.nested_types_by_name['MyStringMapEntry']
_ALLTYPESMAP_MYINT32MAPENTRY = _ALLTYPESMAP.nested_types_by_name['MyInt32MapEntry']
_ALLTYPESMAP_MYINT64MAPENTRY = _ALLTYPESMAP.nested_types_by_name['MyInt64MapEntry']
_ALLTYPESMAP_MYUINT32MAPENTRY = _ALLTYPESMAP.nested_types_by_name['MyUint32MapEntry']
_ALLTYPESMAP_MYUINT64MAPENTRY = _ALLTYPESMAP.nested_types_by_name['MyUint64MapEntry']
_ALLTYPESMAP_MYSINT32MAPENTRY = _ALLTYPESMAP.nested_types_by_name['MySint32MapEntry']
_ALLTYPESMAP_MYSINT64MAPENTRY = _ALLTYPESMAP.nested_types_by_name['MySint64MapEntry']
_ALLTYPESMAP_MYFIXED32MAPENTRY = _ALLTYPESMAP.nested_types_by_name['MyFixed32MapEntry']
_ALLTYPESMAP_MYFIXED64MAPENTRY = _ALLTYPESMAP.nested_types_by_name['MyFixed64MapEntry']
_ALLTYPESMAP_MYSFIXED32MAPENTRY = _ALLTYPESMAP.nested_types_by_name['MySfixed32MapEntry']
_ALLTYPESMAP_MYSFIXED64MAPENTRY = _ALLTYPESMAP.nested_types_by_name['MySfixed64MapEntry']
_ALLTYPESMAP_MYBOOLMAPENTRY = _ALLTYPESMAP.nested_types_by_name['MyBoolMapEntry']
_ALLTYPESNESTEDMAP = DESCRIPTOR.message_types_by_name['AllTypesNestedMap']
_ALLTYPESNESTEDMAP_MYSTRINGMAPENTRY = _ALLTYPESNESTEDMAP.nested_types_by_name['MyStringMapEntry']
_ALLTYPESNESTEDMAP_MYINT32MAPENTRY = _ALLTYPESNESTEDMAP.nested_types_by_name['MyInt32MapEntry']
_ALLTYPESNESTEDMAP_MYINT64MAPENTRY = _ALLTYPESNESTEDMAP.nested_types_by_name['MyInt64MapEntry']
_ALLTYPESNESTEDMAP_MYUINT32MAPENTRY = _ALLTYPESNESTEDMAP.nested_types_by_name['MyUint32MapEntry']
_ALLTYPESNESTEDMAP_MYUINT64MAPENTRY = _ALLTYPESNESTEDMAP.nested_types_by_name['MyUint64MapEntry']
_ALLTYPESNESTEDMAP_MYSINT32MAPENTRY = _ALLTYPESNESTEDMAP.nested_types_by_name['MySint32MapEntry']
_ALLTYPESNESTEDMAP_MYSINT64MAPENTRY = _ALLTYPESNESTEDMAP.nested_types_by_name['MySint64MapEntry']
_ALLTYPESNESTEDMAP_MYFIXED32MAPENTRY = _ALLTYPESNESTEDMAP.nested_types_by_name['MyFixed32MapEntry']
_ALLTYPESNESTEDMAP_MYFIXED64MAPENTRY = _ALLTYPESNESTEDMAP.nested_types_by_name['MyFixed64MapEntry']
_ALLTYPESNESTEDMAP_MYSFIXED32MAPENTRY = _ALLTYPESNESTEDMAP.nested_types_by_name['MySfixed32MapEntry']
_ALLTYPESNESTEDMAP_MYSFIXED64MAPENTRY = _ALLTYPESNESTEDMAP.nested_types_by_name['MySfixed64MapEntry']
_ALLTYPESNESTEDMAP_MYBOOLMAPENTRY = _ALLTYPESNESTEDMAP.nested_types_by_name['MyBoolMapEntry']
SubMessage = _reflection.GeneratedProtocolMessageType('SubMessage', (_message.Message,), {
  'DESCRIPTOR' : _SUBMESSAGE,
  '__module__' : 'sandbox.test.rainbow_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.SubMessage)
  })
_sym_db.RegisterMessage(SubMessage)

RainbowMessage = _reflection.GeneratedProtocolMessageType('RainbowMessage', (_message.Message,), {

  'SimpleMapEntry' : _reflection.GeneratedProtocolMessageType('SimpleMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _RAINBOWMESSAGE_SIMPLEMAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.RainbowMessage.SimpleMapEntry)
    })
  ,

  'MessageMapEntry' : _reflection.GeneratedProtocolMessageType('MessageMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _RAINBOWMESSAGE_MESSAGEMAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.RainbowMessage.MessageMapEntry)
    })
  ,
  'DESCRIPTOR' : _RAINBOWMESSAGE,
  '__module__' : 'sandbox.test.rainbow_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.RainbowMessage)
  })
_sym_db.RegisterMessage(RainbowMessage)
_sym_db.RegisterMessage(RainbowMessage.SimpleMapEntry)
_sym_db.RegisterMessage(RainbowMessage.MessageMapEntry)

TimestampMessage = _reflection.GeneratedProtocolMessageType('TimestampMessage', (_message.Message,), {

  'MyTimestampMapEntry' : _reflection.GeneratedProtocolMessageType('MyTimestampMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _TIMESTAMPMESSAGE_MYTIMESTAMPMAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.TimestampMessage.MyTimestampMapEntry)
    })
  ,
  'DESCRIPTOR' : _TIMESTAMPMESSAGE,
  '__module__' : 'sandbox.test.rainbow_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.TimestampMessage)
  })
_sym_db.RegisterMessage(TimestampMessage)
_sym_db.RegisterMessage(TimestampMessage.MyTimestampMapEntry)

BytesMessage = _reflection.GeneratedProtocolMessageType('BytesMessage', (_message.Message,), {

  'MyBytesMapEntry' : _reflection.GeneratedProtocolMessageType('MyBytesMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _BYTESMESSAGE_MYBYTESMAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.BytesMessage.MyBytesMapEntry)
    })
  ,
  'DESCRIPTOR' : _BYTESMESSAGE,
  '__module__' : 'sandbox.test.rainbow_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.BytesMessage)
  })
_sym_db.RegisterMessage(BytesMessage)
_sym_db.RegisterMessage(BytesMessage.MyBytesMapEntry)

AllTypes = _reflection.GeneratedProtocolMessageType('AllTypes', (_message.Message,), {
  'DESCRIPTOR' : _ALLTYPES,
  '__module__' : 'sandbox.test.rainbow_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.AllTypes)
  })
_sym_db.RegisterMessage(AllTypes)

AllTypesList = _reflection.GeneratedProtocolMessageType('AllTypesList', (_message.Message,), {
  'DESCRIPTOR' : _ALLTYPESLIST,
  '__module__' : 'sandbox.test.rainbow_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesList)
  })
_sym_db.RegisterMessage(AllTypesList)

AllTypesMap = _reflection.GeneratedProtocolMessageType('AllTypesMap', (_message.Message,), {

  'MyStringMapEntry' : _reflection.GeneratedProtocolMessageType('MyStringMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESMAP_MYSTRINGMAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesMap.MyStringMapEntry)
    })
  ,

  'MyInt32MapEntry' : _reflection.GeneratedProtocolMessageType('MyInt32MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESMAP_MYINT32MAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesMap.MyInt32MapEntry)
    })
  ,

  'MyInt64MapEntry' : _reflection.GeneratedProtocolMessageType('MyInt64MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESMAP_MYINT64MAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesMap.MyInt64MapEntry)
    })
  ,

  'MyUint32MapEntry' : _reflection.GeneratedProtocolMessageType('MyUint32MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESMAP_MYUINT32MAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesMap.MyUint32MapEntry)
    })
  ,

  'MyUint64MapEntry' : _reflection.GeneratedProtocolMessageType('MyUint64MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESMAP_MYUINT64MAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesMap.MyUint64MapEntry)
    })
  ,

  'MySint32MapEntry' : _reflection.GeneratedProtocolMessageType('MySint32MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESMAP_MYSINT32MAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesMap.MySint32MapEntry)
    })
  ,

  'MySint64MapEntry' : _reflection.GeneratedProtocolMessageType('MySint64MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESMAP_MYSINT64MAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesMap.MySint64MapEntry)
    })
  ,

  'MyFixed32MapEntry' : _reflection.GeneratedProtocolMessageType('MyFixed32MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESMAP_MYFIXED32MAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesMap.MyFixed32MapEntry)
    })
  ,

  'MyFixed64MapEntry' : _reflection.GeneratedProtocolMessageType('MyFixed64MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESMAP_MYFIXED64MAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesMap.MyFixed64MapEntry)
    })
  ,

  'MySfixed32MapEntry' : _reflection.GeneratedProtocolMessageType('MySfixed32MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESMAP_MYSFIXED32MAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesMap.MySfixed32MapEntry)
    })
  ,

  'MySfixed64MapEntry' : _reflection.GeneratedProtocolMessageType('MySfixed64MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESMAP_MYSFIXED64MAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesMap.MySfixed64MapEntry)
    })
  ,

  'MyBoolMapEntry' : _reflection.GeneratedProtocolMessageType('MyBoolMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESMAP_MYBOOLMAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesMap.MyBoolMapEntry)
    })
  ,
  'DESCRIPTOR' : _ALLTYPESMAP,
  '__module__' : 'sandbox.test.rainbow_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesMap)
  })
_sym_db.RegisterMessage(AllTypesMap)
_sym_db.RegisterMessage(AllTypesMap.MyStringMapEntry)
_sym_db.RegisterMessage(AllTypesMap.MyInt32MapEntry)
_sym_db.RegisterMessage(AllTypesMap.MyInt64MapEntry)
_sym_db.RegisterMessage(AllTypesMap.MyUint32MapEntry)
_sym_db.RegisterMessage(AllTypesMap.MyUint64MapEntry)
_sym_db.RegisterMessage(AllTypesMap.MySint32MapEntry)
_sym_db.RegisterMessage(AllTypesMap.MySint64MapEntry)
_sym_db.RegisterMessage(AllTypesMap.MyFixed32MapEntry)
_sym_db.RegisterMessage(AllTypesMap.MyFixed64MapEntry)
_sym_db.RegisterMessage(AllTypesMap.MySfixed32MapEntry)
_sym_db.RegisterMessage(AllTypesMap.MySfixed64MapEntry)
_sym_db.RegisterMessage(AllTypesMap.MyBoolMapEntry)

AllTypesNestedMap = _reflection.GeneratedProtocolMessageType('AllTypesNestedMap', (_message.Message,), {

  'MyStringMapEntry' : _reflection.GeneratedProtocolMessageType('MyStringMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESNESTEDMAP_MYSTRINGMAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesNestedMap.MyStringMapEntry)
    })
  ,

  'MyInt32MapEntry' : _reflection.GeneratedProtocolMessageType('MyInt32MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESNESTEDMAP_MYINT32MAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesNestedMap.MyInt32MapEntry)
    })
  ,

  'MyInt64MapEntry' : _reflection.GeneratedProtocolMessageType('MyInt64MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESNESTEDMAP_MYINT64MAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesNestedMap.MyInt64MapEntry)
    })
  ,

  'MyUint32MapEntry' : _reflection.GeneratedProtocolMessageType('MyUint32MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESNESTEDMAP_MYUINT32MAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesNestedMap.MyUint32MapEntry)
    })
  ,

  'MyUint64MapEntry' : _reflection.GeneratedProtocolMessageType('MyUint64MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESNESTEDMAP_MYUINT64MAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesNestedMap.MyUint64MapEntry)
    })
  ,

  'MySint32MapEntry' : _reflection.GeneratedProtocolMessageType('MySint32MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESNESTEDMAP_MYSINT32MAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesNestedMap.MySint32MapEntry)
    })
  ,

  'MySint64MapEntry' : _reflection.GeneratedProtocolMessageType('MySint64MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESNESTEDMAP_MYSINT64MAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesNestedMap.MySint64MapEntry)
    })
  ,

  'MyFixed32MapEntry' : _reflection.GeneratedProtocolMessageType('MyFixed32MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESNESTEDMAP_MYFIXED32MAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesNestedMap.MyFixed32MapEntry)
    })
  ,

  'MyFixed64MapEntry' : _reflection.GeneratedProtocolMessageType('MyFixed64MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESNESTEDMAP_MYFIXED64MAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesNestedMap.MyFixed64MapEntry)
    })
  ,

  'MySfixed32MapEntry' : _reflection.GeneratedProtocolMessageType('MySfixed32MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESNESTEDMAP_MYSFIXED32MAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesNestedMap.MySfixed32MapEntry)
    })
  ,

  'MySfixed64MapEntry' : _reflection.GeneratedProtocolMessageType('MySfixed64MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESNESTEDMAP_MYSFIXED64MAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesNestedMap.MySfixed64MapEntry)
    })
  ,

  'MyBoolMapEntry' : _reflection.GeneratedProtocolMessageType('MyBoolMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALLTYPESNESTEDMAP_MYBOOLMAPENTRY,
    '__module__' : 'sandbox.test.rainbow_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesNestedMap.MyBoolMapEntry)
    })
  ,
  'DESCRIPTOR' : _ALLTYPESNESTEDMAP,
  '__module__' : 'sandbox.test.rainbow_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.AllTypesNestedMap)
  })
_sym_db.RegisterMessage(AllTypesNestedMap)
_sym_db.RegisterMessage(AllTypesNestedMap.MyStringMapEntry)
_sym_db.RegisterMessage(AllTypesNestedMap.MyInt32MapEntry)
_sym_db.RegisterMessage(AllTypesNestedMap.MyInt64MapEntry)
_sym_db.RegisterMessage(AllTypesNestedMap.MyUint32MapEntry)
_sym_db.RegisterMessage(AllTypesNestedMap.MyUint64MapEntry)
_sym_db.RegisterMessage(AllTypesNestedMap.MySint32MapEntry)
_sym_db.RegisterMessage(AllTypesNestedMap.MySint64MapEntry)
_sym_db.RegisterMessage(AllTypesNestedMap.MyFixed32MapEntry)
_sym_db.RegisterMessage(AllTypesNestedMap.MyFixed64MapEntry)
_sym_db.RegisterMessage(AllTypesNestedMap.MySfixed32MapEntry)
_sym_db.RegisterMessage(AllTypesNestedMap.MySfixed64MapEntry)
_sym_db.RegisterMessage(AllTypesNestedMap.MyBoolMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RAINBOWMESSAGE_SIMPLEMAPENTRY._options = None
  _RAINBOWMESSAGE_SIMPLEMAPENTRY._serialized_options = b'8\001'
  _RAINBOWMESSAGE_MESSAGEMAPENTRY._options = None
  _RAINBOWMESSAGE_MESSAGEMAPENTRY._serialized_options = b'8\001'
  _TIMESTAMPMESSAGE_MYTIMESTAMPMAPENTRY._options = None
  _TIMESTAMPMESSAGE_MYTIMESTAMPMAPENTRY._serialized_options = b'8\001'
  _BYTESMESSAGE_MYBYTESMAPENTRY._options = None
  _BYTESMESSAGE_MYBYTESMAPENTRY._serialized_options = b'8\001'
  _ALLTYPESMAP_MYSTRINGMAPENTRY._options = None
  _ALLTYPESMAP_MYSTRINGMAPENTRY._serialized_options = b'8\001'
  _ALLTYPESMAP_MYINT32MAPENTRY._options = None
  _ALLTYPESMAP_MYINT32MAPENTRY._serialized_options = b'8\001'
  _ALLTYPESMAP_MYINT64MAPENTRY._options = None
  _ALLTYPESMAP_MYINT64MAPENTRY._serialized_options = b'8\001'
  _ALLTYPESMAP_MYUINT32MAPENTRY._options = None
  _ALLTYPESMAP_MYUINT32MAPENTRY._serialized_options = b'8\001'
  _ALLTYPESMAP_MYUINT64MAPENTRY._options = None
  _ALLTYPESMAP_MYUINT64MAPENTRY._serialized_options = b'8\001'
  _ALLTYPESMAP_MYSINT32MAPENTRY._options = None
  _ALLTYPESMAP_MYSINT32MAPENTRY._serialized_options = b'8\001'
  _ALLTYPESMAP_MYSINT64MAPENTRY._options = None
  _ALLTYPESMAP_MYSINT64MAPENTRY._serialized_options = b'8\001'
  _ALLTYPESMAP_MYFIXED32MAPENTRY._options = None
  _ALLTYPESMAP_MYFIXED32MAPENTRY._serialized_options = b'8\001'
  _ALLTYPESMAP_MYFIXED64MAPENTRY._options = None
  _ALLTYPESMAP_MYFIXED64MAPENTRY._serialized_options = b'8\001'
  _ALLTYPESMAP_MYSFIXED32MAPENTRY._options = None
  _ALLTYPESMAP_MYSFIXED32MAPENTRY._serialized_options = b'8\001'
  _ALLTYPESMAP_MYSFIXED64MAPENTRY._options = None
  _ALLTYPESMAP_MYSFIXED64MAPENTRY._serialized_options = b'8\001'
  _ALLTYPESMAP_MYBOOLMAPENTRY._options = None
  _ALLTYPESMAP_MYBOOLMAPENTRY._serialized_options = b'8\001'
  _ALLTYPESNESTEDMAP_MYSTRINGMAPENTRY._options = None
  _ALLTYPESNESTEDMAP_MYSTRINGMAPENTRY._serialized_options = b'8\001'
  _ALLTYPESNESTEDMAP_MYINT32MAPENTRY._options = None
  _ALLTYPESNESTEDMAP_MYINT32MAPENTRY._serialized_options = b'8\001'
  _ALLTYPESNESTEDMAP_MYINT64MAPENTRY._options = None
  _ALLTYPESNESTEDMAP_MYINT64MAPENTRY._serialized_options = b'8\001'
  _ALLTYPESNESTEDMAP_MYUINT32MAPENTRY._options = None
  _ALLTYPESNESTEDMAP_MYUINT32MAPENTRY._serialized_options = b'8\001'
  _ALLTYPESNESTEDMAP_MYUINT64MAPENTRY._options = None
  _ALLTYPESNESTEDMAP_MYUINT64MAPENTRY._serialized_options = b'8\001'
  _ALLTYPESNESTEDMAP_MYSINT32MAPENTRY._options = None
  _ALLTYPESNESTEDMAP_MYSINT32MAPENTRY._serialized_options = b'8\001'
  _ALLTYPESNESTEDMAP_MYSINT64MAPENTRY._options = None
  _ALLTYPESNESTEDMAP_MYSINT64MAPENTRY._serialized_options = b'8\001'
  _ALLTYPESNESTEDMAP_MYFIXED32MAPENTRY._options = None
  _ALLTYPESNESTEDMAP_MYFIXED32MAPENTRY._serialized_options = b'8\001'
  _ALLTYPESNESTEDMAP_MYFIXED64MAPENTRY._options = None
  _ALLTYPESNESTEDMAP_MYFIXED64MAPENTRY._serialized_options = b'8\001'
  _ALLTYPESNESTEDMAP_MYSFIXED32MAPENTRY._options = None
  _ALLTYPESNESTEDMAP_MYSFIXED32MAPENTRY._serialized_options = b'8\001'
  _ALLTYPESNESTEDMAP_MYSFIXED64MAPENTRY._options = None
  _ALLTYPESNESTEDMAP_MYSFIXED64MAPENTRY._serialized_options = b'8\001'
  _ALLTYPESNESTEDMAP_MYBOOLMAPENTRY._options = None
  _ALLTYPESNESTEDMAP_MYBOOLMAPENTRY._serialized_options = b'8\001'
  _SUBMESSAGE._serialized_start=77
  _SUBMESSAGE._serialized_end=115
  _RAINBOWMESSAGE._serialized_start=118
  _RAINBOWMESSAGE._serialized_end=533
  _RAINBOWMESSAGE_SIMPLEMAPENTRY._serialized_start=408
  _RAINBOWMESSAGE_SIMPLEMAPENTRY._serialized_end=456
  _RAINBOWMESSAGE_MESSAGEMAPENTRY._serialized_start=458
  _RAINBOWMESSAGE_MESSAGEMAPENTRY._serialized_end=533
  _TIMESTAMPMESSAGE._serialized_start=536
  _TIMESTAMPMESSAGE._serialized_end=820
  _TIMESTAMPMESSAGE_MYTIMESTAMPMAPENTRY._serialized_start=739
  _TIMESTAMPMESSAGE_MYTIMESTAMPMAPENTRY._serialized_end=820
  _BYTESMESSAGE._serialized_start=823
  _BYTESMESSAGE._serialized_end=995
  _BYTESMESSAGE_MYBYTESMAPENTRY._serialized_start=946
  _BYTESMESSAGE_MYBYTESMAPENTRY._serialized_end=995
  _ALLTYPES._serialized_start=998
  _ALLTYPES._serialized_end=1293
  _ALLTYPESLIST._serialized_start=1296
  _ALLTYPESLIST._serialized_end=1670
  _ALLTYPESMAP._serialized_start=1673
  _ALLTYPESMAP._serialized_end=3120
  _ALLTYPESMAP_MYSTRINGMAPENTRY._serialized_start=2496
  _ALLTYPESMAP_MYSTRINGMAPENTRY._serialized_end=2546
  _ALLTYPESMAP_MYINT32MAPENTRY._serialized_start=2548
  _ALLTYPESMAP_MYINT32MAPENTRY._serialized_end=2597
  _ALLTYPESMAP_MYINT64MAPENTRY._serialized_start=2599
  _ALLTYPESMAP_MYINT64MAPENTRY._serialized_end=2648
  _ALLTYPESMAP_MYUINT32MAPENTRY._serialized_start=2650
  _ALLTYPESMAP_MYUINT32MAPENTRY._serialized_end=2700
  _ALLTYPESMAP_MYUINT64MAPENTRY._serialized_start=2702
  _ALLTYPESMAP_MYUINT64MAPENTRY._serialized_end=2752
  _ALLTYPESMAP_MYSINT32MAPENTRY._serialized_start=2754
  _ALLTYPESMAP_MYSINT32MAPENTRY._serialized_end=2804
  _ALLTYPESMAP_MYSINT64MAPENTRY._serialized_start=2806
  _ALLTYPESMAP_MYSINT64MAPENTRY._serialized_end=2856
  _ALLTYPESMAP_MYFIXED32MAPENTRY._serialized_start=2858
  _ALLTYPESMAP_MYFIXED32MAPENTRY._serialized_end=2909
  _ALLTYPESMAP_MYFIXED64MAPENTRY._serialized_start=2911
  _ALLTYPESMAP_MYFIXED64MAPENTRY._serialized_end=2962
  _ALLTYPESMAP_MYSFIXED32MAPENTRY._serialized_start=2964
  _ALLTYPESMAP_MYSFIXED32MAPENTRY._serialized_end=3016
  _ALLTYPESMAP_MYSFIXED64MAPENTRY._serialized_start=3018
  _ALLTYPESMAP_MYSFIXED64MAPENTRY._serialized_end=3070
  _ALLTYPESMAP_MYBOOLMAPENTRY._serialized_start=3072
  _ALLTYPESMAP_MYBOOLMAPENTRY._serialized_end=3120
  _ALLTYPESNESTEDMAP._serialized_start=3123
  _ALLTYPESNESTEDMAP._serialized_end=4960
  _ALLTYPESNESTEDMAP_MYSTRINGMAPENTRY._serialized_start=4024
  _ALLTYPESNESTEDMAP_MYSTRINGMAPENTRY._serialized_end=4100
  _ALLTYPESNESTEDMAP_MYINT32MAPENTRY._serialized_start=4102
  _ALLTYPESNESTEDMAP_MYINT32MAPENTRY._serialized_end=4177
  _ALLTYPESNESTEDMAP_MYINT64MAPENTRY._serialized_start=4179
  _ALLTYPESNESTEDMAP_MYINT64MAPENTRY._serialized_end=4254
  _ALLTYPESNESTEDMAP_MYUINT32MAPENTRY._serialized_start=4256
  _ALLTYPESNESTEDMAP_MYUINT32MAPENTRY._serialized_end=4332
  _ALLTYPESNESTEDMAP_MYUINT64MAPENTRY._serialized_start=4334
  _ALLTYPESNESTEDMAP_MYUINT64MAPENTRY._serialized_end=4410
  _ALLTYPESNESTEDMAP_MYSINT32MAPENTRY._serialized_start=4412
  _ALLTYPESNESTEDMAP_MYSINT32MAPENTRY._serialized_end=4488
  _ALLTYPESNESTEDMAP_MYSINT64MAPENTRY._serialized_start=4490
  _ALLTYPESNESTEDMAP_MYSINT64MAPENTRY._serialized_end=4566
  _ALLTYPESNESTEDMAP_MYFIXED32MAPENTRY._serialized_start=4568
  _ALLTYPESNESTEDMAP_MYFIXED32MAPENTRY._serialized_end=4645
  _ALLTYPESNESTEDMAP_MYFIXED64MAPENTRY._serialized_start=4647
  _ALLTYPESNESTEDMAP_MYFIXED64MAPENTRY._serialized_end=4724
  _ALLTYPESNESTEDMAP_MYSFIXED32MAPENTRY._serialized_start=4726
  _ALLTYPESNESTEDMAP_MYSFIXED32MAPENTRY._serialized_end=4804
  _ALLTYPESNESTEDMAP_MYSFIXED64MAPENTRY._serialized_start=4806
  _ALLTYPESNESTEDMAP_MYSFIXED64MAPENTRY._serialized_end=4884
  _ALLTYPESNESTEDMAP_MYBOOLMAPENTRY._serialized_start=4886
  _ALLTYPESNESTEDMAP_MYBOOLMAPENTRY._serialized_end=4960
# @@protoc_insertion_point(module_scope)
