# md5: 7377418bb08dfbedd5ca3dce8504c7cd
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.illnamedservice_pb2
# Generated at: 2022-06-26T12:07:56.414593
__all__ = [
    'ServiceWithBadRequestNamesGrpcServicer',
]
from typing import *
from protoplasm import plasm
from sandbox.test import illnamedservice_dc as dc
from sandbox.test import illnamedservice_pb2 as pb2
from sandbox.test import illnamedservice_pb2_grpc as pb2_grpc
if TYPE_CHECKING:
    from grpc import ServicerContext
    from sandbox.test import illnamedservice_api as api

import logging
log = logging.getLogger(__name__)


class ServiceWithBadRequestNamesGrpcServicer(plasm.BaseGrpcServicer, pb2_grpc.ServiceWithBadRequestNamesServicer):
    def __init__(self, implementation: 'api.ServiceWithBadRequestNamesInterface'):
        super().__init__(implementation)

    def add_to_server(self, server):
        pb2_grpc.add_ServiceWithBadRequestNamesServicer_to_server(self, server)

    def DoSomething(self, request: dc.pb2.MyAction, context: 'ServicerContext') -> dc.pb2.MyConsequence:
        return self._forward_to_unary_unary_impl(dc.MyConsequence, self.impl.do_something, request, context)

