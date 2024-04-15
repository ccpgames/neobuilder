# md5: 68641330b7b31a917289f2133c188bdd
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.illnamedfields_pb2
# Generated at: 2022-06-26T12:07:56.407595
from __future__ import annotations
__all__ = [
    'BadNames',
]
import dataclasses
import datetime
import enum
from typing import *
from protoplasm.casting import dictators
from protoplasm import plasm

from sandbox.test import illnamedfields_pb2 as pb2

import logging
log = logging.getLogger(__name__)


@dataclasses.dataclass
class BadNames(plasm.DataclassBase):
    __proto_cls__ = pb2.BadNames
    False_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'False'})
    None_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'None'})
    True_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'True'})
    and_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'and'})
    as_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'as'})
    assert_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'assert'})
    async_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'async'})
    await_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'await'})
    break_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'break'})
    class_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'class'})
    continue_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'continue'})
    def_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'def'})
    del_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'del'})
    elif_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'elif'})
    else_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'else'})
    except_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'except'})
    finally_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'finally'})
    for_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'for'})
    from_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'from'})
    global_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'global'})
    if_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'if'})
    import_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'import'})
    in_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'in'})
    is_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'is'})
    lambda_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'lambda'})
    nonlocal_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'nonlocal'})
    not_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'not'})
    or_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'or'})
    pass_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'pass'})
    raise_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'raise'})
    return_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'return'})
    try_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'try'})
    while_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'while'})
    with_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'with'})
    yield_: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator, 'pb_name': 'yield'})


