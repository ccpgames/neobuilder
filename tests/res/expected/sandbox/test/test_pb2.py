# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sandbox/test/test.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17sandbox/test/test.proto\x12\x0csandbox.test\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa5\x02\n\x06Simple\x12\x11\n\tmy_string\x18\x01 \x01(\t\x12\x10\n\x08my_float\x18\x02 \x01(\x02\x12\x11\n\tmy_double\x18\x03 \x01(\x01\x12\x10\n\x08my_int32\x18\x04 \x01(\x05\x12\x10\n\x08my_int64\x18\x05 \x01(\x03\x12\x11\n\tmy_uint32\x18\x06 \x01(\r\x12\x11\n\tmy_uint64\x18\x07 \x01(\x04\x12\x11\n\tmy_sint32\x18\x08 \x01(\x11\x12\x11\n\tmy_sint64\x18\t \x01(\x12\x12\x12\n\nmy_fixed32\x18\n \x01(\x07\x12\x12\n\nmy_fixed64\x18\x0b \x01(\x06\x12\x13\n\x0bmy_sfixed32\x18\x0c \x01(\x0f\x12\x13\n\x0bmy_sfixed64\x18\r \x01(\x10\x12\x0f\n\x07my_bool\x18\x0e \x01(\x08\x12\x10\n\x08my_bytes\x18\x0f \x01(\x0c\"\xf4\x02\n\nSimpleList\x12\x16\n\x0emy_string_list\x18\x01 \x03(\t\x12\x15\n\rmy_float_list\x18\x02 \x03(\x02\x12\x16\n\x0emy_double_list\x18\x03 \x03(\x01\x12\x15\n\rmy_int32_list\x18\x04 \x03(\x05\x12\x15\n\rmy_int64_list\x18\x05 \x03(\x03\x12\x16\n\x0emy_uint32_list\x18\x06 \x03(\r\x12\x16\n\x0emy_uint64_list\x18\x07 \x03(\x04\x12\x16\n\x0emy_sint32_list\x18\x08 \x03(\x11\x12\x16\n\x0emy_sint64_list\x18\t \x03(\x12\x12\x17\n\x0fmy_fixed32_list\x18\n \x03(\x07\x12\x17\n\x0fmy_fixed64_list\x18\x0b \x03(\x06\x12\x18\n\x10my_sfixed32_list\x18\x0c \x03(\x0f\x12\x18\n\x10my_sfixed64_list\x18\r \x03(\x10\x12\x14\n\x0cmy_bool_list\x18\x0e \x03(\x08\x12\x15\n\rmy_bytes_list\x18\x0f \x03(\x0c\"\x8d\x0b\n\tSimpleMap\x12?\n\rmy_string_map\x18\x01 \x03(\x0b\x32(.sandbox.test.SimpleMap.MyStringMapEntry\x12=\n\x0cmy_int32_map\x18\x04 \x03(\x0b\x32\'.sandbox.test.SimpleMap.MyInt32MapEntry\x12=\n\x0cmy_int64_map\x18\x05 \x03(\x0b\x32\'.sandbox.test.SimpleMap.MyInt64MapEntry\x12?\n\rmy_uint32_map\x18\x06 \x03(\x0b\x32(.sandbox.test.SimpleMap.MyUint32MapEntry\x12?\n\rmy_uint64_map\x18\x07 \x03(\x0b\x32(.sandbox.test.SimpleMap.MyUint64MapEntry\x12?\n\rmy_sint32_map\x18\x08 \x03(\x0b\x32(.sandbox.test.SimpleMap.MySint32MapEntry\x12?\n\rmy_sint64_map\x18\t \x03(\x0b\x32(.sandbox.test.SimpleMap.MySint64MapEntry\x12\x41\n\x0emy_fixed32_map\x18\n \x03(\x0b\x32).sandbox.test.SimpleMap.MyFixed32MapEntry\x12\x41\n\x0emy_fixed64_map\x18\x0b \x03(\x0b\x32).sandbox.test.SimpleMap.MyFixed64MapEntry\x12\x43\n\x0fmy_sfixed32_map\x18\x0c \x03(\x0b\x32*.sandbox.test.SimpleMap.MySfixed32MapEntry\x12\x43\n\x0fmy_sfixed64_map\x18\r \x03(\x0b\x32*.sandbox.test.SimpleMap.MySfixed64MapEntry\x12;\n\x0bmy_bool_map\x18\x0e \x03(\x0b\x32&.sandbox.test.SimpleMap.MyBoolMapEntry\x1a\x32\n\x10MyStringMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x31\n\x0fMyInt32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x31\n\x0fMyInt64MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a\x32\n\x10MyUint32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x32\n\x10MyUint64MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\x1a\x32\n\x10MySint32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x11\x12\r\n\x05value\x18\x02 \x01(\x11:\x02\x38\x01\x1a\x32\n\x10MySint64MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x12\x12\r\n\x05value\x18\x02 \x01(\x12:\x02\x38\x01\x1a\x33\n\x11MyFixed32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x07\x12\r\n\x05value\x18\x02 \x01(\x07:\x02\x38\x01\x1a\x33\n\x11MyFixed64MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x06\x12\r\n\x05value\x18\x02 \x01(\x06:\x02\x38\x01\x1a\x34\n\x12MySfixed32MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x0f\x12\r\n\x05value\x18\x02 \x01(\x0f:\x02\x38\x01\x1a\x34\n\x12MySfixed64MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x10\x12\r\n\x05value\x18\x02 \x01(\x10:\x02\x38\x01\x1a\x30\n\x0eMyBoolMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\"C\n\x0fSimpleTimestamp\x12\x30\n\x0cmy_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"5\n\nNestedDude\x12\'\n\tmy_simple\x18\x01 \x01(\x0b\x32\x14.sandbox.test.Simple\":\n\nNestedList\x12,\n\x0emy_simple_list\x18\x01 \x03(\x0b\x32\x14.sandbox.test.Simple\"\xc4\x02\n\tNestedMap\x12L\n\x14my_string_simple_map\x18\x01 \x03(\x0b\x32..sandbox.test.NestedMap.MyStringSimpleMapEntry\x12J\n\x13my_int32_simple_map\x18\x02 \x03(\x0b\x32-.sandbox.test.NestedMap.MyInt32SimpleMapEntry\x1aN\n\x16MyStringSimpleMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.sandbox.test.Simple:\x02\x38\x01\x1aM\n\x15MyInt32SimpleMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.sandbox.test.Simple:\x02\x38\x01\"\xaa\x01\n\x0eVeryNestedDude\x12\x30\n\x0emy_nested_dude\x18\x01 \x01(\x0b\x32\x18.sandbox.test.NestedDude\x12\x32\n\x14my_non_nested_simple\x18\x02 \x01(\x0b\x32\x14.sandbox.test.Simple\x12\x32\n\x10my_list_of_lists\x18\x03 \x03(\x0b\x32\x18.sandbox.test.NestedListb\x06proto3')



