# md5: 4ff033d329418d1593f94de4752cb0e2
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.delta_pb2
# Generated at: 2022-06-26T12:07:56.402593
from __future__ import annotations
__all__ = [
    'DeltaMessage',
]
import dataclasses
import datetime
import enum
from typing import *
from protoplasm.casting import dictators
from protoplasm import plasm
from sandbox.test import beta_dc as sandbox__test__beta_dc

from sandbox.test import delta_pb2 as pb2

import logging
log = logging.getLogger(__name__)


@dataclasses.dataclass
class DeltaMessage(plasm.DataclassBase):
    __proto_cls__ = pb2.DeltaMessage
    my_string: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})
    my_number: int = dataclasses.field(default=0, metadata={'dictator': dictators.BaseDictator})
    my_level_three_message: sandbox__test__beta_dc.BetaMessage = dataclasses.field(default=None, metadata={'dictator': dictators.BaseDictator, 'is_obj': True})


