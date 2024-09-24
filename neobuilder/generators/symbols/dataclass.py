from __future__ import annotations
__all__ = [
    'ProtoClass',
    'ProtoField',
    'ProtoEnumValue',
    'ProtoEnum',
]

import typing

from neobuilder.descwrap import *

from google.protobuf import json_format
from google.protobuf import descriptor as pro_desc

from protoplasm.casting import castutils
from neobuilder.generators.symbols import modules
from neobuilder.generators.symbols import common


class ProtoClass(object):
    def __init__(self, descriptor: json_format.descriptor.Descriptor, module: modules.ProtoModule, parent_class: typing.Optional[object] = None, force_import=False):
        self.descriptor = descriptor
        self.module = module
        self.indent = module.indent
        self.enum_map: typing.Mapping[str, ProtoEnum] = {}
        self.field_map: typing.Mapping[str, ProtoField] = {}
        self.nested_message_map: typing.Mapping[str, ProtoClass] = {}
        self.parent_class: typing.Optional[ProtoClass] = parent_class
        self.force_import = force_import
        self.self_import = common.ProtoImport(self.descriptor)
        self._load_class()

    def _load_class(self):
        self.enum_map = {e.name: ProtoEnum(e, self.module, self) for e in self.descriptor.enum_types}
        self.field_map = {f.name: ProtoField(f, self, self.force_import) for f in self.descriptor.fields}
        self.nested_message_map = {}
        for n in self.descriptor.nested_types:
            if not (n.has_options and n.GetOptions().map_entry):
                self.nested_message_map[n.name] = ProtoClass(n, self.module, self)

    def get_class_lineage(self) -> str:
        path = self.get_class_name()
        if self.parent_class:
            path = f'{self.parent_class.get_class_lineage()}.{path}'
        return path

    def get_class_import_name(self):
        """
        :return: 'sandbox.test.delta_dc.DeltaMessage' => 'DeltaMessage'
        """
        return self.get_class_name()

    def get_class_name(self):
        """
        :return: 'sandbox.test.delta_dc.DeltaMessage' => 'DeltaMessage'
        """
        return self.descriptor.name

    def get_under_name(self):
        """
        :return: 'sandbox.test.delta_dc.DeltaMessage' => 'delta_message'
        """
        return castutils.humps_to_under(self.get_class_name())

    def get_proto_cls_name(self):
        """
        :return: 'sandbox.test.delta_dc.DeltaMessage' => 'DeltaMessage'
        """
        if self.parent_class:
            return f'{self.parent_class.get_proto_cls_name()}.{self.get_class_name()}'
        return self.get_class_name()

    def get_file_name(self):
        """
        :return: 'sandbox.test.delta_dc.DeltaMessage' => FileDescriptor('sandbox/test/delta.proto')
        """
        return self.descriptor.file

    def get_proto_module_name(self):
        """
        :return: 'sandbox.test.delta_dc.DeltaMessage' => 'service_with_imported_io_pb2'
        """
        return self.module.get_module_name()

    def get_imports(self):
        import_set = set()
        for f in self.field_map.values():
            if f.msg_import:
                import_set.add(f.msg_import.get_render_import())
        for c in self.nested_message_map.values():
            import_set.update(c.get_imports())
        return import_set

    def output_google_type_proxy(self):
        return {
            'Empty': 'typing.NoReturn'
        }.get(
            self.get_class_name()
        )

    def input_google_type_proxy(self):
        return {
            'Empty': 'None'
        }.get(
            self.get_class_name()
        )

    def protobuf_google_type_proxy(self):
        return f'{self.get_class_name().lower()}_pb2.{self.get_class_name()}'

    def render_dc_type_hint(self, relative_to: modules.ProtoModule = None) -> str:
        relative_to = relative_to or self.module
        if self.descriptor.file.package == 'google.protobuf':
            return self.output_google_type_proxy()
        if not relative_to or self.module.descriptor != self.self_import.descriptor.file:
            return_type = f'{self.self_import.get_import_name()}.{self.get_class_name()}'
            return return_type
        else:
            return f'dc.{self.get_class_name()}'

    def render_pb2_type_hint(self, relative_to: modules.ProtoModule = None) -> str:
        if self.descriptor.file.package == 'google.protobuf':
            return self.protobuf_google_type_proxy()
        else:
            relative_to = relative_to or self.module
            if not relative_to or self.module.descriptor != self.self_import.descriptor.file:
                return f'{self.self_import.get_import_name()}.pb2.{self.get_class_name()}'
            else:
                return f'dc.pb2.{self.get_class_name()}'

    def render_py(self, indent_level=0):
        buf = [
            f'{self.indent*indent_level}@dataclasses.dataclass\n',
            f'{self.indent*indent_level}class {self.get_class_name()}(plasm.DataclassBase):\n',
            f'{self.indent*(indent_level + 1)}__proto_cls__ = pb2.{self.get_proto_cls_name()}\n'
        ]
        if self.enum_map:
            for en in self.enum_map.values():
                buf.append(f'\n{en.render_py(indent_level + 1)}')
            buf.append('\n')

        if self.nested_message_map:
            for nm in self.nested_message_map.values():
                buf.append(f'\n{nm.render_py(indent_level + 1)}')
            buf.append('\n')

        for pf in self.field_map.values():
            buf.append(f'{pf.render_py(indent_level + 1)}\n')

        return ''.join(buf)

    def render_api_args(self, api_file: typing.Optional[pro_desc.FileDescriptor] = None):
        if self.field_map:
            return ', '.join([pf.render_arg_py(api_file or self.descriptor.file) for pf in self.field_map.values()])
        return ''

    def render_api_request_arg(self, method_desc: MethodDescriptorWrapper):
        if self.descriptor.file.package == 'google.protobuf':
            type_hint = self.input_google_type_proxy()
        else:
            type_hint = f'{self.self_import.get_import_name(method_desc.file_descriptor)}.{self.descriptor.name}'

        if method_desc.io_type.is_input_stream():
            return f', request_iterator: typing.Iterable[{type_hint}]'
        return f', {self.get_under_name()}: {type_hint}'

    def render_forwarded_args(self):
        if self.field_map:
            return ', '.join([pf.py_name() for pf in self.field_map.values()])
        return ''

    def _render_forwarded_args__BAD(self):
        return self.get_under_name()

    def render_api_return_args(self, api_file: typing.Optional[pro_desc.FileDescriptor] = None):
        if self.field_map:
            type_hint_list = [pf.get_type_hint(api_file or self.descriptor.file) for pf in self.field_map.values()]
            if len(type_hint_list) == 1:
                return type_hint_list[0]
            else:
                return f"typing.Tuple[{', '.join(type_hint_list)}]"
        return 'typing.NoReturn'

    def render_api_return_dataclass(self, api_file: typing.Optional[pro_desc.FileDescriptor] = None):
        if self.descriptor.file.package == 'google.protobuf':
            return self.output_google_type_proxy()
        return f'{self.self_import.get_import_name(api_file)}.{self.get_class_name()}'


