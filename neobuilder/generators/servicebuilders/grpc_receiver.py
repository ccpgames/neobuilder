from . import base
import grpc
from neobuilder.structs import *
from neobuilder.neobuilder.render import TemplateRenderer


class ModuleBuilder(base.AbstractModuleBuilder):
    builder_name = __name__.split('.')[-1]  # Grab module name

    def get_render_filename(self) -> str:
        return f'{self.module.get_file_full_name()[:-7]}_grpc_receiver.py'

    def render_imports(self) -> str:
        import_set = {
            f'from {self.module.get_package()} import {self.module.get_module_name()} as pb2',
            f'from {self.module.get_package()} import {self.module.get_module_name()}_grpc as pb2_grpc',
            f'from {self.module.get_package()} import {self.module.get_module_name()[:-3]}dc as dc',
        }

        for s in self.module.service_map.values():
            for m in s.method_map.values():
                if m.input:
                    if m.input.self_import:
                        if self.module.descriptor != m.input.self_import.descriptor.file:
                            if m.input.self_import.get_package() != 'google.protobuf':
                                import_set.add(m.input.self_import.get_render_import())
                            else:
                                import_set.add(f'from google.protobuf import {m.input.self_import.get_class_name().lower()}_pb2')
                if m.output:
                    if m.output.self_import:
                        if self.module.descriptor != m.output.self_import.descriptor.file:
                            if m.output.self_import.get_package() != 'google.protobuf':
                                import_set.add(m.output.self_import.get_render_import())
                            else:
                                import_set.add(f'from google.protobuf import {m.output.self_import.get_class_name().lower()}_pb2')

        if import_set:
            return '\n'.join(sorted(import_set))
        return ''

    def get_template_context(self) -> Dict:
        d = super().get_template_context()
        d.update({
            'api_import': f'from {self.module.get_package()} import {self.module.get_module_name()[:-3]}api as api',
            'services': self.render_services(),
            'imports': self.render_imports(),
            'all_list': [f'{svc.service_descriptor.name}GrpcServicer' for svc in self.module.service_map.values()],
        })
        return d

    def render(self) -> str:
        return TemplateRenderer().render_file('grpc_receiver', **self.get_template_context())


class ServiceBuilder(base.AbstractServiceBuilder):
    builder_name = __name__.split('.')[-1]  # Grab module name

    def render(self) -> str:
        __ = self.indent_str
        i = self.base_indent
        return (
            f'{i}class {self.service.service_descriptor.name}GrpcServicer(plasm.BaseGrpcServicer, pb2_grpc.{self.service.service_descriptor.name}Servicer):\n'
            f"{i}{__}def __init__(self, implementation: 'api.{self.service.service_descriptor.name}Interface'):\n"
            f'{i}{__}{__}super().__init__(implementation)\n'
            '\n'
            f'{i}{__}def add_to_server(self, server):\n'
            f'{i}{__}{__}pb2_grpc.add_{self.service.service_descriptor.name}Servicer_to_server(self, server)\n'
            '\n'
            f'{self.render_methods()}'
            '\n'
        )


class MethodBuilder(base.AbstractMethodBuilder):
    def render(self) -> str:
        __ = self.indent_str
        i = self.base_indent

        # TODO(thordurm@ccpgames.com>): The Request and Response may not be from the same file as the service!
        input_param_name = 'request_iterator' if self.method.io_type.is_input_stream() else 'request'
        return (
            f'{i}def {self.method.method_descriptor.name}(self, {input_param_name}: {self.method.get_request_type_hint()}, context: \'ServicerContext\') -> {self.method.get_response_type_hint()}:\n'
            f"{i}{__}return self.{self._forward_to_x_y_impl()}({self.method.get_response_dc_class_type()}, self.impl.{self.method.under_name}, {input_param_name}, context)\n"
        )

    def _forward_to_x_y_impl(self):
        return '_'.join([
            '_forward_to',
            'stream' if self.method.io_type.is_input_stream() else 'unary',
            'stream' if self.method.io_type.is_output_stream() else 'unary',
            'impl',
        ])
