# md5: a56cb7632308915eaed36c02e802d674
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.imported_enum_pb2
# Generated at: 2022-06-26T12:07:56.416594
from __future__ import annotations
__all__ = [
    'MessageWithImportedEnum',
]
import dataclasses
import datetime
import enum
import typing
from protoplasm.casting import dictators
from protoplasm import plasm
from sandbox.test import enums_dc as sandbox__test__enums_dc

from sandbox.test import imported_enum_pb2 as pb2

import logging
log = logging.getLogger(__name__)


@dataclasses.dataclass
class MessageWithImportedEnum(plasm.DataclassBase):
    __proto_cls__ = pb2.MessageWithImportedEnum
    my_external_enum: sandbox__test__enums_dc.ExternalEnum = dataclasses.field(default=0, metadata={'dictator': dictators.EnumDictator, 'is_enum': True})


