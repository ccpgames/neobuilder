from __future__ import annotations

__all__ = [
    'PyType',
    'PY_TYPE_MAP',
    'ProtoImport',
]

import os
import typing

from google.protobuf import json_format


from neobuilder.structs.pytype import *


class ProtoImport(object):
    def __init__(self, descriptor: typing.Union[json_format.descriptor.Descriptor, json_format.descriptor.EnumDescriptor], is_enum=False):
        self.descriptor = descriptor
        # noinspection PyUnresolvedReferences
        self.file_descriptor: json_format.descriptor.FileDescriptor = descriptor.file
        self.is_enum = is_enum

        self.name = self.descriptor.name

        self.module = f'{self.file_descriptor.name[:-6].replace("/", ".")}_dc'

    def get_full_class_name(self):
        return f'{self.get_module_full_name()}.{self.get_class_name()}'

    def get_class_name(self):
        return self.name

    def get_module_full_name(self):
        return self.module

    def get_module_name(self):
        return self.module.split('.')[-1]

    def get_module_name_parts(self):
        return self.module.split('.')

    def get_package(self):
        return self.module.rsplit('.', 1)[0]

    def get_file_full_name(self):
        return f"{self.module.replace('.', '/')}.py"

    def get_file_name(self):
        return os.path.basename(self.get_file_full_name())

    def get_file_path(self):
        return os.path.dirname(self.get_file_full_name())

    def get_name(self):
        return os.path.splitext(self.get_file_name())[0]

    def get_render_file_name(self):
        return f'{self.get_file_full_name()[:-7]}_dc.py'

    def get_import_name(self, used_in_file: json_format.descriptor.FileDescriptor = None):
        if used_in_file and used_in_file == self.descriptor.file:
            return 'dc'
        return self.get_module_full_name().replace('.', '__')

    def get_render_import(self, used_in_file: json_format.descriptor.FileDescriptor = None):
        return f'from {self.get_package()} import {self.get_module_name()} as {self.get_import_name(used_in_file)}'
