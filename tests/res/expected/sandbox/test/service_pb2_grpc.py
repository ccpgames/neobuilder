# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from sandbox.test import service_pb2 as sandbox_dot_test_dot_service__pb2


class SimpleServiceStub(object):
    """This is a really Simple Service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Hello = channel.unary_unary(
                '/sandbox.test.SimpleService/Hello',
                request_serializer=sandbox_dot_test_dot_service__pb2.HelloRequest.SerializeToString,
                response_deserializer=sandbox_dot_test_dot_service__pb2.HelloResponse.FromString,
                )
        self.NestedHello = channel.unary_unary(
                '/sandbox.test.SimpleService/NestedHello',
                request_serializer=sandbox_dot_test_dot_service__pb2.NestedHelloRequest.SerializeToString,
                response_deserializer=sandbox_dot_test_dot_service__pb2.NestedHelloResponse.FromString,
                )
        self.EmptyHello = channel.unary_unary(
                '/sandbox.test.SimpleService/EmptyHello',
                request_serializer=sandbox_dot_test_dot_service__pb2.EmptyHelloRequest.SerializeToString,
                response_deserializer=sandbox_dot_test_dot_service__pb2.EmptyHelloResponse.FromString,
                )


class SimpleServiceServicer(object):
    """This is a really Simple Service
    """

    def Hello(self, request, context):
        """Say hello documentation
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NestedHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EmptyHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SimpleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Hello': grpc.unary_unary_rpc_method_handler(
                    servicer.Hello,
                    request_deserializer=sandbox_dot_test_dot_service__pb2.HelloRequest.FromString,
                    response_serializer=sandbox_dot_test_dot_service__pb2.HelloResponse.SerializeToString,
            ),
            'NestedHello': grpc.unary_unary_rpc_method_handler(
                    servicer.NestedHello,
                    request_deserializer=sandbox_dot_test_dot_service__pb2.NestedHelloRequest.FromString,
                    response_serializer=sandbox_dot_test_dot_service__pb2.NestedHelloResponse.SerializeToString,
            ),
            'EmptyHello': grpc.unary_unary_rpc_method_handler(
                    servicer.EmptyHello,
                    request_deserializer=sandbox_dot_test_dot_service__pb2.EmptyHelloRequest.FromString,
                    response_serializer=sandbox_dot_test_dot_service__pb2.EmptyHelloResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sandbox.test.SimpleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SimpleService(object):
    """This is a really Simple Service
    """

    @staticmethod
    def Hello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sandbox.test.SimpleService/Hello',
            sandbox_dot_test_dot_service__pb2.HelloRequest.SerializeToString,
            sandbox_dot_test_dot_service__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NestedHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sandbox.test.SimpleService/NestedHello',
            sandbox_dot_test_dot_service__pb2.NestedHelloRequest.SerializeToString,
            sandbox_dot_test_dot_service__pb2.NestedHelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EmptyHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sandbox.test.SimpleService/EmptyHello',
            sandbox_dot_test_dot_service__pb2.EmptyHelloRequest.SerializeToString,
            sandbox_dot_test_dot_service__pb2.EmptyHelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class MathStub(object):
    """Does math stuff
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Add = channel.unary_unary(
                '/sandbox.test.Math/Add',
                request_serializer=sandbox_dot_test_dot_service__pb2.AddRequest.SerializeToString,
                response_deserializer=sandbox_dot_test_dot_service__pb2.AddResponse.FromString,
                )
        self.Subtract = channel.unary_unary(
                '/sandbox.test.Math/Subtract',
                request_serializer=sandbox_dot_test_dot_service__pb2.SubtractRequest.SerializeToString,
                response_deserializer=sandbox_dot_test_dot_service__pb2.SubtractResponse.FromString,
                )
        self.IntegerDivision = channel.unary_unary(
                '/sandbox.test.Math/IntegerDivision',
                request_serializer=sandbox_dot_test_dot_service__pb2.IntegerDivisionRequest.SerializeToString,
                response_deserializer=sandbox_dot_test_dot_service__pb2.IntegerDivisionResponse.FromString,
                )


class MathServicer(object):
    """Does math stuff
    """

    def Add(self, request, context):
        """Adds two numbers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subtract(self, request, context):
        """Subtracts the later number from the former
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IntegerDivision(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MathServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Add': grpc.unary_unary_rpc_method_handler(
                    servicer.Add,
                    request_deserializer=sandbox_dot_test_dot_service__pb2.AddRequest.FromString,
                    response_serializer=sandbox_dot_test_dot_service__pb2.AddResponse.SerializeToString,
            ),
            'Subtract': grpc.unary_unary_rpc_method_handler(
                    servicer.Subtract,
                    request_deserializer=sandbox_dot_test_dot_service__pb2.SubtractRequest.FromString,
                    response_serializer=sandbox_dot_test_dot_service__pb2.SubtractResponse.SerializeToString,
            ),
            'IntegerDivision': grpc.unary_unary_rpc_method_handler(
                    servicer.IntegerDivision,
                    request_deserializer=sandbox_dot_test_dot_service__pb2.IntegerDivisionRequest.FromString,
                    response_serializer=sandbox_dot_test_dot_service__pb2.IntegerDivisionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sandbox.test.Math', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Math(object):
    """Does math stuff
    """

    @staticmethod
    def Add(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sandbox.test.Math/Add',
            sandbox_dot_test_dot_service__pb2.AddRequest.SerializeToString,
            sandbox_dot_test_dot_service__pb2.AddResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subtract(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sandbox.test.Math/Subtract',
            sandbox_dot_test_dot_service__pb2.SubtractRequest.SerializeToString,
            sandbox_dot_test_dot_service__pb2.SubtractResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IntegerDivision(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sandbox.test.Math/IntegerDivision',
            sandbox_dot_test_dot_service__pb2.IntegerDivisionRequest.SerializeToString,
            sandbox_dot_test_dot_service__pb2.IntegerDivisionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
