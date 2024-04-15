# md5: cbf0d11d25796c2acb126ee6935f18c3
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.illnamedservice_pb2
# Generated at: 2022-06-26T12:07:56.411591
from __future__ import annotations
__all__ = [
    'MyAction',
    'MyConsequence',
]
import dataclasses
import datetime
import enum
from typing import *
from protoplasm.casting import dictators
from protoplasm import plasm

from sandbox.test import illnamedservice_pb2 as pb2

import logging
log = logging.getLogger(__name__)


@dataclasses.dataclass
class MyAction(plasm.DataclassBase):
    __proto_cls__ = pb2.MyAction
    foo: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})


@dataclasses.dataclass
class MyConsequence(plasm.DataclassBase):
    __proto_cls__ = pb2.MyConsequence
    bar: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})


