# md5: b50bcd0966cde4aea5b565902c2da6a9
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.enums_pb2
# Generated at: 2022-06-26T12:07:56.404593
from __future__ import annotations
__all__ = [
    'ExternalEnum',
    'ExternalAliasEnum',
    'WithExternalEnum',
    'WithInternalEnum',
    'WithInternalEnumAfter',
]
import dataclasses
import datetime
import enum
import typing
from protoplasm.casting import dictators
from protoplasm import plasm

from sandbox.test import enums_pb2 as pb2

import logging
log = logging.getLogger(__name__)


class ExternalEnum(enum.IntEnum):
    __proto_cls__ = pb2.ExternalEnum
    THREE = 3
    TWO = 2
    ONE = 1
    ZERO_AND_DEFAULT = 0


THREE = ExternalEnum(3)
TWO = ExternalEnum(2)
ONE = ExternalEnum(1)
ZERO_AND_DEFAULT = ExternalEnum(0)


class ExternalAliasEnum(enum.IntEnum):
    __proto_cls__ = pb2.ExternalAliasEnum
    SEX = 3
    SIX = 3
    FIMM = 2
    FIVE = 2
    FJORIR = 1
    FOUR = 1
    ZERO = 0
    DEFAULT = 0


SEX = ExternalAliasEnum(3)
SIX = ExternalAliasEnum(3)
FIMM = ExternalAliasEnum(2)
FIVE = ExternalAliasEnum(2)
FJORIR = ExternalAliasEnum(1)
FOUR = ExternalAliasEnum(1)
ZERO = ExternalAliasEnum(0)
DEFAULT = ExternalAliasEnum(0)


@dataclasses.dataclass
class WithExternalEnum(plasm.DataclassBase):
    __proto_cls__ = pb2.WithExternalEnum
    my_enum: ExternalEnum = dataclasses.field(default=0, metadata={'dictator': dictators.EnumDictator, 'is_enum': True})
    my_alias_enum: ExternalAliasEnum = dataclasses.field(default=0, metadata={'dictator': dictators.EnumDictator, 'is_enum': True})
    my_enum_list: typing.List[ExternalEnum] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.EnumDictator, 'is_list': True, 'is_enum': True})
    my_alias_enum_list: typing.List[ExternalAliasEnum] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.EnumDictator, 'is_list': True, 'is_enum': True})
    my_enum_map: typing.Dict[str, ExternalEnum] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.EnumDictator, 'is_map': True, 'is_enum': True})
    my_alias_enum_map: typing.Dict[str, ExternalAliasEnum] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.EnumDictator, 'is_map': True, 'is_enum': True})


@dataclasses.dataclass
class WithInternalEnum(plasm.DataclassBase):
    __proto_cls__ = pb2.WithInternalEnum

    class InternalEnum(enum.IntEnum):
        __proto_cls__ = pb2.WithInternalEnum.InternalEnum
        SIX = 6
        FIVE = 5
        FOUR = 4
        ZERO_AND_DEFAULT = 0

    SIX = InternalEnum(6)
    FIVE = InternalEnum(5)
    FOUR = InternalEnum(4)
    ZERO_AND_DEFAULT = InternalEnum(0)

    class InternalAliasEnum(enum.IntEnum):
        __proto_cls__ = pb2.WithInternalEnum.InternalAliasEnum
        NIU = 9
        NINE = 9
        ATTA = 8
        EIGHT = 8
        SJO = 7
        SEVEN = 7
        ZERO = 0
        DEFAULT = 0

    NIU = InternalAliasEnum(9)
    NINE = InternalAliasEnum(9)
    ATTA = InternalAliasEnum(8)
    EIGHT = InternalAliasEnum(8)
    SJO = InternalAliasEnum(7)
    SEVEN = InternalAliasEnum(7)
    ZERO = InternalAliasEnum(0)
    DEFAULT = InternalAliasEnum(0)

    my_internal_enum: WithInternalEnum.InternalEnum = dataclasses.field(default=0, metadata={'dictator': dictators.EnumDictator, 'is_enum': True})
    my_internal_alias_enum: WithInternalEnum.InternalAliasEnum = dataclasses.field(default=0, metadata={'dictator': dictators.EnumDictator, 'is_enum': True})
    my_internal_enum_list: typing.List[WithInternalEnum.InternalEnum] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.EnumDictator, 'is_list': True, 'is_enum': True})
    my_internal_alias_enum_list: typing.List[WithInternalEnum.InternalAliasEnum] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.EnumDictator, 'is_list': True, 'is_enum': True})
    my_internal_enum_map: typing.Dict[str, WithInternalEnum.InternalEnum] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.EnumDictator, 'is_map': True, 'is_enum': True})
    my_internal_alias_enum_map: typing.Dict[str, WithInternalEnum.InternalAliasEnum] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.EnumDictator, 'is_map': True, 'is_enum': True})


@dataclasses.dataclass
class WithInternalEnumAfter(plasm.DataclassBase):
    __proto_cls__ = pb2.WithInternalEnumAfter

    class InternalEnumAfter(enum.IntEnum):
        __proto_cls__ = pb2.WithInternalEnumAfter.InternalEnumAfter
        AFTER_SIX = 6
        AFTER_FIVE = 5
        AFTER_FOUR = 4
        AFTER_ZERO_AND_DEFAULT = 0

    AFTER_SIX = InternalEnumAfter(6)
    AFTER_FIVE = InternalEnumAfter(5)
    AFTER_FOUR = InternalEnumAfter(4)
    AFTER_ZERO_AND_DEFAULT = InternalEnumAfter(0)

    my_internal_enum_after: WithInternalEnumAfter.InternalEnumAfter = dataclasses.field(default=0, metadata={'dictator': dictators.EnumDictator, 'is_enum': True})


