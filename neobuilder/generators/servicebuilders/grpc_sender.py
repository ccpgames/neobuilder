from . import base
import grpc
from typing import *

from ...neobuilder.render import TemplateRenderer


class ModuleBuilder(base.AbstractModuleBuilder):
    builder_name = __name__.split('.')[-1]  # Grab module name

    def get_render_filename(self) -> str:
        return f'{self.module.get_file_full_name()[:-7]}_grpc_sender.py'

    def render_imports(self) -> str:
        import_set = {
            f'from {self.module.get_package()} import {self.module.get_module_name()}_grpc as pb2_grpc\n'
            f'from {self.module.get_package()}.{self.module.get_module_name()[:-3]}api import *\n'
        }

        for s in self.module.service_map.values():
            for m in s.method_map.values():
                if m.input:
                    if m.input.self_import and m.input.self_import.get_package() != 'google.protobuf':
                        import_set.add(m.input.self_import.get_render_import(self.module.descriptor))

        if import_set:
            return '\n'.join(sorted(import_set))
        return ''

    def get_template_context(self) -> Dict:
        d = super().get_template_context()
        d.update({
            'imports': self.render_imports(),
            'services': self.render_services(),
            'all_list': [f'{svc.service_descriptor.name}' for svc in self.module.service_map.values()],
        })
        return d

    def render(self) -> str:
        return TemplateRenderer().render_file('grpc_sender', **self.get_template_context())


class ServiceBuilder(base.AbstractServiceBuilder):
    builder_name = __name__.split('.')[-1]  # Grab module name

    def render(self) -> str:
        __ = self.indent_str
        i = self.base_indent
        return (
            f'{i}class {self.service.service_descriptor.name}(plasm.BaseGrpcClientImplementation, {self.service.service_descriptor.name}Interface):\n'
            f'{i}{__}def __init__(self, grpc_host: str = \'localhost:50051\', credentials: typing.Optional[typing.Union[bool, \'ChannelCredentials\']] = None, options: typing.Optional[typing.Dict] = None, *args, **kwargs):\n'
            f'{i}{__}{__}super().__init__(pb2_grpc.{self.service.service_descriptor.name}Stub, grpc_host, credentials, options, *args, **kwargs)\n'
            f'\n'
            f'{self.render_methods()}'
        )


class MethodBuilder(base.AbstractMethodBuilder):
    def render(self) -> str:
        __ = self.indent_str
        i = self.base_indent
        return (
            f'{i}def {self.method.under_name}(self{self.method.get_input_params(True)}) -> {self.method.get_return_type_hint(True)}:\n'
            f"{i}{__}return self._forward_to_grpc({self.method.get_request_dc_type_hint()}, self.stub.{self.method.method_descriptor.name}{self.method.get_fwd_params()})\n"
        )
