# md5: 0fc723c3a79ef19e1d9ca49c8f6c71bb
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.illnamedservice_pb2
# Generated at: 2022-06-26T12:07:56.412592
__all__ = [
    'ServiceWithBadRequestNamesInterface',
]
import datetime
from typing import *
from protoplasm import plasm

from sandbox.test import illnamedservice_dc as dc
from sandbox.test.illnamedservice_grpc_receiver import ServiceWithBadRequestNamesGrpcServicer

import logging
log = logging.getLogger(__name__)


class ServiceWithBadRequestNamesInterface:
    __servicer_cls__ = ServiceWithBadRequestNamesGrpcServicer

    def do_something(self, foo: str = None) -> str:
        raise plasm.Unimplemented()

