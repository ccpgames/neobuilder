# md5: ca96aa737e8e51221f6e4b437621d84f
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.service_pb2
# Generated at: 2022-06-26T12:07:56.445593
__all__ = [
    'SimpleServiceGrpcServicer',
    'MathGrpcServicer',
]
import datetime
import typing
from protoplasm import plasm

from sandbox.test import service_dc as dc
from sandbox.test import service_pb2 as pb2
from sandbox.test import service_pb2_grpc as pb2_grpc
if typing.TYPE_CHECKING:
    from grpc import ServicerContext
    from sandbox.test import service_api as api

import logging
log = logging.getLogger(__name__)


class SimpleServiceGrpcServicer(plasm.BaseGrpcServicer, pb2_grpc.SimpleServiceServicer):
    def __init__(self, implementation: 'api.SimpleServiceInterface'):
        super().__init__(implementation)

    def add_to_server(self, server):
        pb2_grpc.add_SimpleServiceServicer_to_server(self, server)

    def Hello(self, request: dc.pb2.HelloRequest, context: 'ServicerContext') -> dc.pb2.HelloResponse:
        return self._forward_to_unary_unary_impl(dc.HelloResponse, self.impl.hello, request, context)

    def NestedHello(self, request: dc.pb2.NestedHelloRequest, context: 'ServicerContext') -> dc.pb2.NestedHelloResponse:
        return self._forward_to_unary_unary_impl(dc.NestedHelloResponse, self.impl.nested_hello, request, context)

    def EmptyHello(self, request: dc.pb2.EmptyHelloRequest, context: 'ServicerContext') -> dc.pb2.EmptyHelloResponse:
        return self._forward_to_unary_unary_impl(dc.EmptyHelloResponse, self.impl.empty_hello, request, context)


class MathGrpcServicer(plasm.BaseGrpcServicer, pb2_grpc.MathServicer):
    def __init__(self, implementation: 'api.MathInterface'):
        super().__init__(implementation)

    def add_to_server(self, server):
        pb2_grpc.add_MathServicer_to_server(self, server)

    def Add(self, request: dc.pb2.AddRequest, context: 'ServicerContext') -> dc.pb2.AddResponse:
        return self._forward_to_unary_unary_impl(dc.AddResponse, self.impl.add, request, context)

    def Subtract(self, request: dc.pb2.SubtractRequest, context: 'ServicerContext') -> dc.pb2.SubtractResponse:
        return self._forward_to_unary_unary_impl(dc.SubtractResponse, self.impl.subtract, request, context)

    def IntegerDivision(self, request: dc.pb2.IntegerDivisionRequest, context: 'ServicerContext') -> dc.pb2.IntegerDivisionResponse:
        return self._forward_to_unary_unary_impl(dc.IntegerDivisionResponse, self.impl.integer_division, request, context)

