# md5: 91abe191a0b6514ba09cc09c37068af7
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.anytest_pb2
# Generated at: 2022-06-26T12:07:56.395594
from __future__ import annotations
__all__ = [
    'AnyMessage',
]
import dataclasses
import datetime
import enum
import typing
from protoplasm.casting import dictators
from protoplasm import plasm

from sandbox.test import anytest_pb2 as pb2

import logging
log = logging.getLogger(__name__)


@dataclasses.dataclass
class AnyMessage(plasm.DataclassBase):
    __proto_cls__ = pb2.AnyMessage
    my_any: plasm.DataclassBase = dataclasses.field(default=None, metadata={'dictator': dictators.AnyDictator})
    my_any_list: typing.List[plasm.DataclassBase] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.AnyDictator, 'is_list': True})
    my_any_map: typing.Dict[str, plasm.DataclassBase] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.AnyDictator, 'is_map': True})


