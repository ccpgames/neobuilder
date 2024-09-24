# md5: 477a1a447caf7cb13cf02dffa3ea736c
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.service_with_oneof_pb2
# Generated at: 2022-06-26T12:07:56.462616
from __future__ import annotations
__all__ = [
    'SimpleOneOfService',
]
import datetime
import typing
from protoplasm import plasm
from sandbox.test import service_with_oneof_dc as dc
from sandbox.test import service_with_oneof_pb2_grpc as pb2_grpc
from sandbox.test.service_with_oneof_api import *

if typing.TYPE_CHECKING:
    from grpc import ChannelCredentials

import logging
log = logging.getLogger(__name__)


class SimpleOneOfService(plasm.BaseGrpcClientImplementation, SimpleOneOfServiceInterface):
    def __init__(self, grpc_host: str = 'localhost:50051', credentials: typing.Optional[typing.Union[bool, 'ChannelCredentials']] = None, options: typing.Optional[typing.Dict] = None, *args, **kwargs):
        super().__init__(pb2_grpc.SimpleOneOfServiceStub, grpc_host, credentials, options, *args, **kwargs)

    def hello_again(self, greeting: str = None) -> typing.Tuple[str, int]:
        return self._forward_to_grpc(dc.HelloAgainRequest, self.stub.HelloAgain, greeting)