_SIMPLE = DESCRIPTOR.message_types_by_name['Simple']
_SIMPLELIST = DESCRIPTOR.message_types_by_name['SimpleList']
_SIMPLEMAP = DESCRIPTOR.message_types_by_name['SimpleMap']
_SIMPLEMAP_MYSTRINGMAPENTRY = _SIMPLEMAP.nested_types_by_name['MyStringMapEntry']
_SIMPLEMAP_MYINT32MAPENTRY = _SIMPLEMAP.nested_types_by_name['MyInt32MapEntry']
_SIMPLEMAP_MYINT64MAPENTRY = _SIMPLEMAP.nested_types_by_name['MyInt64MapEntry']
_SIMPLEMAP_MYUINT32MAPENTRY = _SIMPLEMAP.nested_types_by_name['MyUint32MapEntry']
_SIMPLEMAP_MYUINT64MAPENTRY = _SIMPLEMAP.nested_types_by_name['MyUint64MapEntry']
_SIMPLEMAP_MYSINT32MAPENTRY = _SIMPLEMAP.nested_types_by_name['MySint32MapEntry']
_SIMPLEMAP_MYSINT64MAPENTRY = _SIMPLEMAP.nested_types_by_name['MySint64MapEntry']
_SIMPLEMAP_MYFIXED32MAPENTRY = _SIMPLEMAP.nested_types_by_name['MyFixed32MapEntry']
_SIMPLEMAP_MYFIXED64MAPENTRY = _SIMPLEMAP.nested_types_by_name['MyFixed64MapEntry']
_SIMPLEMAP_MYSFIXED32MAPENTRY = _SIMPLEMAP.nested_types_by_name['MySfixed32MapEntry']
_SIMPLEMAP_MYSFIXED64MAPENTRY = _SIMPLEMAP.nested_types_by_name['MySfixed64MapEntry']
_SIMPLEMAP_MYBOOLMAPENTRY = _SIMPLEMAP.nested_types_by_name['MyBoolMapEntry']
_SIMPLETIMESTAMP = DESCRIPTOR.message_types_by_name['SimpleTimestamp']
_NESTEDDUDE = DESCRIPTOR.message_types_by_name['NestedDude']
_NESTEDLIST = DESCRIPTOR.message_types_by_name['NestedList']
_NESTEDMAP = DESCRIPTOR.message_types_by_name['NestedMap']
_NESTEDMAP_MYSTRINGSIMPLEMAPENTRY = _NESTEDMAP.nested_types_by_name['MyStringSimpleMapEntry']
_NESTEDMAP_MYINT32SIMPLEMAPENTRY = _NESTEDMAP.nested_types_by_name['MyInt32SimpleMapEntry']
_VERYNESTEDDUDE = DESCRIPTOR.message_types_by_name['VeryNestedDude']
Simple = _reflection.GeneratedProtocolMessageType('Simple', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLE,
  '__module__' : 'sandbox.test.test_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.Simple)
  })
