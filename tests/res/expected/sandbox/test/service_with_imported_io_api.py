# md5: 9f1d3a9acd29a04ef4fd207012b00864
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.service_with_imported_io_pb2
# Generated at: 2022-06-26T12:07:56.450593
__all__ = [
    'ServiceWithImportedInputAndOutputInterface',
]
import datetime
import typing
from protoplasm import plasm

from sandbox.test import alpha_dc as sandbox__test__alpha_dc
from sandbox.test import beta_dc as sandbox__test__beta_dc
from sandbox.test import delta_dc as sandbox__test__delta_dc
from sandbox.test import nested_dc as sandbox__test__nested_dc
from sandbox.test import rainbow_dc as sandbox__test__rainbow_dc
from sandbox.test import service_with_imported_io_dc as dc
from sandbox.test.service_with_imported_io_grpc_receiver import ServiceWithImportedInputAndOutputGrpcServicer

import logging
log = logging.getLogger(__name__)


class ServiceWithImportedInputAndOutputInterface:
    __servicer_cls__ = ServiceWithImportedInputAndOutputGrpcServicer

    def simple(self, my_string: str = None, my_number: int = None, my_level_three_message: sandbox__test__beta_dc.BetaMessage = None) -> typing.Tuple[str, str]:
        raise plasm.Unimplemented()

    def nested(self, simple_field: str = None, message_field: sandbox__test__rainbow_dc.SubMessage = None, simple_list: typing.List[str] = None, message_list: typing.List[sandbox__test__rainbow_dc.SubMessage] = None, simple_map: typing.Dict[str, str] = None, message_map: typing.Dict[str, sandbox__test__rainbow_dc.SubMessage] = None) -> typing.Tuple[str, int, sandbox__test__alpha_dc.AlphaMessage]:
        raise plasm.Unimplemented()

    def renest(self, my_int: int = None, my_string: str = None, my_message: sandbox__test__nested_dc.OuterMessage.InnerMessage = None) -> typing.Tuple[str, str]:
        raise plasm.Unimplemented()

    def timestamp_in(self, my_timestamp: datetime.datetime = None, my_timestamp_list: typing.List[datetime.datetime] = None, my_timestamp_map: typing.Dict[str, datetime.datetime] = None) -> typing.Tuple[str, int]:
        raise plasm.Unimplemented()

    def timestamp_out(self, my_string: str = None, my_number: int = None) -> typing.Tuple[int, int]:
        raise plasm.Unimplemented()

    def any_in(self, type_url: str = None, value: bytes = None) -> typing.Tuple[str, int]:
        raise plasm.Unimplemented()

    def any_out(self, my_string: str = None, my_number: int = None) -> typing.Tuple[str, bytes]:
        raise plasm.Unimplemented()

