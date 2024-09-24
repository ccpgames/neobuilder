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
import typing
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
    simple_list: typing.List[str] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    message_list: typing.List[SubMessage] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True, 'is_obj': True})
    simple_map: typing.Dict[str, str] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})
    message_map: typing.Dict[str, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})


@dataclasses.dataclass
class TimestampMessage(plasm.DataclassBase):
    __proto_cls__ = pb2.TimestampMessage
    my_timestamp: datetime.datetime = dataclasses.field(default=None, metadata={'dictator': dictators.TimestampDictator})
    my_timestamp_list: typing.List[datetime.datetime] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.TimestampDictator, 'is_list': True})
    my_timestamp_map: typing.Dict[str, datetime.datetime] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.TimestampDictator, 'is_map': True})


@dataclasses.dataclass
class BytesMessage(plasm.DataclassBase):
    __proto_cls__ = pb2.BytesMessage
    my_bytes: bytes = dataclasses.field(default=b'', metadata={'dictator': dictators.ByteDictator})
    my_bytes_list: typing.List[bytes] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.ByteDictator, 'is_list': True})
    my_bytes_map: typing.Dict[str, bytes] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.ByteDictator, 'is_map': True})


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
    my_string_list: typing.List[str] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_float_list: typing.List[float] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_double_list: typing.List[float] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_int32_list: typing.List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_int64_list: typing.List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.LongDictator, 'is_list': True})
    my_uint32_list: typing.List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_uint64_list: typing.List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.LongDictator, 'is_list': True})
    my_sint32_list: typing.List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_sint64_list: typing.List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.LongDictator, 'is_list': True})
    my_fixed32_list: typing.List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_fixed64_list: typing.List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.LongDictator, 'is_list': True})
    my_sfixed32_list: typing.List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_sfixed64_list: typing.List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.LongDictator, 'is_list': True})
    my_bool_list: typing.List[bool] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_bytes_list: typing.List[bytes] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.ByteDictator, 'is_list': True})


@dataclasses.dataclass
class AllTypesMap(plasm.DataclassBase):
    __proto_cls__ = pb2.AllTypesMap
    my_string_map: typing.Dict[str, str] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})
    my_int32_map: typing.Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})
    my_int64_map: typing.Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.LongDictator, 'is_map': True})
    my_uint32_map: typing.Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})
    my_uint64_map: typing.Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.LongDictator, 'is_map': True})
    my_sint32_map: typing.Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})
    my_sint64_map: typing.Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.LongDictator, 'is_map': True})
    my_fixed32_map: typing.Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})
    my_fixed64_map: typing.Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.LongDictator, 'is_map': True})
    my_sfixed32_map: typing.Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})
    my_sfixed64_map: typing.Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.LongDictator, 'is_map': True})
    my_bool_map: typing.Dict[bool, bool] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})


@dataclasses.dataclass
class AllTypesNestedMap(plasm.DataclassBase):
    __proto_cls__ = pb2.AllTypesNestedMap
    my_string_map: typing.Dict[str, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_int32_map: typing.Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_int64_map: typing.Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_uint32_map: typing.Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_uint64_map: typing.Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_sint32_map: typing.Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_sint64_map: typing.Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_fixed32_map: typing.Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_fixed64_map: typing.Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_sfixed32_map: typing.Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_sfixed64_map: typing.Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_bool_map: typing.Dict[bool, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})