_sym_db.RegisterMessage(Simple)

SimpleList = _reflection.GeneratedProtocolMessageType('SimpleList', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLELIST,
  '__module__' : 'sandbox.test.test_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.SimpleList)
  })
_sym_db.RegisterMessage(SimpleList)

SimpleMap = _reflection.GeneratedProtocolMessageType('SimpleMap', (_message.Message,), {

  'MyStringMapEntry' : _reflection.GeneratedProtocolMessageType('MyStringMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _SIMPLEMAP_MYSTRINGMAPENTRY,
    '__module__' : 'sandbox.test.test_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.SimpleMap.MyStringMapEntry)
    })
  ,

  'MyInt32MapEntry' : _reflection.GeneratedProtocolMessageType('MyInt32MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _SIMPLEMAP_MYINT32MAPENTRY,
    '__module__' : 'sandbox.test.test_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.SimpleMap.MyInt32MapEntry)
    })
  ,

  'MyInt64MapEntry' : _reflection.GeneratedProtocolMessageType('MyInt64MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _SIMPLEMAP_MYINT64MAPENTRY,
    '__module__' : 'sandbox.test.test_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.SimpleMap.MyInt64MapEntry)
    })
  ,

  'MyUint32MapEntry' : _reflection.GeneratedProtocolMessageType('MyUint32MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _SIMPLEMAP_MYUINT32MAPENTRY,
    '__module__' : 'sandbox.test.test_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.SimpleMap.MyUint32MapEntry)
    })
  ,

  'MyUint64MapEntry' : _reflection.GeneratedProtocolMessageType('MyUint64MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _SIMPLEMAP_MYUINT64MAPENTRY,
    '__module__' : 'sandbox.test.test_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.SimpleMap.MyUint64MapEntry)
    })
  ,

  'MySint32MapEntry' : _reflection.GeneratedProtocolMessageType('MySint32MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _SIMPLEMAP_MYSINT32MAPENTRY,
    '__module__' : 'sandbox.test.test_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.SimpleMap.MySint32MapEntry)
    })
  ,

  'MySint64MapEntry' : _reflection.GeneratedProtocolMessageType('MySint64MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _SIMPLEMAP_MYSINT64MAPENTRY,
    '__module__' : 'sandbox.test.test_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.SimpleMap.MySint64MapEntry)
    })
  ,

  'MyFixed32MapEntry' : _reflection.GeneratedProtocolMessageType('MyFixed32MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _SIMPLEMAP_MYFIXED32MAPENTRY,
    '__module__' : 'sandbox.test.test_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.SimpleMap.MyFixed32MapEntry)
    })
  ,

  'MyFixed64MapEntry' : _reflection.GeneratedProtocolMessageType('MyFixed64MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _SIMPLEMAP_MYFIXED64MAPENTRY,
    '__module__' : 'sandbox.test.test_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.SimpleMap.MyFixed64MapEntry)
    })
  ,

  'MySfixed32MapEntry' : _reflection.GeneratedProtocolMessageType('MySfixed32MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _SIMPLEMAP_MYSFIXED32MAPENTRY,
    '__module__' : 'sandbox.test.test_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.SimpleMap.MySfixed32MapEntry)
    })
  ,

  'MySfixed64MapEntry' : _reflection.GeneratedProtocolMessageType('MySfixed64MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _SIMPLEMAP_MYSFIXED64MAPENTRY,
    '__module__' : 'sandbox.test.test_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.SimpleMap.MySfixed64MapEntry)
    })
  ,

  'MyBoolMapEntry' : _reflection.GeneratedProtocolMessageType('MyBoolMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _SIMPLEMAP_MYBOOLMAPENTRY,
    '__module__' : 'sandbox.test.test_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.SimpleMap.MyBoolMapEntry)
    })
  ,
  'DESCRIPTOR' : _SIMPLEMAP,
  '__module__' : 'sandbox.test.test_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.SimpleMap)
  })
