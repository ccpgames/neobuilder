from . import base
from typing import *

from neobuilder.neobuilder.render import TemplateRenderer
from ..symbols import ProtoMethod


class ModuleBuilder(base.AbstractModuleBuilder):
    builder_name = __name__.split('.')[-1]  # Grab module name

    def get_render_filename(self) -> str:
        return f'{self.module.get_file_full_name()[:-7]}_api.py'

    def get_import_lines(self) -> List[str]:
        import_set = {
            f'from {self.module.get_package()} import {self.module.get_module_name()[:-3]}dc as dc'
        }
        for s in self.module.service_map.values():
            for m in s.method_map.values():
                # From 3.2
                if m.input.self_import.get_package() != 'google.protobuf':
                    import_set.add(m.input.self_import.get_render_import(self.module.descriptor))

                if m.output.self_import.get_package() != 'google.protobuf':
                    import_set.add(m.output.self_import.get_render_import(self.module.descriptor))

                for f in m.input.field_map.values():
                    if f.msg_import:
                        if self.module.descriptor != f.msg_import.descriptor.file:
                            import_set.add(f.msg_import.get_render_import(self.module.descriptor))

                for f in m.output.field_map.values():
                    if f.msg_import:
                        if self.module.descriptor != f.msg_import.descriptor.file:
                            import_set.add(f.msg_import.get_render_import(self.module.descriptor))

        return sorted(import_set)

    def get_template_context(self) -> Dict:
        d: Dict = super().get_template_context()
        d.update({
            'package': self.module.get_package(),
            'import_lines': self.get_import_lines(),
            'services': self.render_services(),
            'all_clause': [f'{svc.service_descriptor.name}Interface' for svc in self.module.service_map.values()]
        })
        return d

    def render(self) -> str:
        return TemplateRenderer().render_file('interface', **self.get_template_context())


class ServiceBuilder(base.AbstractServiceBuilder):
    builder_name = __name__.split('.')[-1]  # Grab module name

    def get_method_context(self, method: ProtoMethod) -> Dict[str, Any]:
        d = super().get_method_context(method)
        d.update({
            'method_under_name': method.under_name,
            'input_params': method.get_input_params(True),
            'return_type_hint': method.get_return_type_hint(True),
        })
        return d

    def render(self) -> str:
        return TemplateRenderer().render_file('parts/_interface_service', **self.get_template_context())


class MethodBuilder(base.AbstractMethodBuilder):
    def get_template_context(self) -> Dict:
        d = super().get_template_context()
        d.update({
            'method_under_name': self.method.under_name,
            'input_params': self.method.get_input_params(True),
            'return_type_hint': self.method.get_return_type_hint(True),
        })
        return d

    def render(self) -> str:
        return TemplateRenderer().render_file('parts/_interface_method', **self.get_template_context())
