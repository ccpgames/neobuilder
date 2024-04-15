# md5: 6dbde48775c607b887fcca4af489ac5d
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.test_pb2
# Generated at: 2022-06-26T12:07:56.464593
from __future__ import annotations
__all__ = [
    'Simple',
    'SimpleList',
    'SimpleMap',
    'SimpleTimestamp',
    'NestedDude',
    'NestedList',
    'NestedMap',
    'VeryNestedDude',
]
import dataclasses
import datetime
import enum
from typing import *
from protoplasm.casting import dictators
from protoplasm import plasm

from sandbox.test import test_pb2 as pb2

import logging
log = logging.getLogger(__name__)


@dataclasses.dataclass
class Simple(plasm.DataclassBase):
    __proto_cls__ = pb2.Simple
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
class SimpleList(plasm.DataclassBase):
    __proto_cls__ = pb2.SimpleList
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
class SimpleMap(plasm.DataclassBase):
    __proto_cls__ = pb2.SimpleMap
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
class SimpleTimestamp(plasm.DataclassBase):
    __proto_cls__ = pb2.SimpleTimestamp
    my_timestamp: datetime.datetime = dataclasses.field(default=None, metadata={'dictator': dictators.TimestampDictator})


@dataclasses.dataclass
class NestedDude(plasm.DataclassBase):
    __proto_cls__ = pb2.NestedDude
    my_simple: Simple = dataclasses.field(default=None, metadata={'dictator': dictators.BaseDictator, 'is_obj': True})


@dataclasses.dataclass
class NestedList(plasm.DataclassBase):
    __proto_cls__ = pb2.NestedList
    my_simple_list: List[Simple] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True, 'is_obj': True})


@dataclasses.dataclass
class NestedMap(plasm.DataclassBase):
    __proto_cls__ = pb2.NestedMap
    my_string_simple_map: Dict[str, Simple] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_int32_simple_map: Dict[int, Simple] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})


@dataclasses.dataclass
class VeryNestedDude(plasm.DataclassBase):
    __proto_cls__ = pb2.VeryNestedDude
    my_nested_dude: NestedDude = dataclasses.field(default=None, metadata={'dictator': dictators.BaseDictator, 'is_obj': True})
    my_non_nested_simple: Simple = dataclasses.field(default=None, metadata={'dictator': dictators.BaseDictator, 'is_obj': True})
    my_list_of_lists: List[NestedList] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True, 'is_obj': True})