_sym_db.RegisterMessage(SimpleMap)
_sym_db.RegisterMessage(SimpleMap.MyStringMapEntry)
_sym_db.RegisterMessage(SimpleMap.MyInt32MapEntry)
_sym_db.RegisterMessage(SimpleMap.MyInt64MapEntry)
_sym_db.RegisterMessage(SimpleMap.MyUint32MapEntry)
_sym_db.RegisterMessage(SimpleMap.MyUint64MapEntry)
_sym_db.RegisterMessage(SimpleMap.MySint32MapEntry)
_sym_db.RegisterMessage(SimpleMap.MySint64MapEntry)
_sym_db.RegisterMessage(SimpleMap.MyFixed32MapEntry)
_sym_db.RegisterMessage(SimpleMap.MyFixed64MapEntry)
_sym_db.RegisterMessage(SimpleMap.MySfixed32MapEntry)
_sym_db.RegisterMessage(SimpleMap.MySfixed64MapEntry)
_sym_db.RegisterMessage(SimpleMap.MyBoolMapEntry)

SimpleTimestamp = _reflection.GeneratedProtocolMessageType('SimpleTimestamp', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLETIMESTAMP,
  '__module__' : 'sandbox.test.test_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.SimpleTimestamp)
  })
_sym_db.RegisterMessage(SimpleTimestamp)

NestedDude = _reflection.GeneratedProtocolMessageType('NestedDude', (_message.Message,), {
  'DESCRIPTOR' : _NESTEDDUDE,
  '__module__' : 'sandbox.test.test_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.NestedDude)
  })
_sym_db.RegisterMessage(NestedDude)

