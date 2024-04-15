# md5: 36a0fc95fe0d5f549c8ad3b75b87780d
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.clones_pb2
# Generated at: 2022-06-26T12:07:56.400593
from __future__ import annotations
__all__ = [
    'SubThing',
    'ThingOne',
    'ThingTwo',
]
import dataclasses
import datetime
import enum
from typing import *
from protoplasm.casting import dictators
from protoplasm import plasm

from sandbox.test import clones_pb2 as pb2

import logging
log = logging.getLogger(__name__)


@dataclasses.dataclass
class SubThing(plasm.DataclassBase):
    __proto_cls__ = pb2.SubThing
    foo: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})
    bar: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})


@dataclasses.dataclass
class ThingOne(plasm.DataclassBase):
    __proto_cls__ = pb2.ThingOne
    my_string: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})
    my_number: int = dataclasses.field(default=0, metadata={'dictator': dictators.BaseDictator})
    my_float: float = dataclasses.field(default=0.0, metadata={'dictator': dictators.BaseDictator})
    my_timestamp: datetime.datetime = dataclasses.field(default=None, metadata={'dictator': dictators.TimestampDictator})
    my_subthing: SubThing = dataclasses.field(default=None, metadata={'dictator': dictators.BaseDictator, 'is_obj': True})
    my_unique_string: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})


@dataclasses.dataclass
class ThingTwo(plasm.DataclassBase):
    __proto_cls__ = pb2.ThingTwo
    my_string: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})
    my_number: int = dataclasses.field(default=0, metadata={'dictator': dictators.BaseDictator})
    my_float: float = dataclasses.field(default=0.0, metadata={'dictator': dictators.BaseDictator})
    my_timestamp: datetime.datetime = dataclasses.field(default=None, metadata={'dictator': dictators.TimestampDictator})
    my_subthing: SubThing = dataclasses.field(default=None, metadata={'dictator': dictators.BaseDictator, 'is_obj': True})
    my_special_string: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})


