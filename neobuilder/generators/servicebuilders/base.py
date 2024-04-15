from __future__ import annotations
from neobuilder.generators.symbols import service as symbols_service
from neobuilder.generators.symbols import modules
import datetime
from typing import *


class AbstractModuleBuilder(object):
    builder_name = ''

    def __init__(self, module: modules.ProtoModule):
        self.module = module
        self.indent_str = self.module.indent
        self.service_joiner = '\n\n'

    def get_template_context(self) -> Dict:
        return {
            'module_full_name': self.module.get_module_full_name(),
            'iso_timestamp': datetime.datetime.now().isoformat(),
        }

    def render_top(self) -> str:
        # TODO(thordurm@ccpgames.com) 2022-06-24: Remove!
        return ('# Auto-Generated file - DO NOT EDIT!\n'
                f'# Source module: {self.module.get_module_full_name()}\n'
                f'# Generated at: {datetime.datetime.now().isoformat()}\n')

    def render_service_list(self) -> List[str]:
        return [svc.render(self.builder_name) for svc in self.module.service_map.values()]

    def render_services(self) -> str:
        return '\n'.join(self.render_service_list())

    def get_render_filename(self) -> str:
        raise NotImplementedError('AbstractModuleBuilder not implemented')

    def render(self) -> str:
        raise NotImplementedError('AbstractModuleBuilder not implemented')


class AbstractServiceBuilder(object):
    builder_name = ''

    def __init__(self, service: symbols_service.ProtoService, indent_level: int = 0):
        self.service = service
        self.indent_level = indent_level
        self.indent_str = self.service.indent
        self.base_indent = self.indent_str * indent_level

    def get_template_context(self) -> Dict:
        return {
            'service': self.service,
            'service_name': self.service.service_descriptor.name,
            '_indent_level': self.indent_level,
            '_indent_str': self.indent_str,
            '_base_indent': self.base_indent,
            'method_list': [self.get_method_context(m) for m in self.service.method_map.values()],
            'indent_spaces': self.indent_level * 4,
        }

    def get_method_context(self, method: symbols_service.ProtoMethod) -> Dict[str, Any]:
        return {
            'method': method,
        }

    def render_methods(self) -> str:
        ____ = self.indent_str
        i = self.base_indent
        buf = []
        if self.service.method_map:
            buf.append(
                '\n'.join([m.render(self.builder_name, self.indent_level + 1) for m in self.service.method_map.values()]))
        else:
            buf.append(f'{i}pass\n')
        return ''.join(buf)

    def render(self) -> str:
        raise NotImplementedError('AbstractServiceBuilder not implemented')


class AbstractMethodBuilder(object):
    def __init__(self, method: symbols_service.ProtoMethod, indent_level: int = 0):
        self.method = method
        self.indent_level = indent_level
        self.indent_str = self.method.indent
        self.base_indent = self.indent_str * indent_level

    def get_template_context(self) -> Dict:
        return {
            'method': self.method,
            '_indent_level': self.indent_level,
            '_indent_str': self.indent_str,
            '_base_indent': self.base_indent,
            'indent_spaces': self.indent_level * 4,
        }

    def render(self) -> str:
        raise NotImplementedError('AbstractServiceMethod not implemented')
