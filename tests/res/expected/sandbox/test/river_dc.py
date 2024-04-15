# md5: 74423be271dc4064cc4641d57ab12f6e
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.river_pb2
# Generated at: 2022-06-26T12:07:56.431593
from __future__ import annotations
__all__ = [
    'ReverseMyShitRequest',
    'ReverseMyShitResponse',
    'TellMeAStoryRequest',
    'TellMeAStoryResponse',
    'MarcoPoloRequest',
    'MarcoPoloResponse',
    'GuessTheNumberRequest',
    'GuessTheNumberResponse',
]
import dataclasses
import datetime
import enum
from typing import *
from protoplasm.casting import dictators
from protoplasm import plasm

from sandbox.test import river_pb2 as pb2

import logging
log = logging.getLogger(__name__)


@dataclasses.dataclass
class ReverseMyShitRequest(plasm.DataclassBase):
    __proto_cls__ = pb2.ReverseMyShitRequest
    shit: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})


@dataclasses.dataclass
class ReverseMyShitResponse(plasm.DataclassBase):
    __proto_cls__ = pb2.ReverseMyShitResponse
    tihs: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})


@dataclasses.dataclass
class TellMeAStoryRequest(plasm.DataclassBase):
    __proto_cls__ = pb2.TellMeAStoryRequest
    story: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})


@dataclasses.dataclass
class TellMeAStoryResponse(plasm.DataclassBase):
    __proto_cls__ = pb2.TellMeAStoryResponse
    line: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})


@dataclasses.dataclass
class MarcoPoloRequest(plasm.DataclassBase):
    __proto_cls__ = pb2.MarcoPoloRequest
    question: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})


@dataclasses.dataclass
class MarcoPoloResponse(plasm.DataclassBase):
    __proto_cls__ = pb2.MarcoPoloResponse
    answer: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})


@dataclasses.dataclass
class GuessTheNumberRequest(plasm.DataclassBase):
    __proto_cls__ = pb2.GuessTheNumberRequest
    number: int = dataclasses.field(default=0, metadata={'dictator': dictators.BaseDictator})


@dataclasses.dataclass
class GuessTheNumberResponse(plasm.DataclassBase):
    __proto_cls__ = pb2.GuessTheNumberResponse
    did_i_win: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})


