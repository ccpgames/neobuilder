# md5: 853ef53413c3270f9b6991c4d82434b1
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.alpha_pb2
# Generated at: 2022-06-26T12:07:56.393597
from __future__ import annotations
__all__ = [
    'AlphaMessage',
]
import dataclasses
import datetime
import enum
from typing import *
from protoplasm.casting import dictators
from protoplasm import plasm

from sandbox.test import alpha_pb2 as pb2

import logging
log = logging.getLogger(__name__)


@dataclasses.dataclass
class AlphaMessage(plasm.DataclassBase):
    __proto_cls__ = pb2.AlphaMessage
    my_string: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})
    my_number: int = dataclasses.field(default=0, metadata={'dictator': dictators.BaseDictator})


