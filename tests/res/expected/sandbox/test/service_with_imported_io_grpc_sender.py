# md5: 4083100042bacaf700e862abb15c318c
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.service_with_imported_io_pb2
# Generated at: 2022-06-26T12:07:56.454629
from __future__ import annotations
__all__ = [
    'ServiceWithImportedInputAndOutput',
]
import datetime
import typing
from protoplasm import plasm
from sandbox.test import alpha_dc as sandbox__test__alpha_dc
from sandbox.test import delta_dc as sandbox__test__delta_dc
from sandbox.test import nested_dc as sandbox__test__nested_dc
from sandbox.test import rainbow_dc as sandbox__test__rainbow_dc
from sandbox.test import service_with_imported_io_pb2_grpc as pb2_grpc
from sandbox.test.service_with_imported_io_api import *

if typing.TYPE_CHECKING:
    from grpc import ChannelCredentials

import logging
log = logging.getLogger(__name__)


class ServiceWithImportedInputAndOutput(plasm.BaseGrpcClientImplementation, ServiceWithImportedInputAndOutputInterface):
    def __init__(self, grpc_host: str = 'localhost:50051', credentials: typing.Optional[typing.Union[bool, 'ChannelCredentials']] = None, options: typing.Optional[typing.Dict] = None, *args, **kwargs):
        super().__init__(pb2_grpc.ServiceWithImportedInputAndOutputStub, grpc_host, credentials, options, *args, **kwargs)

    def simple(self, my_string: str = None, my_number: int = None, my_level_three_message: sandbox__test__beta_dc.BetaMessage = None) -> typing.Tuple[str, str]:
        return self._forward_to_grpc(sandbox__test__delta_dc.DeltaMessage, self.stub.Simple, my_string, my_number, my_level_three_message)

    def nested(self, simple_field: str = None, message_field: sandbox__test__rainbow_dc.SubMessage = None, simple_list: typing.List[str] = None, message_list: typing.List[sandbox__test__rainbow_dc.SubMessage] = None, simple_map: typing.Dict[str, str] = None, message_map: typing.Dict[str, sandbox__test__rainbow_dc.SubMessage] = None) -> typing.Tuple[str, int, sandbox__test__alpha_dc.AlphaMessage]:
        return self._forward_to_grpc(sandbox__test__rainbow_dc.RainbowMessage, self.stub.Nested, simple_field, message_field, simple_list, message_list, simple_map, message_map)

    def renest(self, my_int: int = None, my_string: str = None, my_message: sandbox__test__nested_dc.OuterMessage.InnerMessage = None) -> typing.Tuple[str, str]:
        return self._forward_to_grpc(sandbox__test__nested_dc.OuterMessage, self.stub.Renest, my_int, my_string, my_message)

    def timestamp_in(self, my_timestamp: datetime.datetime = None, my_timestamp_list: typing.List[datetime.datetime] = None, my_timestamp_map: typing.Dict[str, datetime.datetime] = None) -> typing.Tuple[str, int]:
        return self._forward_to_grpc(sandbox__test__rainbow_dc.TimestampMessage, self.stub.TimestampIn, my_timestamp, my_timestamp_list, my_timestamp_map)

    def timestamp_out(self, my_string: str = None, my_number: int = None) -> typing.Tuple[int, int]:
        return self._forward_to_grpc(sandbox__test__alpha_dc.AlphaMessage, self.stub.TimestampOut, my_string, my_number)

    def any_in(self, type_url: str = None, value: bytes = None) -> typing.Tuple[str, int]:
        return self._forward_to_grpc(None, self.stub.AnyIn, type_url, value)

    def any_out(self, my_string: str = None, my_number: int = None) -> typing.Tuple[str, bytes]:
        return self._forward_to_grpc(sandbox__test__alpha_dc.AlphaMessage, self.stub.AnyOut, my_string, my_number)
