# md5: ddec0bc9e38cb44bae9e9522f9f0ec12
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.beta_pb2
# Generated at: 2022-06-26T12:07:56.397592
from __future__ import annotations
__all__ = [
    'BetaMessage',
]
import dataclasses
import datetime
import enum
import typing
from protoplasm.casting import dictators
from protoplasm import plasm
from sandbox.test import alpha_dc as sandbox__test__alpha_dc

from sandbox.test import beta_pb2 as pb2

import logging
log = logging.getLogger(__name__)


@dataclasses.dataclass
class BetaMessage(plasm.DataclassBase):
    __proto_cls__ = pb2.BetaMessage
    my_string: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})
    my_number: int = dataclasses.field(default=0, metadata={'dictator': dictators.BaseDictator})
    my_foreign_message: sandbox__test__alpha_dc.AlphaMessage = dataclasses.field(default=None, metadata={'dictator': dictators.BaseDictator, 'is_obj': True})


