# md5: a3eb53581e8a4a083d3f6540b758d8e3
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.interfaceonly_pb2
# Generated at: 2022-06-26T12:07:56.418593
from __future__ import annotations
__all__ = [
    'OnHelloRequest',
    'OnHelloResponse',
]
import dataclasses
import datetime
import enum
from typing import *
from protoplasm.casting import dictators
from protoplasm import plasm

from sandbox.test import interfaceonly_pb2 as pb2

import logging
log = logging.getLogger(__name__)


@dataclasses.dataclass
class OnHelloRequest(plasm.DataclassBase):
    __proto_cls__ = pb2.OnHelloRequest
    greeting: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})


@dataclasses.dataclass
class OnHelloResponse(plasm.DataclassBase):
    __proto_cls__ = pb2.OnHelloResponse
    reply: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})


