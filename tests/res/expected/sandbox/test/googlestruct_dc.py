# md5: 7b314132a19d0dc0845666a4261161ed
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.googlestruct_pb2
# Generated at: 2024-09-19T12:21:16.292717
from __future__ import annotations
__all__ = [
    'StructMessage',
]
import dataclasses
import datetime
import enum
import typing
from protoplasm.casting import dictators
from protoplasm import plasm

from sandbox.test import googlestruct_pb2 as pb2

import logging
log = logging.getLogger(__name__)


@dataclasses.dataclass
class StructMessage(plasm.DataclassBase):
    __proto_cls__ = pb2.StructMessage
    my_struct: typing.Dict[str, typing.Any] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.StructDictator, 'is_struct': True})

