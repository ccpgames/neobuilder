# md5: edb159e268d19272dbdd3b72b46988be
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.service_with_oneof_pb2
# Generated at: 2022-06-26T12:07:56.461630
__all__ = [
    'SimpleOneOfServiceGrpcServicer',
]
import datetime
import typing
from protoplasm import plasm
from sandbox.test import service_with_oneof_dc as dc
from sandbox.test import service_with_oneof_pb2 as pb2
from sandbox.test import service_with_oneof_pb2_grpc as pb2_grpc
if typing.TYPE_CHECKING:
    from grpc import ServicerContext
    from sandbox.test import service_with_oneof_api as api

import logging
log = logging.getLogger(__name__)


class SimpleOneOfServiceGrpcServicer(plasm.BaseGrpcServicer, pb2_grpc.SimpleOneOfServiceServicer):
    def __init__(self, implementation: 'api.SimpleOneOfServiceInterface'):
        super().__init__(implementation)

    def add_to_server(self, server):
        pb2_grpc.add_SimpleOneOfServiceServicer_to_server(self, server)

    def HelloAgain(self, request: dc.pb2.HelloAgainRequest, context: 'ServicerContext') -> dc.pb2.HelloAgainResponse:
        return self._forward_to_unary_unary_impl(dc.HelloAgainResponse, self.impl.hello_again, request, context)

