# md5: 40eddbb46ed790644f1be8bfac9e3530
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.rainbow_pb2
# Generated at: 2022-06-26T12:07:56.423635
from __future__ import annotations
__all__ = [
    'SubMessage',
    'RainbowMessage',
    'TimestampMessage',
    'BytesMessage',
    'AllTypes',
    'AllTypesList',
    'AllTypesMap',
    'AllTypesNestedMap',
]
import dataclasses
import datetime
import enum
from typing import *
from protoplasm.casting import dictators
from protoplasm import plasm

from sandbox.test import rainbow_pb2 as pb2

import logging
log = logging.getLogger(__name__)


@dataclasses.dataclass
class SubMessage(plasm.DataclassBase):
    __proto_cls__ = pb2.SubMessage
    foo: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})
    bar: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})


@dataclasses.dataclass
class RainbowMessage(plasm.DataclassBase):
    __proto_cls__ = pb2.RainbowMessage
    simple_field: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})
    message_field: SubMessage = dataclasses.field(default=None, metadata={'dictator': dictators.BaseDictator, 'is_obj': True})
    simple_list: List[str] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    message_list: List[SubMessage] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True, 'is_obj': True})
    simple_map: Dict[str, str] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})
    message_map: Dict[str, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})


@dataclasses.dataclass
class TimestampMessage(plasm.DataclassBase):
    __proto_cls__ = pb2.TimestampMessage
    my_timestamp: datetime.datetime = dataclasses.field(default=None, metadata={'dictator': dictators.TimestampDictator})
    my_timestamp_list: List[datetime.datetime] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.TimestampDictator, 'is_list': True})
    my_timestamp_map: Dict[str, datetime.datetime] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.TimestampDictator, 'is_map': True})


@dataclasses.dataclass
class BytesMessage(plasm.DataclassBase):
    __proto_cls__ = pb2.BytesMessage
    my_bytes: bytes = dataclasses.field(default=b'', metadata={'dictator': dictators.ByteDictator})
    my_bytes_list: List[bytes] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.ByteDictator, 'is_list': True})
    my_bytes_map: Dict[str, bytes] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.ByteDictator, 'is_map': True})


@dataclasses.dataclass
class AllTypes(plasm.DataclassBase):
    __proto_cls__ = pb2.AllTypes
    my_string: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})
    my_float: float = dataclasses.field(default=0.0, metadata={'dictator': dictators.BaseDictator})
    my_double: float = dataclasses.field(default=0.0, metadata={'dictator': dictators.BaseDictator})
    my_int32: int = dataclasses.field(default=0, metadata={'dictator': dictators.BaseDictator})
    my_int64: int = dataclasses.field(default=0, metadata={'dictator': dictators.LongDictator})
    my_uint32: int = dataclasses.field(default=0, metadata={'dictator': dictators.BaseDictator})
    my_uint64: int = dataclasses.field(default=0, metadata={'dictator': dictators.LongDictator})
    my_sint32: int = dataclasses.field(default=0, metadata={'dictator': dictators.BaseDictator})
    my_sint64: int = dataclasses.field(default=0, metadata={'dictator': dictators.LongDictator})
    my_fixed32: int = dataclasses.field(default=0, metadata={'dictator': dictators.BaseDictator})
    my_fixed64: int = dataclasses.field(default=0, metadata={'dictator': dictators.LongDictator})
    my_sfixed32: int = dataclasses.field(default=0, metadata={'dictator': dictators.BaseDictator})
    my_sfixed64: int = dataclasses.field(default=0, metadata={'dictator': dictators.LongDictator})
    my_bool: bool = dataclasses.field(default=False, metadata={'dictator': dictators.BaseDictator})
    my_bytes: bytes = dataclasses.field(default=b'', metadata={'dictator': dictators.ByteDictator})


@dataclasses.dataclass
class AllTypesList(plasm.DataclassBase):
    __proto_cls__ = pb2.AllTypesList
    my_string_list: List[str] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_float_list: List[float] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_double_list: List[float] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_int32_list: List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_int64_list: List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.LongDictator, 'is_list': True})
    my_uint32_list: List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_uint64_list: List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.LongDictator, 'is_list': True})
    my_sint32_list: List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_sint64_list: List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.LongDictator, 'is_list': True})
    my_fixed32_list: List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_fixed64_list: List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.LongDictator, 'is_list': True})
    my_sfixed32_list: List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_sfixed64_list: List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.LongDictator, 'is_list': True})
    my_bool_list: List[bool] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_bytes_list: List[bytes] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.ByteDictator, 'is_list': True})


@dataclasses.dataclass
class AllTypesMap(plasm.DataclassBase):
    __proto_cls__ = pb2.AllTypesMap
    my_string_map: Dict[str, str] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})
    my_int32_map: Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})
    my_int64_map: Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.LongDictator, 'is_map': True})
    my_uint32_map: Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})
    my_uint64_map: Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.LongDictator, 'is_map': True})
    my_sint32_map: Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})
    my_sint64_map: Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.LongDictator, 'is_map': True})
    my_fixed32_map: Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})
    my_fixed64_map: Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.LongDictator, 'is_map': True})
    my_sfixed32_map: Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})
    my_sfixed64_map: Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.LongDictator, 'is_map': True})
    my_bool_map: Dict[bool, bool] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})


@dataclasses.dataclass
class AllTypesNestedMap(plasm.DataclassBase):
    __proto_cls__ = pb2.AllTypesNestedMap
    my_string_map: Dict[str, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_int32_map: Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_int64_map: Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_uint32_map: Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_uint64_map: Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_sint32_map: Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_sint64_map: Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_fixed32_map: Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_fixed64_map: Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_sfixed32_map: Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_sfixed64_map: Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_bool_map: Dict[bool, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})


