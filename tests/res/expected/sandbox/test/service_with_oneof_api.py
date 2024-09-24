# md5: 4f4284f233d9b306f90f241c9f5c8b9d
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.service_with_oneof_pb2
# Generated at: 2022-06-26T12:07:56.459594
__all__ = [
    'SimpleOneOfServiceInterface',
]
import datetime
import typing
from protoplasm import plasm

from sandbox.test import service_with_oneof_dc as dc
from sandbox.test.service_with_oneof_grpc_receiver import SimpleOneOfServiceGrpcServicer

import logging
log = logging.getLogger(__name__)


class SimpleOneOfServiceInterface:
    __servicer_cls__ = SimpleOneOfServiceGrpcServicer

    def hello_again(self, greeting: str = None) -> typing.Tuple[str, int]:
        raise plasm.Unimplemented()