NestedList = _reflection.GeneratedProtocolMessageType('NestedList', (_message.Message,), {
  'DESCRIPTOR' : _NESTEDLIST,
  '__module__' : 'sandbox.test.test_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.NestedList)
  })
_sym_db.RegisterMessage(NestedList)

NestedMap = _reflection.GeneratedProtocolMessageType('NestedMap', (_message.Message,), {

  'MyStringSimpleMapEntry' : _reflection.GeneratedProtocolMessageType('MyStringSimpleMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _NESTEDMAP_MYSTRINGSIMPLEMAPENTRY,
    '__module__' : 'sandbox.test.test_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.NestedMap.MyStringSimpleMapEntry)
    })
  ,

  'MyInt32SimpleMapEntry' : _reflection.GeneratedProtocolMessageType('MyInt32SimpleMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _NESTEDMAP_MYINT32SIMPLEMAPENTRY,
    '__module__' : 'sandbox.test.test_pb2'
    # @@protoc_insertion_point(class_scope:sandbox.test.NestedMap.MyInt32SimpleMapEntry)
    })
  ,
  'DESCRIPTOR' : _NESTEDMAP,
  '__module__' : 'sandbox.test.test_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.NestedMap)
  })
_sym_db.RegisterMessage(NestedMap)
_sym_db.RegisterMessage(NestedMap.MyStringSimpleMapEntry)
_sym_db.RegisterMessage(NestedMap.MyInt32SimpleMapEntry)

VeryNestedDude = _reflection.GeneratedProtocolMessageType('VeryNestedDude', (_message.Message,), {
  'DESCRIPTOR' : _VERYNESTEDDUDE,
  '__module__' : 'sandbox.test.test_pb2'
  # @@protoc_insertion_point(class_scope:sandbox.test.VeryNestedDude)
  })
