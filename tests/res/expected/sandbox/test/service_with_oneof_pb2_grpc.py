# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from sandbox.test import service_with_oneof_pb2 as sandbox_dot_test_dot_service__with__oneof__pb2


class SimpleOneOfServiceStub(object):
    """This is a really Simple Service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HelloAgain = channel.unary_unary(
                '/sandbox.test.SimpleOneOfService/HelloAgain',
                request_serializer=sandbox_dot_test_dot_service__with__oneof__pb2.HelloAgainRequest.SerializeToString,
                response_deserializer=sandbox_dot_test_dot_service__with__oneof__pb2.HelloAgainResponse.FromString,
                )


class SimpleOneOfServiceServicer(object):
    """This is a really Simple Service
    """

    def HelloAgain(self, request, context):
        """Say hello
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SimpleOneOfServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HelloAgain': grpc.unary_unary_rpc_method_handler(
                    servicer.HelloAgain,
                    request_deserializer=sandbox_dot_test_dot_service__with__oneof__pb2.HelloAgainRequest.FromString,
                    response_serializer=sandbox_dot_test_dot_service__with__oneof__pb2.HelloAgainResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sandbox.test.SimpleOneOfService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SimpleOneOfService(object):
    """This is a really Simple Service
    """

    @staticmethod
    def HelloAgain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sandbox.test.SimpleOneOfService/HelloAgain',
            sandbox_dot_test_dot_service__with__oneof__pb2.HelloAgainRequest.SerializeToString,
            sandbox_dot_test_dot_service__with__oneof__pb2.HelloAgainResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
