# md5: cf35852977322845897261ddc280159c
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.service_with_oneof_pb2
# Generated at: 2022-06-26T12:07:56.458593
from __future__ import annotations
__all__ = [
    'HelloAgainRequest',
    'HelloAgainResponse',
]
import dataclasses
import datetime
import enum
from typing import *
from protoplasm.casting import dictators
from protoplasm import plasm

from sandbox.test import service_with_oneof_pb2 as pb2

import logging
log = logging.getLogger(__name__)


@dataclasses.dataclass
class HelloAgainRequest(plasm.DataclassBase):
    __proto_cls__ = pb2.HelloAgainRequest
    greeting: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})


@dataclasses.dataclass
class HelloAgainResponse(plasm.DataclassBase):
    __proto_cls__ = pb2.HelloAgainResponse
    response: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})
    number: int = dataclasses.field(default=0, metadata={'dictator': dictators.BaseDictator})


