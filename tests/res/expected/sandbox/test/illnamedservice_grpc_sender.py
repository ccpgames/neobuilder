# md5: 46910dede0d35914d2dbfbf760d892c5
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.illnamedservice_pb2
# Generated at: 2022-06-26T12:07:56.414593
from __future__ import annotations
__all__ = [
    'ServiceWithBadRequestNames',
]
import datetime
import typing
from protoplasm import plasm
from sandbox.test import illnamedservice_dc as dc
from sandbox.test import illnamedservice_pb2_grpc as pb2_grpc
from sandbox.test.illnamedservice_api import *

if typing.TYPE_CHECKING:
    from grpc import ChannelCredentials

import logging
log = logging.getLogger(__name__)


class ServiceWithBadRequestNames(plasm.BaseGrpcClientImplementation, ServiceWithBadRequestNamesInterface):
    def __init__(self, grpc_host: str = 'localhost:50051', credentials: typing.Optional[typing.Union[bool, 'ChannelCredentials']] = None, options: typing.Optional[typing.Dict] = None, *args, **kwargs):
        super().__init__(pb2_grpc.ServiceWithBadRequestNamesStub, grpc_host, credentials, options, *args, **kwargs)

    def do_something(self, foo: str = None) -> str:
        return self._forward_to_grpc(dc.MyAction, self.stub.DoSomething, foo)
