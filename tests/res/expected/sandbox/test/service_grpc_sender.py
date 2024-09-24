# md5: 026a46fb6c145bf15a49ca16c1ba5842
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.service_pb2
# Generated at: 2022-06-26T12:07:56.446592
from __future__ import annotations
__all__ = [
    'SimpleService',
    'Math',
]
import datetime
import typing
from protoplasm import plasm
from sandbox.test import service_dc as dc
from sandbox.test import service_pb2_grpc as pb2_grpc
from sandbox.test.service_api import *

if typing.TYPE_CHECKING:
    from grpc import ChannelCredentials

import logging
log = logging.getLogger(__name__)


class SimpleService(plasm.BaseGrpcClientImplementation, SimpleServiceInterface):
    def __init__(self, grpc_host: str = 'localhost:50051', credentials: typing.Optional[typing.Union[bool, 'ChannelCredentials']] = None, options: typing.Optional[typing.Dict] = None, *args, **kwargs):
        super().__init__(pb2_grpc.SimpleServiceStub, grpc_host, credentials, options, *args, **kwargs)

    def hello(self, greeting: str = None) -> str:
        return self._forward_to_grpc(dc.HelloRequest, self.stub.Hello, greeting)

    def nested_hello(self, my_message: dc.GreetingMessage = None) -> dc.GreetingMessage:
        return self._forward_to_grpc(dc.NestedHelloRequest, self.stub.NestedHello, my_message)

    def empty_hello(self) -> typing.NoReturn:
        return self._forward_to_grpc(dc.EmptyHelloRequest, self.stub.EmptyHello)

class Math(plasm.BaseGrpcClientImplementation, MathInterface):
    def __init__(self, grpc_host: str = 'localhost:50051', credentials: typing.Optional[typing.Union[bool, 'ChannelCredentials']] = None, options: typing.Optional[typing.Dict] = None, *args, **kwargs):
        super().__init__(pb2_grpc.MathStub, grpc_host, credentials, options, *args, **kwargs)

    def add(self, x: int = None, y: int = None) -> int:
        return self._forward_to_grpc(dc.AddRequest, self.stub.Add, x, y)

    def subtract(self, x: int = None, y: int = None) -> int:
        return self._forward_to_grpc(dc.SubtractRequest, self.stub.Subtract, x, y)

    def integer_division(self, x: int = None, y: int = None) -> typing.Tuple[int, int]:
        return self._forward_to_grpc(dc.IntegerDivisionRequest, self.stub.IntegerDivision, x, y)
