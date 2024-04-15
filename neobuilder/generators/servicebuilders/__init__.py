from __future__ import annotations
from . import base
from ccptools.tpu import strimp
import typing

import logging
log = logging.getLogger(__name__)

_CACHE = {}


def get_builder_module(implementation_name: str):
    if implementation_name not in _CACHE:
        _CACHE[implementation_name] = strimp.get_module(f'{__package__}.{implementation_name}', logger=log, reraise=True)
    return _CACHE[implementation_name]


def get_module_builder(implementation_name: str) -> typing.Type[base.AbstractModuleBuilder]:
    return getattr(get_builder_module(implementation_name), 'ModuleBuilder')


def get_service_builder(implementation_name: str) -> typing.Type[base.AbstractServiceBuilder]:
    return getattr(get_builder_module(implementation_name), 'ServiceBuilder')


def get_method_builder(implementation_name: str) -> typing.Type[base.AbstractMethodBuilder]:
    return getattr(get_builder_module(implementation_name), 'MethodBuilder')