_sym_db.RegisterMessage(VeryNestedDude)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SIMPLEMAP_MYSTRINGMAPENTRY._options = None
  _SIMPLEMAP_MYSTRINGMAPENTRY._serialized_options = b'8\001'
  _SIMPLEMAP_MYINT32MAPENTRY._options = None
  _SIMPLEMAP_MYINT32MAPENTRY._serialized_options = b'8\001'
  _SIMPLEMAP_MYINT64MAPENTRY._options = None
  _SIMPLEMAP_MYINT64MAPENTRY._serialized_options = b'8\001'
  _SIMPLEMAP_MYUINT32MAPENTRY._options = None
  _SIMPLEMAP_MYUINT32MAPENTRY._serialized_options = b'8\001'
  _SIMPLEMAP_MYUINT64MAPENTRY._options = None
  _SIMPLEMAP_MYUINT64MAPENTRY._serialized_options = b'8\001'
  _SIMPLEMAP_MYSINT32MAPENTRY._options = None
  _SIMPLEMAP_MYSINT32MAPENTRY._serialized_options = b'8\001'
  _SIMPLEMAP_MYSINT64MAPENTRY._options = None
  _SIMPLEMAP_MYSINT64MAPENTRY._serialized_options = b'8\001'
  _SIMPLEMAP_MYFIXED32MAPENTRY._options = None
  _SIMPLEMAP_MYFIXED32MAPENTRY._serialized_options = b'8\001'
  _SIMPLEMAP_MYFIXED64MAPENTRY._options = None
  _SIMPLEMAP_MYFIXED64MAPENTRY._serialized_options = b'8\001'
  _SIMPLEMAP_MYSFIXED32MAPENTRY._options = None
  _SIMPLEMAP_MYSFIXED32MAPENTRY._serialized_options = b'8\001'
  _SIMPLEMAP_MYSFIXED64MAPENTRY._options = None
  _SIMPLEMAP_MYSFIXED64MAPENTRY._serialized_options = b'8\001'
  _SIMPLEMAP_MYBOOLMAPENTRY._options = None
  _SIMPLEMAP_MYBOOLMAPENTRY._serialized_options = b'8\001'
  _NESTEDMAP_MYSTRINGSIMPLEMAPENTRY._options = None
  _NESTEDMAP_MYSTRINGSIMPLEMAPENTRY._serialized_options = b'8\001'
  _NESTEDMAP_MYINT32SIMPLEMAPENTRY._options = None
  _NESTEDMAP_MYINT32SIMPLEMAPENTRY._serialized_options = b'8\001'
  _SIMPLE._serialized_start=75
  _SIMPLE._serialized_end=368
  _SIMPLELIST._serialized_start=371
  _SIMPLELIST._serialized_end=743
  _SIMPLEMAP._serialized_start=746
  _SIMPLEMAP._serialized_end=2167
  _SIMPLEMAP_MYSTRINGMAPENTRY._serialized_start=1543
  _SIMPLEMAP_MYSTRINGMAPENTRY._serialized_end=1593
  _SIMPLEMAP_MYINT32MAPENTRY._serialized_start=1595
  _SIMPLEMAP_MYINT32MAPENTRY._serialized_end=1644
  _SIMPLEMAP_MYINT64MAPENTRY._serialized_start=1646
  _SIMPLEMAP_MYINT64MAPENTRY._serialized_end=1695
  _SIMPLEMAP_MYUINT32MAPENTRY._serialized_start=1697
  _SIMPLEMAP_MYUINT32MAPENTRY._serialized_end=1747
  _SIMPLEMAP_MYUINT64MAPENTRY._serialized_start=1749
  _SIMPLEMAP_MYUINT64MAPENTRY._serialized_end=1799
  _SIMPLEMAP_MYSINT32MAPENTRY._serialized_start=1801
  _SIMPLEMAP_MYSINT32MAPENTRY._serialized_end=1851
  _SIMPLEMAP_MYSINT64MAPENTRY._serialized_start=1853
  _SIMPLEMAP_MYSINT64MAPENTRY._serialized_end=1903
  _SIMPLEMAP_MYFIXED32MAPENTRY._serialized_start=1905
  _SIMPLEMAP_MYFIXED32MAPENTRY._serialized_end=1956
  _SIMPLEMAP_MYFIXED64MAPENTRY._serialized_start=1958
  _SIMPLEMAP_MYFIXED64MAPENTRY._serialized_end=2009
  _SIMPLEMAP_MYSFIXED32MAPENTRY._serialized_start=2011
  _SIMPLEMAP_MYSFIXED32MAPENTRY._serialized_end=2063
  _SIMPLEMAP_MYSFIXED64MAPENTRY._serialized_start=2065
  _SIMPLEMAP_MYSFIXED64MAPENTRY._serialized_end=2117
  _SIMPLEMAP_MYBOOLMAPENTRY._serialized_start=2119
  _SIMPLEMAP_MYBOOLMAPENTRY._serialized_end=2167
  _SIMPLETIMESTAMP._serialized_start=2169
  _SIMPLETIMESTAMP._serialized_end=2236
  _NESTEDDUDE._serialized_start=2238
  _NESTEDDUDE._serialized_end=2291
  _NESTEDLIST._serialized_start=2293
  _NESTEDLIST._serialized_end=2351
  _NESTEDMAP._serialized_start=2354
  _NESTEDMAP._serialized_end=2678
  _NESTEDMAP_MYSTRINGSIMPLEMAPENTRY._serialized_start=2521
  _NESTEDMAP_MYSTRINGSIMPLEMAPENTRY._serialized_end=2599
  _NESTEDMAP_MYINT32SIMPLEMAPENTRY._serialized_start=2601
  _NESTEDMAP_MYINT32SIMPLEMAPENTRY._serialized_end=2678
  _VERYNESTEDDUDE._serialized_start=2681
  _VERYNESTEDDUDE._serialized_end=2851
# @@protoc_insertion_point(module_scope)
