# md5: f949beec3d6a757809954b0f49c5513b
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.river_pb2
# Generated at: 2022-06-26T12:07:56.436596
__all__ = [
    'StreamingServiceGrpcServicer',
]
import datetime
import typing
from protoplasm import plasm
from sandbox.test import river_dc as dc
from sandbox.test import river_pb2 as pb2
from sandbox.test import river_pb2_grpc as pb2_grpc
if typing.TYPE_CHECKING:
    from grpc import ServicerContext
    from sandbox.test import river_api as api

import logging
log = logging.getLogger(__name__)


class StreamingServiceGrpcServicer(plasm.BaseGrpcServicer, pb2_grpc.StreamingServiceServicer):
    def __init__(self, implementation: 'api.StreamingServiceInterface'):
        super().__init__(implementation)

    def add_to_server(self, server):
        pb2_grpc.add_StreamingServiceServicer_to_server(self, server)

    def ReverseMyShit(self, request: dc.pb2.ReverseMyShitRequest, context: 'ServicerContext') -> dc.pb2.ReverseMyShitResponse:
        return self._forward_to_unary_unary_impl(dc.ReverseMyShitResponse, self.impl.reverse_my_shit, request, context)

    def MarcoPolo(self, request_iterator: typing.Iterable[dc.pb2.MarcoPoloRequest], context: 'ServicerContext') -> dc.pb2.MarcoPoloResponse:
        return self._forward_to_stream_stream_impl(dc.MarcoPoloResponse, self.impl.marco_polo, request_iterator, context)

    def TellMeAStory(self, request: dc.pb2.TellMeAStoryRequest, context: 'ServicerContext') -> dc.pb2.TellMeAStoryResponse:
        return self._forward_to_unary_stream_impl(dc.TellMeAStoryResponse, self.impl.tell_me_a_story, request, context)

    def GuessTheNumber(self, request_iterator: typing.Iterable[dc.pb2.GuessTheNumberRequest], context: 'ServicerContext') -> dc.pb2.GuessTheNumberResponse:
        return self._forward_to_stream_unary_impl(dc.GuessTheNumberResponse, self.impl.guess_the_number, request_iterator, context)