class ProtoField(object):
    def __init__(self,
                 field_descriptor: json_format.descriptor.FieldDescriptor,
                 parent_class: ProtoClass,
                 force_import: bool = False):
        """
        :type field_descriptor: google.protobuf.descriptor.FieldDescriptor
        """
        self.field_descriptor = FieldDescriptorWrapper(field_descriptor)
        self.parent_class = parent_class
        self.indent = parent_class.indent
        self.force_import = force_import

        self.msg_import: typing.Optional[common.ProtoImport] = None

        if self.is_message() and not self.is_any():
            if self.force_import or self.field_descriptor.value_msg.file != self.parent_class.module.descriptor:
                self.msg_import = common.ProtoImport(self.field_descriptor.value_msg)

        if self.is_enum():
            if self.force_import or self.field_descriptor.value_field.enum_type.file != self.parent_class.module.descriptor:
                self.msg_import = common.ProtoImport(self.field_descriptor.value_field.enum_type)

    def is_proto_repeated(self) -> bool:
        return self.field_descriptor.is_proto_repeated

    def py_name(self):
        if self.is_keyword():
            return f'{self.field_descriptor.name}_'
        return self.field_descriptor.name

    def render_py(self, indent_level=0):
        return f'{self.indent*indent_level}{self.py_name()}: {self.get_type_hint()} = dataclasses.field({self.get_field_options()})'

    def render_arg_py(self, used_in_file: json_format.descriptor.FileDescriptor = None):
        return f'{self.py_name()}: {self.get_type_hint(used_in_file)} = None'

    def get_field_options(self):
        if self.is_struct():
            return f"default_factory=dict, metadata={{{self.get_metadata()}}}"
        elif self.is_map():
            return f"default_factory=dict, metadata={{{self.get_metadata()}}}"
        elif self.is_list():
            return f"default_factory=list, metadata={{{self.get_metadata()}}}"
        elif self.is_enum():
            # This breaks in the case of an internal class using internal enum
            # (e.g. eve.starbase.starbase_pb2.Settings)...
            #
            # enum_guy = self.get_py_type_name(self.field_descriptor.real_descriptor.file)
            # if self.field_descriptor.real_descriptor.file == self.field_descriptor.real_descriptor.enum_type.file:
            #     if '.' in enum_guy:  # Nested... break it!
            #         enum_guy = enum_guy[enum_guy.rindex('.')+1:]
            # return f"default={enum_guy}(0), metadata={{{self.get_metadata()}}}"
            #
            # ...so we'll just use 0 for now!
            return f"default=0, metadata={{{self.get_metadata()}}}"
        return f"default={self.field_descriptor.py_type.default_value}, metadata={{{self.get_metadata()}}}"

    def get_py_type(self) -> common.PyType:
        return self.field_descriptor.py_type

    def get_full_path(self, containing_type: pro_desc.Descriptor):
        def get_containing_type(value_msg: pro_desc.Descriptor):
            path = value_msg.name
            if value_msg.containing_type:
                path = f'{get_containing_type(value_msg.containing_type)}.{path}'
            return path
        return get_containing_type(containing_type)

    def get_py_module_name(self, used_in_file: json_format.descriptor.FileDescriptor = None) -> str:
        if self.msg_import:
            return f'{self.msg_import.get_import_name(used_in_file)}.'
        if self.is_enum() and self.field_descriptor.value_field.enum_type.containing_type:
            return f'{self.get_full_path(self.field_descriptor.value_field.enum_type.containing_type)}.'
        return ''

    def get_py_type_name(self, used_in_file: json_format.descriptor.FileDescriptor = None) -> str:
        if self.is_timestamp():
            return 'datetime.datetime'
        if self.is_duration():
            return 'datetime.timedelta'
        if self.is_any():
            return 'plasm.DataclassBase'
        if self.is_message():
            return f'{self.get_py_module_name(used_in_file)}{self.get_message_container_type()}'
        elif self.is_enum():
            return f'{self.get_py_module_name(used_in_file)}{self.field_descriptor.value_field.enum_type.name}'
        else:
            return self.field_descriptor.py_type.name

    def get_type_hint(self, used_in_file: json_format.descriptor.FileDescriptor = None) -> str:
        if self.is_struct():
            return f'typing.Dict[str, typing.Any]'
        elif self.is_map():
            return f'typing.Dict[{self.field_descriptor.key_py_type.name}, {self.get_py_type_name(used_in_file)}]'
        elif self.is_list():
            return f'typing.List[{self.get_py_type_name(used_in_file)}]'
        elif self.is_empty():
            return f'None'
        return self.get_py_type_name(used_in_file)

    def get_message_container_type(self) -> str:
        def get_containing_type(value_msg: pro_desc.Descriptor):
            path = value_msg.name
            if value_msg.containing_type:
                path = f'{get_containing_type(value_msg.containing_type)}.{path}'
            return path
        return get_containing_type(self.field_descriptor.value_msg)

    def get_metadata(self):
        buf = [f"'dictator': dictators.{self.get_dictator_name()}"]
        if self.is_map():
            buf.append("'is_map': True")
        elif self.is_list():
            buf.append("'is_list': True")

        if self.is_struct():
            buf.append("'is_struct': True")
        elif self.is_message():
            buf.append("'is_obj': True")
        elif self.is_enum():
            buf.append("'is_enum': True")

        if self.is_keyword():
            buf.append(f"'pb_name': '{self.field_descriptor.name}'")

        return ', '.join(buf)

    def get_dictator_name(self):
        if self.is_empty():
            return 'EmptyDictator'
        if self.is_any():
            return 'AnyDictator'
        if self.is_timestamp():
            return 'TimestampDictator'
        if self.is_duration():
            return 'DurationDictator'
        if self.is_bytes():
            return 'ByteDictator'
        if self.is_enum():
            return 'EnumDictator'
        if self.is_long():
            return 'LongDictator'
        if self.is_struct():
            return 'StructDictator'
        return 'BaseDictator'

    def is_long(self):
        return bool(self.field_descriptor.kind & FieldKind.SPECIAL_LONG)

    def is_timestamp(self):
        return bool(self.field_descriptor.kind & FieldKind.SPECIAL_TIMESTAMP)

    def is_struct(self):
        return bool(self.field_descriptor.kind & FieldKind.SPECIAL_STRUCT)

    def is_duration(self):
        return bool(self.field_descriptor.kind & FieldKind.SPECIAL_DURATION)

    def is_any(self):
        return bool(self.field_descriptor.kind & FieldKind.SPECIAL_ANY)

    def is_empty(self):
        return bool(self.field_descriptor.kind & FieldKind.SPECIAL_EMPTY)

    def is_bytes(self):
        return bool(self.field_descriptor.kind & FieldKind.SPECIAL_BYTES)

    def is_single(self):
        return bool(self.field_descriptor.kind & FieldKind.KIND_SINGLE)

    def is_map(self):
        return bool(self.field_descriptor.kind & FieldKind.KIND_MAP)

    def is_list(self):
        return bool(self.field_descriptor.kind & FieldKind.KIND_LIST)

    def is_scalar(self):
        return bool(self.field_descriptor.kind & FieldKind.DATA_SCALAR)

    def is_message(self):
        return bool(self.field_descriptor.kind & FieldKind.DATA_MESSAGE)

    def is_enum(self):
        return bool(self.field_descriptor.kind & FieldKind.DATA_ENUM)

    def is_keyword(self):
        return bool(self.field_descriptor.kind & FieldKind.SPECIAL_KEYWORD)


