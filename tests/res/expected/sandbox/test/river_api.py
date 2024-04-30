# md5: ab3f54dac463476b0bb955bdad25becd
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.river_pb2
# Generated at: 2022-06-26T12:07:56.433592
__all__ = [
    'StreamingServiceInterface',
]
import datetime
from typing import *
from protoplasm import plasm

from sandbox.test import river_dc as dc
from sandbox.test.river_grpc_receiver import StreamingServiceGrpcServicer

import logging
log = logging.getLogger(__name__)


class StreamingServiceInterface:
    __servicer_cls__ = StreamingServiceGrpcServicer

    def reverse_my_shit(self, shit: str = None) -> str:
        raise plasm.Unimplemented()

    def marco_polo(self, request_iterator: Iterable[dc.MarcoPoloRequest]) -> plasm.ResponseIterator[dc.MarcoPoloResponse]:
        raise plasm.Unimplemented()

    def tell_me_a_story(self, story: str = None) -> plasm.ResponseIterator[dc.TellMeAStoryResponse]:
        raise plasm.Unimplemented()

    def guess_the_number(self, request_iterator: Iterable[dc.GuessTheNumberRequest]) -> str:
        raise plasm.Unimplemented()

