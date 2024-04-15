from __future__ import annotations
__all__ = [
    'ProtoService',
    'ProtoMethod',
]
from google.protobuf import json_format

from neobuilder.descwrap import *
from neobuilder.structs import *

from neobuilder.generators import servicebuilders
from neobuilder.generators.symbols import dataclass
from neobuilder.generators.symbols import modules


class ProtoService(object):
    def __init__(self, service_descriptor: json_format.descriptor.ServiceDescriptor, module: modules.ProtoModule):
        self.service_descriptor = service_descriptor
        # self.service_descriptor.name = Math
        # self.service_descriptor.file.name = sandbox/test/service.proto
        # self.service_descriptor.file.package = sandbox.test
        # self.service_descriptor.full_name = sandbox.test.Math
        self.module = module
        self.method_map: Mapping[str, ProtoMethod] = {}
        self.indent = module.indent
        self._load_service()

    def _load_service(self):
        self.method_map = {m.name: ProtoMethod(m, self) for m in self.service_descriptor.methods}

    # ---

    def render_grpc_server(self, indent_level=0):  # GRPC Server
        return self.render('grpc_server', indent_level)
        # return f'{self.indent*indent_level}gs.add_servicer(dc_grpc.{self.service_descriptor.name}GrpcServicer(impl.{self.service_descriptor.name}()))'

    def render_api_service(self, indent_level=0):  # API
        return self.render('interface', indent_level)

    def render_grpc_servicer(self, indent_level=0):  # GRPC DC
        return self.render('grpc_receiver', indent_level)

    def render_grpc_impl(self, indent_level=0):  # GRPC Implementation
        return self.render('grpc_sender', indent_level)

    def render_impl_service(self, indent_level=0):  # Implementation example
        return self.render('implementation', indent_level)

    #
    # Generic renderer
    #

    def render(self, builder_name: str, indent_level: int = 0) -> str:
        return servicebuilders.get_service_builder(builder_name)(self, indent_level).render()


class ProtoMethod(object):
    def __init__(self,
                 method_descriptor: json_format.descriptor.MethodDescriptor,
                 service: ProtoService):
        self.method_descriptor: MethodDescriptorWrapper = MethodDescriptorWrapper(method_descriptor)
        # self.method_descriptor.name = Add
        # self.method_descriptor.full_name = sandbox.test.Math.Add
        self.service = service
        self.indent = service.indent

        self.input = dataclass.ProtoClass(self.method_descriptor.input_type, self.service.module, force_import=True)
        self.output = dataclass.ProtoClass(self.method_descriptor.output_type, self.service.module, force_import=True)

    @property
    def under_name(self) -> str:
        return self.method_descriptor.under_name

    def get_return_type_hint(self, relative_to_self: bool = False):
        if self.io_type.is_output_stream():
            if relative_to_self:
                return f'plasm.ResponseIterator[{self.output.render_api_return_dataclass(self.service.service_descriptor.file)}]'
            return f'plasm.ResponseIterator[{self.output.render_api_return_dataclass()}]'
        if relative_to_self:
            return self.output.render_api_return_args(self.service.service_descriptor.file)
        return self.output.render_api_return_args()

    def get_input_params(self, relative_to_self: bool = False):
        # TODO(thordurm@ccpgames.com) 2022-06-18: Check for input stream...
        if self.io_type.is_input_stream():
            return self.input.render_api_request_arg(self.method_descriptor)

        else:
            if relative_to_self:
                args = self.input.render_api_args(self.service.service_descriptor.file)
            else:
                args = self.input.render_api_args()
            if args:
                return f', {args}'
            else:
                return ''

    def get_fwd_params(self):
        if self.io_type.is_input_stream():
            return ', request_iterator'

        args = self.input.render_forwarded_args()
        if args:
            return f', {args}'
        else:
            return ''

    def get_input_name(self):
        return f'{self.input.get_class_name()}'

    def get_output_name(self):
        return f'{self.output.get_class_name()}'

    def get_request_type_hint(self) -> str:
        unary = f'{self.input.render_pb2_type_hint(self.service.module)}'
        if self.io_type.is_input_stream():
            return f'Iterable[{unary}]'
        return unary

    def get_request_dc_type_hint(self) -> str:
        return f'{self.input.render_dc_type_hint(self.service.module)}'

    def get_response_type_hint(self) -> str:
        return f'{self.output.render_pb2_type_hint(self.service.module)}'

    def get_response_dc_type(self) -> str:
        if self.io_type.is_output_stream():
            return f'Iterable[{self.get_response_dc_class_type()}]'
        return self.get_response_dc_class_type()

    def get_response_dc_class_type(self) -> str:
        return f'{self.output.render_dc_type_hint(self.service.module)}'

    def render(self, generator_name: str, indent_level: int = 0) -> str:
        return servicebuilders.get_method_builder(generator_name)(self, indent_level).render()

    @property
    def io_type(self) -> MethodIoType:
        return self.method_descriptor.io_type
