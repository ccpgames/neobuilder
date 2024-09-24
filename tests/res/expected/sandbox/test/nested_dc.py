# md5: 45f4470368efec2e672f0c2848171fe4
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.nested_pb2
# Generated at: 2022-06-26T12:07:56.420632
from __future__ import annotations
__all__ = [
    'OuterMessage',
]
import dataclasses
import datetime
import enum
import typing
from protoplasm.casting import dictators
from protoplasm import plasm

from sandbox.test import nested_pb2 as pb2

import logging
log = logging.getLogger(__name__)


@dataclasses.dataclass
class OuterMessage(plasm.DataclassBase):
    __proto_cls__ = pb2.OuterMessage

    @dataclasses.dataclass
    class InnerMessage(plasm.DataclassBase):
        __proto_cls__ = pb2.OuterMessage.InnerMessage
        my_inner_int: int = dataclasses.field(default=0, metadata={'dictator': dictators.BaseDictator})
        my_inner_string: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})

    my_int: int = dataclasses.field(default=0, metadata={'dictator': dictators.BaseDictator})
    my_string: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})
    my_message: OuterMessage.InnerMessage = dataclasses.field(default=None, metadata={'dictator': dictators.BaseDictator, 'is_obj': True})


