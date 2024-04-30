# md5: 0b1abb509cb3481eb0711515a9b1e789
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.service_pb2
# Generated at: 2022-06-26T12:07:56.442631
__all__ = [
    'SimpleServiceInterface',
    'MathInterface',
]
import datetime
from typing import *
from protoplasm import plasm

from sandbox.test import service_dc as dc
from sandbox.test.service_grpc_receiver import MathGrpcServicer
from sandbox.test.service_grpc_receiver import SimpleServiceGrpcServicer

import logging
log = logging.getLogger(__name__)


class SimpleServiceInterface:
    __servicer_cls__ = SimpleServiceGrpcServicer

    def hello(self, greeting: str = None) -> str:
        raise plasm.Unimplemented()

    def nested_hello(self, my_message: dc.GreetingMessage = None) -> dc.GreetingMessage:
        raise plasm.Unimplemented()

    def empty_hello(self) -> NoReturn:
        raise plasm.Unimplemented()


class MathInterface:
    __servicer_cls__ = MathGrpcServicer

    def add(self, x: int = None, y: int = None) -> int:
        raise plasm.Unimplemented()

    def subtract(self, x: int = None, y: int = None) -> int:
        raise plasm.Unimplemented()

    def integer_division(self, x: int = None, y: int = None) -> Tuple[int, int]:
        raise plasm.Unimplemented()

