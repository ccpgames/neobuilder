from . import base
import datetime


class ModuleBuilder(base.AbstractModuleBuilder):
    builder_name = __name__.split('.')[-1]  # Grab module name

    def get_render_filename(self) -> str:
        return f'{self.module.get_file_full_name()[:-7]}_impl.py'

    def render_top(self):
        return ('# Auto-Generated example file - Fill this out at will! :D\n'
                f'# Source module: {self.module.get_module_full_name()}\n'
                f'# Generated at: {datetime.datetime.now().isoformat()}\n')

    def render(self) -> str:
        return (
            f'{self.render_top()}'
            f'from {self.module.get_package()}.{self.module.get_module_name()[:-3]}api import *\n'
            'from protoplasm import decorators\n'
            '\n'
            'import logging\n'
            'log = logging.getLogger(__name__)\n'
            '\n'
            '\n'
            f'{self.render_services()}'
        )


class ServiceBuilder(base.AbstractServiceBuilder):
    builder_name = __name__.split('.')[-1]  # Grab module name

    def render(self) -> str:
        ____ = self.indent_str
        i = self.base_indent
        return (
            f'{i}class {self.service.service_descriptor.name}({self.service.service_descriptor.name}Interface):\n'
            f'{self.render_methods()}'
        )


class MethodBuilder(base.AbstractMethodBuilder):
    def render(self) -> str:
        ____ = self.indent_str
        i = self.base_indent
        return (
            f'{i}def {self.method.under_name}(self{self.method.get_input_params()}) -> {self.method.get_return_type_hint()}:\n'
            f"{i}{____}raise errors.api.Unimplemented()\n"
        )
