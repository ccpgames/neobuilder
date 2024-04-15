from . import base
import datetime


class ModuleBuilder(base.AbstractModuleBuilder):
    builder_name = __name__.split('.')[-1]  # Grab module name

    def get_render_filename(self) -> str:
        return f'{self.module.get_file_full_name()[:-7]}_grpc_server.py'

    def render_top(self):
        return ('# Auto-Generated example file - Fill this out at will! :D\n'
                f'# Source module: {self.module.get_module_full_name()}\n'
                f'# Generated at: {datetime.datetime.now().isoformat()}\n')

    def render_services(self) -> str:
        return '\n'.join(self.render_service_list())

    def render(self):
        __ = self.indent_str
        return (
            f'{self.render_top()}'
            'from protoplasm import grpcserver\n'
            f'from {self.module.get_package()} import {self.module.get_module_name()[:-3]}grpc_receiver as grpc_receiver\n'
            f'from {self.module.get_package()} import {self.module.get_module_name()[:-3]}impl as impl\n'
            '\n'
            'import logging\n'
            'log = logging.getLogger(__name__)\n'
            '\n'
            '\n'
            f'def get_grpc_server() -> grpcserver.GrpcServer:\n'
            f'{__}gs = grpcserver.GrpcServer()\n'
            f'{self.render_services()}\n'
            f'{__}return gs\n'
            '\n'
            '\n'
            f"if __name__ == '__main__':\n"
            f'{__}logging.basicConfig(level=logging.DEBUG)\n'
            f'{__}gs = get_grpc_server()\n'
            f'{__}gs.serve()\n'
        )


class ServiceBuilder(base.AbstractServiceBuilder):
    builder_name = __name__.split('.')[-1]  # Grab module name

    def render(self) -> str:
        __ = self.indent_str
        i = self.base_indent
        return f'{i}{__}gs.add_servicer(grpc_receiver.{self.service.service_descriptor.name}GrpcServicer(impl.{self.service.service_descriptor.name}()))'


class MethodBuilder(base.AbstractMethodBuilder):
    pass  # Not used!
