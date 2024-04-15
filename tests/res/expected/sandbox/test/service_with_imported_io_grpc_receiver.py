# md5: fcf4e1506aa41679135b65546bf1471d
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.service_with_imported_io_pb2
# Generated at: 2022-06-26T12:07:56.453631
__all__ = [
    'ServiceWithImportedInputAndOutputGrpcServicer',
]
from typing import *
from protoplasm import plasm
from google.protobuf import any_pb2
from google.protobuf import timestamp_pb2
from sandbox.test import alpha_dc as sandbox__test__alpha_dc
from sandbox.test import beta_dc as sandbox__test__beta_dc
from sandbox.test import delta_dc as sandbox__test__delta_dc
from sandbox.test import nested_dc as sandbox__test__nested_dc
from sandbox.test import rainbow_dc as sandbox__test__rainbow_dc
from sandbox.test import service_with_imported_io_api as api
from sandbox.test import service_with_imported_io_dc as dc
from sandbox.test import service_with_imported_io_pb2 as pb2
from sandbox.test import service_with_imported_io_pb2_grpc as pb2_grpc
if TYPE_CHECKING:
    from grpc import ServicerContext

import logging
log = logging.getLogger(__name__)


class ServiceWithImportedInputAndOutputGrpcServicer(plasm.BaseGrpcServicer, pb2_grpc.ServiceWithImportedInputAndOutputServicer):
    def __init__(self, implementation: api.ServiceWithImportedInputAndOutputInterface):
        super().__init__(implementation)

    def add_to_server(self, server):
        pb2_grpc.add_ServiceWithImportedInputAndOutputServicer_to_server(self, server)

    def Simple(self, request: sandbox__test__delta_dc.pb2.DeltaMessage, context: 'ServicerContext') -> sandbox__test__rainbow_dc.pb2.SubMessage:
        return self._forward_to_unary_unary_impl(sandbox__test__rainbow_dc.SubMessage, self.impl.simple, request, context)

    def Nested(self, request: sandbox__test__rainbow_dc.pb2.RainbowMessage, context: 'ServicerContext') -> sandbox__test__beta_dc.pb2.BetaMessage:
        return self._forward_to_unary_unary_impl(sandbox__test__beta_dc.BetaMessage, self.impl.nested, request, context)

    def Renest(self, request: sandbox__test__nested_dc.pb2.OuterMessage, context: 'ServicerContext') -> sandbox__test__rainbow_dc.pb2.SubMessage:
        return self._forward_to_unary_unary_impl(sandbox__test__rainbow_dc.SubMessage, self.impl.renest, request, context)

    def TimestampIn(self, request: sandbox__test__rainbow_dc.pb2.TimestampMessage, context: 'ServicerContext') -> sandbox__test__alpha_dc.pb2.AlphaMessage:
        return self._forward_to_unary_unary_impl(sandbox__test__alpha_dc.AlphaMessage, self.impl.timestamp_in, request, context)

    def TimestampOut(self, request: sandbox__test__alpha_dc.pb2.AlphaMessage, context: 'ServicerContext') -> timestamp_pb2.Timestamp:
        return self._forward_to_unary_unary_impl(None, self.impl.timestamp_out, request, context)

    def AnyIn(self, request: any_pb2.Any, context: 'ServicerContext') -> sandbox__test__alpha_dc.pb2.AlphaMessage:
        return self._forward_to_unary_unary_impl(sandbox__test__alpha_dc.AlphaMessage, self.impl.any_in, request, context)

    def AnyOut(self, request: sandbox__test__alpha_dc.pb2.AlphaMessage, context: 'ServicerContext') -> any_pb2.Any:
        return self._forward_to_unary_unary_impl(None, self.impl.any_out, request, context)

