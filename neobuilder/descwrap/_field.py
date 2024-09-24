__all__ = [
    'FieldKind',
    'FieldDescriptorWrapper',
]
import dataclasses
import enum
from typing import *
import keyword
from google.protobuf.json_format import descriptor
from google.protobuf import json_format
from neobuilder.structs.pytype import *


class FieldKind(enum.IntFlag):
    UNKNOWN             = 0x0000
    DATA_SCALAR         = 0x0001
    DATA_MESSAGE        = 0x0002
    DATA_ENUM           = 0x0004

    KIND_SINGLE         = 0x0010
    KIND_LIST           = 0x0020
    KIND_MAP            = 0x0040

    SPECIAL_TIMESTAMP   = 0x00100
    SPECIAL_BYTES       = 0x00200
    SPECIAL_LONG        = 0x00400
    SPECIAL_DURATION    = 0x00800
    SPECIAL_ANY         = 0x01000
    SPECIAL_EMPTY       = 0x02000
    SPECIAL_STRUCT      = 0x04000
    SPECIAL_VALUE       = 0x08000
    SPECIAL_LIST_VALUE  = 0x10000
    SPECIAL_NULL_VALUE  = 0x20000

    SPECIAL_KEYWORD     = 0x10000000

    # scalar
    FIELD_SIMPLE = DATA_SCALAR | KIND_SINGLE
    # Message
    FIELD_MESSAGE = DATA_MESSAGE | KIND_SINGLE
    # Enum
    FIELD_ENUM = DATA_ENUM | KIND_SINGLE

    # repeated scalar
    FIELD_SIMPLE_LIST = DATA_SCALAR | KIND_LIST
    # repeated Message
    FIELD_MESSAGE_LIST = DATA_MESSAGE | KIND_LIST
    # repeated Enum
    FIELD_ENUM_LIST = DATA_ENUM | KIND_LIST

    # map<scalar, scalar>
    FIELD_SIMPLE_MAP = DATA_SCALAR | KIND_MAP
    # map<scalar, Message>
    FIELD_MESSAGE_MAP = DATA_MESSAGE | KIND_MAP
    # map<scalar, Enum>
    FIELD_ENUM_MAP = DATA_ENUM | KIND_MAP

    FIELD_STRUCT_VALUES = SPECIAL_STRUCT | SPECIAL_VALUE | SPECIAL_LIST_VALUE | SPECIAL_NULL_VALUE

    def __repr__(self) -> str:
        return self.name or str(self.value)


@dataclasses.dataclass
class FieldDescriptorWrapper:
    """This is a wrapper around Google's protobuf FieldDescriptor.

    Its point is twofold.

    1. To mask complex lookups and evaluations behind a simpler facade to use
       in the rest of the code.
    2. To abstract away the exact structure of Google's descriptor to guard
       against future code changes, especially in internal parts that aren't
       part of the official API.
    """
    real_descriptor: descriptor.FieldDescriptor = dataclasses.field(repr=False)

    name: str = dataclasses.field(default='', init=False)

    kind: FieldKind = dataclasses.field(default=FieldKind.UNKNOWN, init=False)

    options: Optional[Any] = dataclasses.field(default=None, init=False, repr=False)

    key_field: Optional[descriptor.FieldDescriptor] = dataclasses.field(default=None, init=False, repr=False)
    value_field: Optional[descriptor.FieldDescriptor] = dataclasses.field(default=None, init=False, repr=False)
    value_msg: Optional[descriptor.Descriptor] = dataclasses.field(default=None, init=False, repr=False)

    py_type: PyType = dataclasses.field(default=PY_TYPE_MAP[ProtoType.UNKNOWN], init=False)
    key_py_type: PyType = dataclasses.field(default=PY_TYPE_MAP[ProtoType.UNKNOWN], init=False)

    is_proto_repeated: bool = dataclasses.field(default=False, init=False)

    def __post_init__(self):
        self.name = self.real_descriptor.name
        self.is_proto_repeated = self.real_descriptor.label == descriptor.FieldDescriptor.LABEL_REPEATED
        self._check_field_kind()

    def _load_options(self):
        self.options = None
        if self.real_descriptor.type == ProtoType.MESSAGE:
            if self.real_descriptor.message_type.has_options:
                self.options = self.real_descriptor.message_type.GetOptions()

    def _check_field_kind(self):
        self._load_options()

        if self.options and self.options.map_entry:  # Message that is a map...
            self.key_field = self.real_descriptor.message_type.fields_by_name['key']
            self.key_py_type = PY_TYPE_MAP[self.key_field.type]
            self.value_field = self.real_descriptor.message_type.fields_by_name['value']
            self.kind |= FieldKind.KIND_MAP
        else:
            self.value_field = self.real_descriptor
            if self.is_proto_repeated:
                self.kind |= FieldKind.KIND_LIST
            else:
                self.kind |= FieldKind.KIND_SINGLE

        if self.value_field.type == ProtoType.MESSAGE:  # Message
            self.value_msg = self.value_field.message_type

            if self.value_msg.full_name == 'google.protobuf.Timestamp':
                self.kind |= FieldKind.DATA_SCALAR
                self.kind |= FieldKind.SPECIAL_TIMESTAMP
            elif self.value_msg.full_name == 'google.protobuf.Duration':
                self.kind |= FieldKind.DATA_SCALAR
                self.kind |= FieldKind.SPECIAL_DURATION
            elif self.value_msg.full_name == 'google.protobuf.Any':
                self.kind |= FieldKind.DATA_SCALAR
                self.kind |= FieldKind.SPECIAL_ANY
            elif self.value_msg.full_name == 'google.protobuf.Empty':
                self.kind |= FieldKind.SPECIAL_EMPTY
            elif self.value_msg.full_name == 'google.protobuf.Struct':
                self.kind |= FieldKind.SPECIAL_STRUCT
            elif self.value_msg.full_name == 'google.protobuf.Value':
                self.kind |= FieldKind.SPECIAL_VALUE
            elif self.value_msg.full_name == 'google.protobuf.ListValue':
                self.kind |= FieldKind.SPECIAL_LIST_VALUE
            elif self.value_msg.full_name == 'google.protobuf.NullValue':
                self.kind |= FieldKind.SPECIAL_NULL_VALUE
            else:
                self.kind |= FieldKind.DATA_MESSAGE
        elif self.value_field.type == ProtoType.ENUM:  # Enum
            self.kind |= FieldKind.DATA_ENUM

        else:  # Scalar
            self.kind |= FieldKind.DATA_SCALAR

            if self.value_field.type == ProtoType.BYTES:
                self.kind |= FieldKind.SPECIAL_BYTES
            else:
                if self.value_field.cpp_type in json_format._INT64_TYPES:
                    self.kind |= FieldKind.SPECIAL_LONG

        self.py_type = PY_TYPE_MAP[self.value_field.type]

        if keyword.iskeyword(self.name):
            self.kind |= FieldKind.SPECIAL_KEYWORD

    @property
    def camelcase_name(self) -> str:
        return self.real_descriptor.camelcase_name

    @property
    def json_name(self) -> str:
        return self.real_descriptor.json_name

    @property
    def default_value(self) -> Any:
        return self.real_descriptor.default_value

    @property
    def full_name(self) -> Any:
        return self.real_descriptor.full_name


# def main():
#     fields = []
#     from sandbox.test import RainbowMessage
#     for f in RainbowMessage.DESCRIPTOR.fields:
#         ff = FieldDescriptorWrapper(f)
#         print(ff)
#         fields.append(ff)
#
#     # print(fields)
#
# if __name__ == '__main__':
#     main()
