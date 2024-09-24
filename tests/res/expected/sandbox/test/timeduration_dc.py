# md5: 2281e3171201e0ca9594e8e12c81cae4
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.timeduration_pb2
# Generated at: 2022-06-26T12:07:56.469591
from __future__ import annotations
__all__ = [
    'DurationMessage',
]
import dataclasses
import datetime
import enum
import typing
from protoplasm.casting import dictators
from protoplasm import plasm

from sandbox.test import timeduration_pb2 as pb2

import logging
log = logging.getLogger(__name__)


@dataclasses.dataclass
class DurationMessage(plasm.DataclassBase):
    __proto_cls__ = pb2.DurationMessage
    my_duration: datetime.timedelta = dataclasses.field(default=None, metadata={'dictator': dictators.DurationDictator})
    my_duration_list: typing.List[datetime.timedelta] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.DurationDictator, 'is_list': True})
    my_duration_map: typing.Dict[str, datetime.timedelta] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.DurationDictator, 'is_map': True})