class ProtoEnumValue(object):
    def __init__(self, descriptor: json_format.descriptor.EnumValueDescriptor):
        self.descriptor = descriptor

    def get_name(self):
        return self.descriptor.name

    def get_value(self):
        return self.descriptor.number

    def render_py(self):
        return f'{self.get_name()} = {self.get_value()}'


class ProtoEnum(object):
    def __init__(self, descriptor: json_format.descriptor.EnumDescriptor, module: modules.ProtoModule, parent_class: typing.Optional[ProtoClass] = None):
        self.descriptor = descriptor
        self.module = module
        self.parent_class = parent_class
        self.indent = module.indent

    def get_name(self):
        return self.descriptor.name

    def get_class_import_name(self):
        buf = []
        if self.parent_class:
            buf.append(self.parent_class.get_class_lineage())
        buf.append(self.get_name())
        return '.'.join(buf)

    def render_py_consts(self, indent_level=0):
        buf = []
        for v in reversed(self.descriptor.values):  # Reversing order to ensure default Alias render correctly
            pv = ProtoEnumValue(v)
            buf.append(f'{self.indent*indent_level}{pv.get_name()} = {self.get_name()}({pv.get_value()})\n')
        return ''.join(buf)

    def render_py_class(self, indent_level=0):
        buf = [
            f'{self.indent*indent_level}class {self.get_name()}(enum.IntEnum):\n',
            f'{self.indent*(indent_level + 1)}__proto_cls__ = pb2.{self.get_class_import_name()}\n'
        ]
        for v in reversed(self.descriptor.values):  # Reversing order to ensure default Alias render correctly
            pv = ProtoEnumValue(v)
            buf.append(f'{self.indent*(indent_level + 1)}{pv.render_py()}\n')
        return ''.join(buf)

    def render_py(self, indent_level=0):
        buf = [
            self.render_py_class(indent_level),
            '\n' if self.parent_class else '\n\n',
            self.render_py_consts(indent_level)
        ]
        return ''.join(buf)
