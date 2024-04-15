__all__ = [
    'ProtoType',
    'PyType',
    'PY_TYPE_MAP',
]
from google.protobuf.json_format import descriptor
from typing import *
import enum


class ProtoType(enum.IntEnum):
    UNKNOWN = -42
    DOUBLE = descriptor.FieldDescriptor.TYPE_DOUBLE  # 1
    FLOAT = descriptor.FieldDescriptor.TYPE_FLOAT  # 2
    INT64 = descriptor.FieldDescriptor.TYPE_INT64  # 3
    UINT64 = descriptor.FieldDescriptor.TYPE_UINT64  # 4
    INT32 = descriptor.FieldDescriptor.TYPE_INT32  # 5
    FIXED64 = descriptor.FieldDescriptor.TYPE_FIXED64  # 6
    FIXED32 = descriptor.FieldDescriptor.TYPE_FIXED32  # 7
    BOOL = descriptor.FieldDescriptor.TYPE_BOOL  # 8
    STRING = descriptor.FieldDescriptor.TYPE_STRING  # 9
    BYTES = descriptor.FieldDescriptor.TYPE_BYTES  # 12
    UINT32 = descriptor.FieldDescriptor.TYPE_UINT32  # 13
    SFIXED32 = descriptor.FieldDescriptor.TYPE_SFIXED32  # 15
    SFIXED64 = descriptor.FieldDescriptor.TYPE_SFIXED64  # 16
    SINT32 = descriptor.FieldDescriptor.TYPE_SINT32  # 17
    SINT64 = descriptor.FieldDescriptor.TYPE_SINT64  # 18

    GROUP = descriptor.FieldDescriptor.TYPE_GROUP  # 10
    MESSAGE = descriptor.FieldDescriptor.TYPE_MESSAGE  # 11
    ENUM = descriptor.FieldDescriptor.TYPE_ENUM  # 14

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'{self.name}({self.value})'


class PyType:
    __slots__ = ('proto_type', 'py_name', 'default_value')

    def __init__(self, proto_type: Union[ProtoType, int], py_name: str, default_value: str):
        if isinstance(proto_type, int):
            proto_type = ProtoType(proto_type)
        self.proto_type = proto_type
        self.py_name = py_name
        self.default_value = default_value

    def __str__(self) -> str:
        return self.py_name

    def __repr__(self) -> str:
        if self.proto_type == ProtoType.UNKNOWN:
            return '?'
        return f'{self.proto_type!s}->{self.py_name}'

    # For backwards compatibility
    @property
    def number(self) -> int:
        return self.proto_type.value

    # For backwards compatibility
    @property
    def name(self) -> str:
        return self.py_name


PY_TYPE_MAP = {
    ProtoType.DOUBLE: PyType(ProtoType.DOUBLE, 'float', '0.0'),
    ProtoType.FLOAT: PyType(ProtoType.FLOAT, 'float', '0.0'),
    ProtoType.INT64: PyType(ProtoType.INT64, 'int', '0'),
    ProtoType.UINT64: PyType(ProtoType.UINT64, 'int', '0'),
    ProtoType.INT32: PyType(ProtoType.INT32, 'int', '0'),
    ProtoType.FIXED64: PyType(ProtoType.FIXED64, 'int', '0'),
    ProtoType.FIXED32: PyType(ProtoType.FIXED32, 'int', '0'),
    ProtoType.BOOL: PyType(ProtoType.BOOL, 'bool', 'False'),
    ProtoType.STRING: PyType(ProtoType.STRING, 'str', "''"),
    ProtoType.BYTES: PyType(ProtoType.BYTES, 'bytes', "b''"),
    ProtoType.UINT32: PyType(ProtoType.UINT32, 'int', '0'),
    ProtoType.SFIXED32: PyType(ProtoType.SFIXED32, 'int', '0'),
    ProtoType.SFIXED64: PyType(ProtoType.SFIXED64, 'int', '0'),
    ProtoType.SINT32: PyType(ProtoType.SINT32, 'int', '0'),
    ProtoType.SINT64: PyType(ProtoType.SINT64, 'int', '0'),

    # PyType.GROUP: PyType(PyType.GROUP, 'Group'),  # ?!?
    ProtoType.MESSAGE: PyType(ProtoType.MESSAGE, 'Message', 'None'),
    ProtoType.ENUM: PyType(ProtoType.ENUM, 'Enum', '0'),

    ProtoType.UNKNOWN: PyType(ProtoType.UNKNOWN, '?', 'None'),
}
