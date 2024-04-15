# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from sandbox.test import river_pb2 as sandbox_dot_test_dot_river__pb2


class StreamingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReverseMyShit = channel.unary_unary(
                '/sandbox.test.StreamingService/ReverseMyShit',
                request_serializer=sandbox_dot_test_dot_river__pb2.ReverseMyShitRequest.SerializeToString,
                response_deserializer=sandbox_dot_test_dot_river__pb2.ReverseMyShitResponse.FromString,
                )
        self.MarcoPolo = channel.stream_stream(
                '/sandbox.test.StreamingService/MarcoPolo',
                request_serializer=sandbox_dot_test_dot_river__pb2.MarcoPoloRequest.SerializeToString,
                response_deserializer=sandbox_dot_test_dot_river__pb2.MarcoPoloResponse.FromString,
                )
        self.TellMeAStory = channel.unary_stream(
                '/sandbox.test.StreamingService/TellMeAStory',
                request_serializer=sandbox_dot_test_dot_river__pb2.TellMeAStoryRequest.SerializeToString,
                response_deserializer=sandbox_dot_test_dot_river__pb2.TellMeAStoryResponse.FromString,
                )
        self.GuessTheNumber = channel.stream_unary(
                '/sandbox.test.StreamingService/GuessTheNumber',
                request_serializer=sandbox_dot_test_dot_river__pb2.GuessTheNumberRequest.SerializeToString,
                response_deserializer=sandbox_dot_test_dot_river__pb2.GuessTheNumberResponse.FromString,
                )


class StreamingServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ReverseMyShit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MarcoPolo(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TellMeAStory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GuessTheNumber(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReverseMyShit': grpc.unary_unary_rpc_method_handler(
                    servicer.ReverseMyShit,
                    request_deserializer=sandbox_dot_test_dot_river__pb2.ReverseMyShitRequest.FromString,
                    response_serializer=sandbox_dot_test_dot_river__pb2.ReverseMyShitResponse.SerializeToString,
            ),
            'MarcoPolo': grpc.stream_stream_rpc_method_handler(
                    servicer.MarcoPolo,
                    request_deserializer=sandbox_dot_test_dot_river__pb2.MarcoPoloRequest.FromString,
                    response_serializer=sandbox_dot_test_dot_river__pb2.MarcoPoloResponse.SerializeToString,
            ),
            'TellMeAStory': grpc.unary_stream_rpc_method_handler(
                    servicer.TellMeAStory,
                    request_deserializer=sandbox_dot_test_dot_river__pb2.TellMeAStoryRequest.FromString,
                    response_serializer=sandbox_dot_test_dot_river__pb2.TellMeAStoryResponse.SerializeToString,
            ),
            'GuessTheNumber': grpc.stream_unary_rpc_method_handler(
                    servicer.GuessTheNumber,
                    request_deserializer=sandbox_dot_test_dot_river__pb2.GuessTheNumberRequest.FromString,
                    response_serializer=sandbox_dot_test_dot_river__pb2.GuessTheNumberResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sandbox.test.StreamingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StreamingService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ReverseMyShit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sandbox.test.StreamingService/ReverseMyShit',
            sandbox_dot_test_dot_river__pb2.ReverseMyShitRequest.SerializeToString,
            sandbox_dot_test_dot_river__pb2.ReverseMyShitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MarcoPolo(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/sandbox.test.StreamingService/MarcoPolo',
            sandbox_dot_test_dot_river__pb2.MarcoPoloRequest.SerializeToString,
            sandbox_dot_test_dot_river__pb2.MarcoPoloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TellMeAStory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/sandbox.test.StreamingService/TellMeAStory',
            sandbox_dot_test_dot_river__pb2.TellMeAStoryRequest.SerializeToString,
            sandbox_dot_test_dot_river__pb2.TellMeAStoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GuessTheNumber(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/sandbox.test.StreamingService/GuessTheNumber',
            sandbox_dot_test_dot_river__pb2.GuessTheNumberRequest.SerializeToString,
            sandbox_dot_test_dot_river__pb2.GuessTheNumberResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
