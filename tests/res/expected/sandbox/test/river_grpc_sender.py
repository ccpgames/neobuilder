# md5: 161a73d7328da5966f66b94d55d32506
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.river_pb2
# Generated at: 2022-06-26T12:07:56.437592
from __future__ import annotations
__all__ = [
    'StreamingService',
]
from typing import *
from protoplasm import plasm
from sandbox.test import river_dc as dc
from sandbox.test import river_pb2_grpc as pb2_grpc
from sandbox.test.river_api import *

if TYPE_CHECKING:
    from grpc import ChannelCredentials

import logging
log = logging.getLogger(__name__)


class StreamingService(plasm.BaseGrpcClientImplementation, StreamingServiceInterface):
    def __init__(self, grpc_host: str = 'localhost:50051', credentials: Optional[Union[bool, 'ChannelCredentials']] = None, options: Optional[Dict] = None, *args, **kwargs):
        super().__init__(pb2_grpc.StreamingServiceStub, grpc_host, credentials, options, *args, **kwargs)

    def reverse_my_shit(self, shit: str = None) -> str:
        return self._forward_to_grpc(dc.ReverseMyShitRequest, self.stub.ReverseMyShit, shit)

    def marco_polo(self, request_iterator: Iterable[dc.MarcoPoloRequest]) -> plasm.ResponseIterator[dc.MarcoPoloResponse]:
        return self._forward_to_grpc(dc.MarcoPoloRequest, self.stub.MarcoPolo, request_iterator)

    def tell_me_a_story(self, story: str = None) -> plasm.ResponseIterator[dc.TellMeAStoryResponse]:
        return self._forward_to_grpc(dc.TellMeAStoryRequest, self.stub.TellMeAStory, story)

    def guess_the_number(self, request_iterator: Iterable[dc.GuessTheNumberRequest]) -> str:
        return self._forward_to_grpc(dc.GuessTheNumberRequest, self.stub.GuessTheNumber, request_iterator)
