from __future__ import annotations
__all__ = [
    'ProtoModule',
]

import datetime
import hashlib
import os
import re
from typing import *

from google.protobuf import json_format

from neobuilder.generators.symbols import service
from neobuilder.generators.symbols import dataclass
from neobuilder.generators import servicebuilders
from neobuilder.neobuilder.render import TemplateRenderer

import logging
log = logging.getLogger(__name__)


CHECKSUM_MATCHER = re.compile(r'^# md5: (?P<checksum>[\dA-F]{32})', re.IGNORECASE)


class ProtoModule(object):
    def __init__(self, module, indent='    '):
        self.module = module
        self.indent = indent
        self.descriptor: json_format.descriptor.FileDescriptor = module.DESCRIPTOR
        self.message_map: Mapping[str, dataclass.ProtoClass] = {}
        self.enum_map: Mapping[str, dataclass.ProtoEnum] = {}
        self.service_map: Mapping[str, service.ProtoService] = {}
        self.imports: Mapping[str, json_format.descriptor.FileDescriptor] = {}

        self._load_module()

    def _load_module(self):
        self.enum_map = {n: dataclass.ProtoEnum(des, self) for n, des in self.descriptor.enum_types_by_name.items()}
        self.message_map = {n: dataclass.ProtoClass(des, self) for n, des in self.descriptor.message_types_by_name.items()}
        self.service_map = {n: service.ProtoService(des, self) for n, des in self.descriptor.services_by_name.items()}

    def get_module_full_name(self):
        return self.module.__name__

    def get_module_name(self):
        return self.module.__name__.split('.')[-1]

    def get_module_name_parts(self):
        return self.module.__name__.split('.')

    def get_package(self):
        return self.module.__package__

    def get_file_full_name(self):
        return self.module.__file__

    def get_file_name(self):
        return os.path.basename(self.get_file_full_name())

    def get_file_path(self):
        return os.path.dirname(self.get_file_full_name())

    def get_name(self):
        return os.path.splitext(self.get_file_name())[0]

    def get_render_file_name(self):
        return f'{self.get_file_full_name()[:-7]}_dc.py'

    def get_grpc_file_name(self):
        return f'{self.get_file_full_name()[:-3]}_grpc.py'

    def get_md5_hash(self, contents):
        hasher = hashlib.md5()
        if isinstance(contents, str):
            contents = contents.encode('utf-8')
        hasher.update(contents)
        return hasher.hexdigest()

    def can_write(self, filename, silent=False):
        if not os.path.exists(filename):
            return True  # File doesn't exist!

        content = []
        with open(filename, 'r', encoding='utf-8') as fin:
            content = [l for l in fin]

        if not content:
            return True  # File is empty

        first = content[0]
        m = CHECKSUM_MATCHER.match(first)
        if not m:
            if not silent:
                log.warning('Checksum not found for file: %s - It may have been manually edited.', filename)
            return False  # Checksum not found!

        found_sum = m.group('checksum')
        file_sum = self.get_md5_hash(''.join(content[1:]))

        if not found_sum == file_sum:
            if not silent:
                log.warning('Checksum mismatch in file: %s - It may have been manually edited.', filename)
            return False  # Checksum mismatch!

        return True  # Otherwise we're good :)

    def is_grpc_file(self):
        if os.path.exists(self.get_grpc_file_name()):
            return True
        return False

    def write_rendered_file(self):
        self.write_dataclass_file()
        if self.service_map:
            self.write_api_file()
            if self.is_grpc_file():
                self.write_grpc_file()
                self.write_grpc_impl_file()
                # TODO(thordurm@ccpgames.com>): This is unnecessary
                # self.write_grpc_server_file()
            # TODO(thordurm@ccpgames.com>): This is unnecessary
            # self.write_impl_file()

    def write_file(self, file_name, content, silent=False):
        # TODO(thordurm@ccpgames.com>): Need to support generating multiple dicectories if needed
        # TODO(thordurm@ccpgames.com>): Need to ensure file paths make sense if proto modules are libraries
        checksum = self.get_md5_hash(content)
        if self.can_write(file_name, silent):
            with open(file_name, 'w', encoding='utf-8') as fout:
                fout.write(f'# md5: {checksum}\n')
                fout.write(content)

    #
    # Dataclass stuff!
    #

    def render_proto_import(self):
        return f'from {self.get_package()} import {self.get_module_name()} as pb2'

    def render_imports(self):
        import_set = set()
        for m in self.message_map.values():
            import_set.update(m.get_imports())
        if import_set:
            return '\n'.join(sorted(import_set)) + '\n'
        return ''

    def get_all_list(self) -> List[str]:
        all_list = [en.get_name() for en in self.enum_map.values()]
        all_list.extend([pc.get_class_name() for pc in self.message_map.values()])
        return all_list

    def render_dataclass_file(self):
        return TemplateRenderer().render_file('dataclass_module', **{
            'module_full_name': self.get_module_full_name(),
            'iso_timestamp': datetime.datetime.now().isoformat(),
            'imports': self.render_imports(),
            'proto_import': self.render_proto_import(),
            'enum_list': [en.render_py() for en in self.enum_map.values()],
            'message_list': [pc.render_py() for pc in self.message_map.values()],
            'all_list': self.get_all_list(),
        })

    def write_dataclass_file(self):
        self.write_file(self.get_render_file_name(), self.render_dataclass_file())

    #
    # GRPC SERVER FILE!
    #

    def write_grpc_server_file(self):
        b = servicebuilders.get_module_builder('grpc_server')(self)
        self.write_file(b.get_render_filename(), b.render(), silent=True)

    def render_grpc_server_file(self):
        return self.render('grpc_server')

    #
    # API FILE!
    #

    def write_api_file(self):
        b = servicebuilders.get_module_builder('interface')(self)
        self.write_file(b.get_render_filename(), b.render())

    def render_api_file(self):
        return self.render('interface')

    #
    # GRPC FILE! - grpc_receiver
    #

    def write_grpc_file(self):
        b = servicebuilders.get_module_builder('grpc_receiver')(self)
        self.write_file(b.get_render_filename(), b.render())

    def render_grpc_file(self):
        return self.render('grpc_receiver')

    #
    # GRPC IMPL FILE!
    #

    def write_grpc_impl_file(self):
        b = servicebuilders.get_module_builder('grpc_sender')(self)
        self.write_file(b.get_render_filename(), b.render())

    def render_grpc_impl_file(self):
        return self.render('grpc_sender')

    #
    # Implementation FILE!
    #

    def write_impl_file(self):
        b = servicebuilders.get_module_builder('implementation')(self)
        self.write_file(b.get_render_filename(), b.render(), silent=True)

    def render_impl_file(self):
        return self.render('implementation')

    #
    # Generic Render
    #

    def render(self, builder_name: str):
        return servicebuilders.get_module_builder(builder_name)(self).render()
