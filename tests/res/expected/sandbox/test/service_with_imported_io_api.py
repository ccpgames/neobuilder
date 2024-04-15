# md5: 9f1d3a9acd29a04ef4fd207012b00864
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.service_with_imported_io_pb2
# Generated at: 2022-06-26T12:07:56.450593
__all__ = [
    'ServiceWithImportedInputAndOutputInterface',
]
import datetime
from typing import *
from protoplasm import plasm

from sandbox.test import alpha_dc as sandbox__test__alpha_dc
from sandbox.test import beta_dc as sandbox__test__beta_dc
from sandbox.test import delta_dc as sandbox__test__delta_dc
from sandbox.test import nested_dc as sandbox__test__nested_dc
from sandbox.test import rainbow_dc as sandbox__test__rainbow_dc
from sandbox.test import service_with_imported_io_dc as dc

import logging
log = logging.getLogger(__name__)


class ServiceWithImportedInputAndOutputInterface:
    def simple(self, my_string: str = None, my_number: int = None, my_level_three_message: sandbox__test__beta_dc.BetaMessage = None) -> Tuple[str, str]:
        raise plasm.Unimplemented()

    def nested(self, simple_field: str = None, message_field: sandbox__test__rainbow_dc.SubMessage = None, simple_list: List[str] = None, message_list: List[sandbox__test__rainbow_dc.SubMessage] = None, simple_map: Dict[str, str] = None, message_map: Dict[str, sandbox__test__rainbow_dc.SubMessage] = None) -> Tuple[str, int, sandbox__test__alpha_dc.AlphaMessage]:
        raise plasm.Unimplemented()

    def renest(self, my_int: int = None, my_string: str = None, my_message: sandbox__test__nested_dc.OuterMessage.InnerMessage = None) -> Tuple[str, str]:
        raise plasm.Unimplemented()

    def timestamp_in(self, my_timestamp: datetime.datetime = None, my_timestamp_list: List[datetime.datetime] = None, my_timestamp_map: Dict[str, datetime.datetime] = None) -> Tuple[str, int]:
        raise plasm.Unimplemented()

    def timestamp_out(self, my_string: str = None, my_number: int = None) -> Tuple[int, int]:
        raise plasm.Unimplemented()

    def any_in(self, type_url: str = None, value: bytes = None) -> Tuple[str, int]:
        raise plasm.Unimplemented()

    def any_out(self, my_string: str = None, my_number: int = None) -> Tuple[str, bytes]:
        raise plasm.Unimplemented()

