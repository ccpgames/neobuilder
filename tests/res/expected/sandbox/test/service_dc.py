# md5: 2b8fb1bd2c6830f8eb4de89f6d6c6389
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.service_pb2
# Generated at: 2022-06-26T12:07:56.440624
from __future__ import annotations
__all__ = [
    'HelloRequest',
    'HelloResponse',
    'GreetingMessage',
    'NestedHelloRequest',
    'NestedHelloResponse',
    'EmptyHelloRequest',
    'EmptyHelloResponse',
    'AddRequest',
    'AddResponse',
    'SubtractRequest',
    'SubtractResponse',
    'IntegerDivisionRequest',
    'IntegerDivisionResponse',
]
import dataclasses
import datetime
import enum
import typing
from protoplasm.casting import dictators
from protoplasm import plasm

from sandbox.test import service_pb2 as pb2

import logging
log = logging.getLogger(__name__)


@dataclasses.dataclass
class HelloRequest(plasm.DataclassBase):
    __proto_cls__ = pb2.HelloRequest
    greeting: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})


@dataclasses.dataclass
class HelloResponse(plasm.DataclassBase):
    __proto_cls__ = pb2.HelloResponse
    reply: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})


@dataclasses.dataclass
class GreetingMessage(plasm.DataclassBase):
    __proto_cls__ = pb2.GreetingMessage
    greeting: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})
    language: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})


@dataclasses.dataclass
class NestedHelloRequest(plasm.DataclassBase):
    __proto_cls__ = pb2.NestedHelloRequest
    my_message: GreetingMessage = dataclasses.field(default=None, metadata={'dictator': dictators.BaseDictator, 'is_obj': True})


@dataclasses.dataclass
class NestedHelloResponse(plasm.DataclassBase):
    __proto_cls__ = pb2.NestedHelloResponse
    my_reply: GreetingMessage = dataclasses.field(default=None, metadata={'dictator': dictators.BaseDictator, 'is_obj': True})


@dataclasses.dataclass
class EmptyHelloRequest(plasm.DataclassBase):
    __proto_cls__ = pb2.EmptyHelloRequest


@dataclasses.dataclass
class EmptyHelloResponse(plasm.DataclassBase):
    __proto_cls__ = pb2.EmptyHelloResponse


@dataclasses.dataclass
class AddRequest(plasm.DataclassBase):
    __proto_cls__ = pb2.AddRequest
    x: int = dataclasses.field(default=0, metadata={'dictator': dictators.LongDictator})
    y: int = dataclasses.field(default=0, metadata={'dictator': dictators.LongDictator})


@dataclasses.dataclass
class AddResponse(plasm.DataclassBase):
    __proto_cls__ = pb2.AddResponse
    result: int = dataclasses.field(default=0, metadata={'dictator': dictators.LongDictator})


@dataclasses.dataclass
class SubtractRequest(plasm.DataclassBase):
    __proto_cls__ = pb2.SubtractRequest
    x: int = dataclasses.field(default=0, metadata={'dictator': dictators.LongDictator})
    y: int = dataclasses.field(default=0, metadata={'dictator': dictators.LongDictator})


@dataclasses.dataclass
class SubtractResponse(plasm.DataclassBase):
    __proto_cls__ = pb2.SubtractResponse
    result: int = dataclasses.field(default=0, metadata={'dictator': dictators.LongDictator})


@dataclasses.dataclass
class IntegerDivisionRequest(plasm.DataclassBase):
    __proto_cls__ = pb2.IntegerDivisionRequest
    x: int = dataclasses.field(default=0, metadata={'dictator': dictators.LongDictator})
    y: int = dataclasses.field(default=0, metadata={'dictator': dictators.LongDictator})


@dataclasses.dataclass
class IntegerDivisionResponse(plasm.DataclassBase):
    __proto_cls__ = pb2.IntegerDivisionResponse
    result: int = dataclasses.field(default=0, metadata={'dictator': dictators.LongDictator})
    remainder: int = dataclasses.field(default=0, metadata={'dictator': dictators.LongDictator})


