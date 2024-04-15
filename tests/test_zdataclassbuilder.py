import unittest
import os
import sys
from neobuilder.neobuilder import NeoBuilder
import shutil
import time
import neobuilder.generators.symbols
import neobuilder.generators.symbols.dataclass
import neobuilder.generators.symbols.modules

HERE = os.path.dirname(__file__)
BUILD_ROOT = os.path.join(HERE, 'res', 'build')
PROTO_ROOT = os.path.join(HERE, 'res', 'proto')

import logging
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class ProtoFieldTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Remove old stuff...
        build_package = os.path.join(BUILD_ROOT, 'sandbox')
        if os.path.exists(build_package):
            shutil.rmtree(build_package)
            time.sleep(0.1)

        # Build stuff...
        builder = NeoBuilder(package='sandbox',
                             protopath=PROTO_ROOT,
                             build_root=BUILD_ROOT)
        builder.build()

        sys.path.append(BUILD_ROOT)

    def test_rainbow_simple_field(self):
        from sandbox.test import rainbow_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(rainbow_pb2.RainbowMessage.DESCRIPTOR, neobuilder.generators.symbols.modules.ProtoModule(rainbow_pb2))
        proto_field = neobuilder.generators.symbols.dataclass.ProtoField(proto_class.descriptor.fields_by_name['simple_field'], proto_class)

        self.assertTrue(proto_field.is_single())
        self.assertFalse(proto_field.is_list())
        self.assertFalse(proto_field.is_map())

        self.assertFalse(proto_field.field_descriptor.is_proto_repeated)

        self.assertTrue(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())

        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())
        self.assertFalse(proto_field.is_enum())

        self.assertEqual('simple_field', proto_field.py_name())
        self.assertEqual('str', proto_field.get_type_hint())
        self.assertEqual('BaseDictator', proto_field.get_dictator_name())
        self.assertEqual("'dictator': dictators.BaseDictator", proto_field.get_metadata())
        self.assertEqual("simple_field: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})", proto_field.render_py())

    def test_rainbow_message_field(self):
        from sandbox.test import rainbow_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(rainbow_pb2.RainbowMessage.DESCRIPTOR, neobuilder.generators.symbols.modules.ProtoModule(rainbow_pb2))
        proto_field = neobuilder.generators.symbols.dataclass.ProtoField(proto_class.descriptor.fields_by_name['message_field'], proto_class)

        self.assertTrue(proto_field.is_single())
        self.assertFalse(proto_field.is_list())
        self.assertFalse(proto_field.is_map())

        self.assertFalse(proto_field.is_proto_repeated())

        self.assertFalse(proto_field.is_scalar())
        self.assertTrue(proto_field.is_message())

        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())
        self.assertFalse(proto_field.is_enum())

        self.assertEqual('message_field', proto_field.py_name())
        self.assertEqual('SubMessage', proto_field.get_type_hint())
        self.assertEqual('BaseDictator', proto_field.get_dictator_name())
        self.assertEqual("'dictator': dictators.BaseDictator, 'is_obj': True", proto_field.get_metadata())
        self.assertEqual("message_field: SubMessage = dataclasses.field(default=None, metadata={'dictator': dictators.BaseDictator, 'is_obj': True})", proto_field.render_py())

    def test_rainbow_simple_list(self):
        from sandbox.test import rainbow_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(rainbow_pb2.RainbowMessage.DESCRIPTOR, neobuilder.generators.symbols.modules.ProtoModule(rainbow_pb2))
        proto_field = neobuilder.generators.symbols.dataclass.ProtoField(proto_class.descriptor.fields_by_name['simple_list'], proto_class)

        self.assertFalse(proto_field.is_single())
        self.assertTrue(proto_field.is_list())
        self.assertFalse(proto_field.is_map())

        self.assertTrue(proto_field.is_proto_repeated())

        self.assertTrue(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())

        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())
        self.assertFalse(proto_field.is_enum())

        self.assertEqual('simple_list', proto_field.py_name())
        self.assertEqual('List[str]', proto_field.get_type_hint())
        self.assertEqual('BaseDictator', proto_field.get_dictator_name())
        self.assertEqual("'dictator': dictators.BaseDictator, 'is_list': True", proto_field.get_metadata())
        self.assertEqual("simple_list: List[str] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})", proto_field.render_py())

    def test_rainbow_message_list(self):
        from sandbox.test import rainbow_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(rainbow_pb2.RainbowMessage.DESCRIPTOR, neobuilder.generators.symbols.modules.ProtoModule(rainbow_pb2))
        proto_field = neobuilder.generators.symbols.dataclass.ProtoField(proto_class.descriptor.fields_by_name['message_list'], proto_class)

        self.assertFalse(proto_field.is_single())
        self.assertTrue(proto_field.is_list())
        self.assertFalse(proto_field.is_map())

        self.assertTrue(proto_field.is_proto_repeated())

        self.assertFalse(proto_field.is_scalar())
        self.assertTrue(proto_field.is_message())

        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())
        self.assertFalse(proto_field.is_enum())

        self.assertEqual('message_list', proto_field.py_name())
        self.assertEqual('List[SubMessage]', proto_field.get_type_hint())
        self.assertEqual('BaseDictator', proto_field.get_dictator_name())
        self.assertEqual("'dictator': dictators.BaseDictator, 'is_list': True, 'is_obj': True", proto_field.get_metadata())
        self.assertEqual("message_list: List[SubMessage] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True, 'is_obj': True})", proto_field.render_py())

    def test_rainbow_simple_map(self):
        from sandbox.test import rainbow_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(rainbow_pb2.RainbowMessage.DESCRIPTOR, neobuilder.generators.symbols.modules.ProtoModule(rainbow_pb2))
        proto_field = neobuilder.generators.symbols.dataclass.ProtoField(proto_class.descriptor.fields_by_name['simple_map'], proto_class)

        self.assertFalse(proto_field.is_single())
        self.assertFalse(proto_field.is_list())
        self.assertTrue(proto_field.is_map())

        self.assertTrue(proto_field.is_proto_repeated())

        self.assertTrue(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())

        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())
        self.assertFalse(proto_field.is_enum())

        self.assertEqual('simple_map', proto_field.py_name())
        self.assertEqual('Dict[str, str]', proto_field.get_type_hint())
        self.assertEqual('BaseDictator', proto_field.get_dictator_name())
        self.assertEqual("'dictator': dictators.BaseDictator, 'is_map': True", proto_field.get_metadata())
        self.assertEqual("simple_map: Dict[str, str] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})", proto_field.render_py())

    def test_rainbow_message_map(self):
        from sandbox.test import rainbow_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(rainbow_pb2.RainbowMessage.DESCRIPTOR, neobuilder.generators.symbols.modules.ProtoModule(rainbow_pb2))
        proto_field = neobuilder.generators.symbols.dataclass.ProtoField(proto_class.descriptor.fields_by_name['message_map'], proto_class)

        self.assertFalse(proto_field.is_single())
        self.assertFalse(proto_field.is_list())
        self.assertTrue(proto_field.is_map())

        self.assertTrue(proto_field.is_proto_repeated())

        self.assertFalse(proto_field.is_scalar())
        self.assertTrue(proto_field.is_message())

        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())
        self.assertFalse(proto_field.is_enum())

        self.assertEqual('message_map', proto_field.py_name())
        self.assertEqual('Dict[str, SubMessage]', proto_field.get_type_hint())
        self.assertEqual('BaseDictator', proto_field.get_dictator_name())
        self.assertEqual("'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True", proto_field.get_metadata())
        self.assertEqual("message_map: Dict[str, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})", proto_field.render_py())

    def test_timestamp(self):
        from sandbox.test import rainbow_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(rainbow_pb2.TimestampMessage.DESCRIPTOR, neobuilder.generators.symbols.modules.ProtoModule(rainbow_pb2))
        proto_field = neobuilder.generators.symbols.dataclass.ProtoField(proto_class.descriptor.fields_by_name['my_timestamp'], proto_class)

        self.assertTrue(proto_field.is_single())
        self.assertFalse(proto_field.is_list())
        self.assertFalse(proto_field.is_map())

        self.assertFalse(proto_field.is_proto_repeated())

        self.assertTrue(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())

        self.assertTrue(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())
        self.assertFalse(proto_field.is_enum())

        self.assertEqual('my_timestamp', proto_field.py_name())
        self.assertEqual('datetime.datetime', proto_field.get_type_hint())
        self.assertEqual('TimestampDictator', proto_field.get_dictator_name())
        self.assertEqual("'dictator': dictators.TimestampDictator", proto_field.get_metadata())
        self.assertEqual("my_timestamp: datetime.datetime = dataclasses.field(default=None, metadata={'dictator': dictators.TimestampDictator})", proto_field.render_py())

    def test_timestamp_list(self):
        from sandbox.test import rainbow_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(rainbow_pb2.TimestampMessage.DESCRIPTOR, neobuilder.generators.symbols.modules.ProtoModule(rainbow_pb2))
        proto_field = neobuilder.generators.symbols.dataclass.ProtoField(proto_class.descriptor.fields_by_name['my_timestamp_list'], proto_class)

        self.assertFalse(proto_field.is_single())
        self.assertTrue(proto_field.is_list())
        self.assertFalse(proto_field.is_map())

        self.assertTrue(proto_field.is_proto_repeated())

        self.assertTrue(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())

        self.assertTrue(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())
        self.assertFalse(proto_field.is_enum())

        self.assertEqual('my_timestamp_list', proto_field.py_name())
        self.assertEqual('List[datetime.datetime]', proto_field.get_type_hint())
        self.assertEqual('TimestampDictator', proto_field.get_dictator_name())
        self.assertEqual("'dictator': dictators.TimestampDictator, 'is_list': True", proto_field.get_metadata())
        self.assertEqual("my_timestamp_list: List[datetime.datetime] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.TimestampDictator, 'is_list': True})", proto_field.render_py())

    def test_timestamp_map(self):
        from sandbox.test import rainbow_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(rainbow_pb2.TimestampMessage.DESCRIPTOR, neobuilder.generators.symbols.modules.ProtoModule(rainbow_pb2))
        proto_field = neobuilder.generators.symbols.dataclass.ProtoField(proto_class.descriptor.fields_by_name['my_timestamp_map'], proto_class)

        self.assertFalse(proto_field.is_single())
        self.assertFalse(proto_field.is_list())
        self.assertTrue(proto_field.is_map())

        self.assertTrue(proto_field.is_proto_repeated())

        self.assertTrue(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())

        self.assertTrue(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())
        self.assertFalse(proto_field.is_enum())

        self.assertEqual('my_timestamp_map', proto_field.py_name())
        self.assertEqual('Dict[str, datetime.datetime]', proto_field.get_type_hint())
        self.assertEqual('TimestampDictator', proto_field.get_dictator_name())
        self.assertEqual("'dictator': dictators.TimestampDictator, 'is_map': True", proto_field.get_metadata())
        self.assertEqual("my_timestamp_map: Dict[str, datetime.datetime] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.TimestampDictator, 'is_map': True})", proto_field.render_py())

    def test_bytes(self):
        from sandbox.test import rainbow_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(rainbow_pb2.BytesMessage.DESCRIPTOR, neobuilder.generators.symbols.modules.ProtoModule(rainbow_pb2))
        proto_field = neobuilder.generators.symbols.dataclass.ProtoField(proto_class.descriptor.fields_by_name['my_bytes'], proto_class)

        self.assertTrue(proto_field.is_single())
        self.assertFalse(proto_field.is_list())
        self.assertFalse(proto_field.is_map())

        self.assertFalse(proto_field.is_proto_repeated())

        self.assertTrue(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())

        self.assertFalse(proto_field.is_timestamp())
        self.assertTrue(proto_field.is_bytes())

        self.assertEqual('my_bytes', proto_field.py_name())
        self.assertEqual('bytes', proto_field.get_type_hint())
        self.assertEqual('ByteDictator', proto_field.get_dictator_name())
        self.assertEqual("'dictator': dictators.ByteDictator", proto_field.get_metadata())
        self.assertEqual("my_bytes: bytes = dataclasses.field(default=b'', metadata={'dictator': dictators.ByteDictator})", proto_field.render_py())

    def test_bytes_list(self):
        from sandbox.test import rainbow_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(rainbow_pb2.BytesMessage.DESCRIPTOR, neobuilder.generators.symbols.modules.ProtoModule(rainbow_pb2))
        proto_field = neobuilder.generators.symbols.dataclass.ProtoField(proto_class.descriptor.fields_by_name['my_bytes_list'], proto_class)

        self.assertFalse(proto_field.is_single())
        self.assertTrue(proto_field.is_list())
        self.assertFalse(proto_field.is_map())

        self.assertTrue(proto_field.is_proto_repeated())

        self.assertTrue(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())

        self.assertFalse(proto_field.is_timestamp())
        self.assertTrue(proto_field.is_bytes())
        self.assertFalse(proto_field.is_enum())

        self.assertEqual('my_bytes_list', proto_field.py_name())
        self.assertEqual('List[bytes]', proto_field.get_type_hint())
        self.assertEqual('ByteDictator', proto_field.get_dictator_name())
        self.assertEqual("'dictator': dictators.ByteDictator, 'is_list': True", proto_field.get_metadata())
        self.assertEqual("my_bytes_list: List[bytes] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.ByteDictator, 'is_list': True})", proto_field.render_py())

    def test_bytes_map(self):
        from sandbox.test import rainbow_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(rainbow_pb2.BytesMessage.DESCRIPTOR, neobuilder.generators.symbols.modules.ProtoModule(rainbow_pb2))
        proto_field = neobuilder.generators.symbols.dataclass.ProtoField(proto_class.descriptor.fields_by_name['my_bytes_map'], proto_class)

        self.assertFalse(proto_field.is_single())
        self.assertFalse(proto_field.is_list())
        self.assertTrue(proto_field.is_map())

        self.assertTrue(proto_field.is_proto_repeated())

        self.assertTrue(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())

        self.assertFalse(proto_field.is_timestamp())
        self.assertTrue(proto_field.is_bytes())
        self.assertFalse(proto_field.is_enum())

        self.assertEqual('my_bytes_map', proto_field.py_name())
        self.assertEqual('Dict[str, bytes]', proto_field.get_type_hint())
        self.assertEqual('ByteDictator', proto_field.get_dictator_name())
        self.assertEqual("'dictator': dictators.ByteDictator, 'is_map': True", proto_field.get_metadata())
        self.assertEqual("my_bytes_map: Dict[str, bytes] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.ByteDictator, 'is_map': True})", proto_field.render_py())

    def test_all_types(self):
        from sandbox.test import rainbow_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(rainbow_pb2.AllTypes.DESCRIPTOR, neobuilder.generators.symbols.modules.ProtoModule(rainbow_pb2))
        class_string = proto_class.render_py().strip()
        expected = """@dataclasses.dataclass
class AllTypes(plasm.DataclassBase):
    __proto_cls__ = pb2.AllTypes
    my_string: str = dataclasses.field(default='', metadata={'dictator': dictators.BaseDictator})
    my_float: float = dataclasses.field(default=0.0, metadata={'dictator': dictators.BaseDictator})
    my_double: float = dataclasses.field(default=0.0, metadata={'dictator': dictators.BaseDictator})
    my_int32: int = dataclasses.field(default=0, metadata={'dictator': dictators.BaseDictator})
    my_int64: int = dataclasses.field(default=0, metadata={'dictator': dictators.LongDictator})
    my_uint32: int = dataclasses.field(default=0, metadata={'dictator': dictators.BaseDictator})
    my_uint64: int = dataclasses.field(default=0, metadata={'dictator': dictators.LongDictator})
    my_sint32: int = dataclasses.field(default=0, metadata={'dictator': dictators.BaseDictator})
    my_sint64: int = dataclasses.field(default=0, metadata={'dictator': dictators.LongDictator})
    my_fixed32: int = dataclasses.field(default=0, metadata={'dictator': dictators.BaseDictator})
    my_fixed64: int = dataclasses.field(default=0, metadata={'dictator': dictators.LongDictator})
    my_sfixed32: int = dataclasses.field(default=0, metadata={'dictator': dictators.BaseDictator})
    my_sfixed64: int = dataclasses.field(default=0, metadata={'dictator': dictators.LongDictator})
    my_bool: bool = dataclasses.field(default=False, metadata={'dictator': dictators.BaseDictator})
    my_bytes: bytes = dataclasses.field(default=b'', metadata={'dictator': dictators.ByteDictator})"""
        self.assertEqual(expected, class_string)

    def test_all_types_list(self):
        from sandbox.test import rainbow_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(rainbow_pb2.AllTypesList.DESCRIPTOR, neobuilder.generators.symbols.modules.ProtoModule(rainbow_pb2))
        class_string = proto_class.render_py().strip()
        expected = """@dataclasses.dataclass
class AllTypesList(plasm.DataclassBase):
    __proto_cls__ = pb2.AllTypesList
    my_string_list: List[str] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_float_list: List[float] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_double_list: List[float] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_int32_list: List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_int64_list: List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.LongDictator, 'is_list': True})
    my_uint32_list: List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_uint64_list: List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.LongDictator, 'is_list': True})
    my_sint32_list: List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_sint64_list: List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.LongDictator, 'is_list': True})
    my_fixed32_list: List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_fixed64_list: List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.LongDictator, 'is_list': True})
    my_sfixed32_list: List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_sfixed64_list: List[int] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.LongDictator, 'is_list': True})
    my_bool_list: List[bool] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.BaseDictator, 'is_list': True})
    my_bytes_list: List[bytes] = dataclasses.field(default_factory=list, metadata={'dictator': dictators.ByteDictator, 'is_list': True})"""
        self.assertEqual(expected, class_string)

    def test_all_types_map(self):
        from sandbox.test import rainbow_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(rainbow_pb2.AllTypesMap.DESCRIPTOR, neobuilder.generators.symbols.modules.ProtoModule(rainbow_pb2))
        class_string = proto_class.render_py().strip()
        expected = """@dataclasses.dataclass
class AllTypesMap(plasm.DataclassBase):
    __proto_cls__ = pb2.AllTypesMap
    my_string_map: Dict[str, str] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})
    my_int32_map: Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})
    my_int64_map: Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.LongDictator, 'is_map': True})
    my_uint32_map: Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})
    my_uint64_map: Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.LongDictator, 'is_map': True})
    my_sint32_map: Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})
    my_sint64_map: Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.LongDictator, 'is_map': True})
    my_fixed32_map: Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})
    my_fixed64_map: Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.LongDictator, 'is_map': True})
    my_sfixed32_map: Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})
    my_sfixed64_map: Dict[int, int] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.LongDictator, 'is_map': True})
    my_bool_map: Dict[bool, bool] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True})"""
        self.assertEqual(expected, class_string)

    def test_all_types_nested_map(self):
        from sandbox.test import rainbow_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(rainbow_pb2.AllTypesNestedMap.DESCRIPTOR, neobuilder.generators.symbols.modules.ProtoModule(rainbow_pb2))
        class_string = proto_class.render_py().strip()
        expected = """@dataclasses.dataclass
class AllTypesNestedMap(plasm.DataclassBase):
    __proto_cls__ = pb2.AllTypesNestedMap
    my_string_map: Dict[str, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_int32_map: Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_int64_map: Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_uint32_map: Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_uint64_map: Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_sint32_map: Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_sint64_map: Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_fixed32_map: Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_fixed64_map: Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_sfixed32_map: Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_sfixed64_map: Dict[int, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})
    my_bool_map: Dict[bool, SubMessage] = dataclasses.field(default_factory=dict, metadata={'dictator': dictators.BaseDictator, 'is_map': True, 'is_obj': True})"""
        self.assertEqual(expected, class_string)

    def test_duration(self):
        from sandbox.test import timeduration_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(timeduration_pb2.DurationMessage.DESCRIPTOR,
                                                                         neobuilder.generators.symbols.modules.ProtoModule(timeduration_pb2))
        exp_field = 'my_duration'
        exp_type_hint = 'datetime.timedelta'
        exp_dictator = 'DurationDictator'
        exp_meta = f"'dictator': dictators.{exp_dictator}"
        exp_default = 'default=None'

        proto_field = neobuilder.generators.symbols.dataclass.ProtoField(proto_class.descriptor.fields_by_name[exp_field], proto_class)

        self.assertTrue(proto_field.is_single())
        self.assertFalse(proto_field.is_list())
        self.assertFalse(proto_field.is_map())

        self.assertFalse(proto_field.is_proto_repeated())

        self.assertTrue(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())

        self.assertTrue(proto_field.is_duration())
        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())
        self.assertFalse(proto_field.is_enum())

        self.assertEqual(exp_field, proto_field.py_name())
        self.assertEqual(exp_type_hint, proto_field.get_type_hint())
        self.assertEqual(exp_dictator, proto_field.get_dictator_name())
        self.assertEqual(exp_meta, proto_field.get_metadata())
        self.assertEqual(f"{exp_field}: {exp_type_hint} = dataclasses.field({exp_default}, metadata={{{exp_meta}}})", proto_field.render_py())

    def test_duration_list(self):
        from sandbox.test import timeduration_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(timeduration_pb2.DurationMessage.DESCRIPTOR,
                                                                         neobuilder.generators.symbols.modules.ProtoModule(timeduration_pb2))
        exp_field = 'my_duration_list'
        exp_type_hint = 'List[datetime.timedelta]'
        exp_dictator = 'DurationDictator'
        exp_meta = f"'dictator': dictators.{exp_dictator}, 'is_list': True"
        exp_default = 'default_factory=list'

        proto_field = neobuilder.generators.symbols.dataclass.ProtoField(proto_class.descriptor.fields_by_name[exp_field], proto_class)

        self.assertFalse(proto_field.is_single())
        self.assertTrue(proto_field.is_list())
        self.assertFalse(proto_field.is_map())

        self.assertTrue(proto_field.is_proto_repeated())

        self.assertTrue(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())

        self.assertTrue(proto_field.is_duration())
        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())
        self.assertFalse(proto_field.is_enum())

        self.assertEqual(exp_field, proto_field.py_name())
        self.assertEqual(exp_type_hint, proto_field.get_type_hint())
        self.assertEqual(exp_dictator, proto_field.get_dictator_name())
        self.assertEqual(exp_meta, proto_field.get_metadata())
        self.assertEqual(f"{exp_field}: {exp_type_hint} = dataclasses.field({exp_default}, metadata={{{exp_meta}}})",
                         proto_field.render_py())

    def test_duration_map(self):
        from sandbox.test import timeduration_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(timeduration_pb2.DurationMessage.DESCRIPTOR,
                                                                         neobuilder.generators.symbols.modules.ProtoModule(timeduration_pb2))
        exp_field = 'my_duration_map'
        exp_type_hint = 'Dict[str, datetime.timedelta]'
        exp_dictator = 'DurationDictator'
        exp_meta = f"'dictator': dictators.{exp_dictator}, 'is_map': True"
        exp_default = 'default_factory=dict'

        proto_field = neobuilder.generators.symbols.dataclass.ProtoField(proto_class.descriptor.fields_by_name[exp_field], proto_class)

        self.assertFalse(proto_field.is_single())
        self.assertFalse(proto_field.is_list())
        self.assertTrue(proto_field.is_map())

        self.assertTrue(proto_field.is_proto_repeated())

        self.assertTrue(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())

        self.assertTrue(proto_field.is_duration())
        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())
        self.assertFalse(proto_field.is_enum())

        self.assertEqual(exp_field, proto_field.py_name())
        self.assertEqual(exp_type_hint, proto_field.get_type_hint())
        self.assertEqual(exp_dictator, proto_field.get_dictator_name())
        self.assertEqual(exp_meta, proto_field.get_metadata())
        self.assertEqual(f"{exp_field}: {exp_type_hint} = dataclasses.field({exp_default}, metadata={{{exp_meta}}})",
                         proto_field.render_py())


class ProtoAnyFieldTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Remove old stuff...
        build_package = os.path.join(BUILD_ROOT, 'sandbox')
        if os.path.exists(build_package):
            shutil.rmtree(build_package)
            time.sleep(0.1)

        # Build stuff...
        builder = NeoBuilder(package='sandbox',
                             protopath=PROTO_ROOT,
                             build_root=BUILD_ROOT)
        builder.build()

        sys.path.append(BUILD_ROOT)

    def test_any(self):
        from sandbox.test import anytest_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(anytest_pb2.AnyMessage.DESCRIPTOR,
                                                                         neobuilder.generators.symbols.modules.ProtoModule(anytest_pb2))
        exp_field = 'my_any'
        exp_type_hint = 'plasm.DataclassBase'
        exp_dictator = 'AnyDictator'
        exp_meta = f"'dictator': dictators.{exp_dictator}"
        exp_default = 'default=None'

        proto_field = neobuilder.generators.symbols.dataclass.ProtoField(proto_class.descriptor.fields_by_name[exp_field], proto_class)

        self.assertTrue(proto_field.is_single())
        self.assertFalse(proto_field.is_list())
        self.assertFalse(proto_field.is_map())

        self.assertFalse(proto_field.is_proto_repeated())

        self.assertTrue(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())

        self.assertTrue(proto_field.is_any())
        self.assertFalse(proto_field.is_duration())
        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())
        self.assertFalse(proto_field.is_enum())

        self.assertEqual(exp_field, proto_field.py_name())
        self.assertEqual(exp_type_hint, proto_field.get_type_hint())
        self.assertEqual(exp_dictator, proto_field.get_dictator_name())
        self.assertEqual(exp_meta, proto_field.get_metadata())
        self.assertEqual(f"{exp_field}: {exp_type_hint} = dataclasses.field({exp_default}, metadata={{{exp_meta}}})", proto_field.render_py())

    def test_any_list(self):
        from sandbox.test import anytest_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(anytest_pb2.AnyMessage.DESCRIPTOR,
                                                                         neobuilder.generators.symbols.modules.ProtoModule(anytest_pb2))
        exp_field = 'my_any_list'
        exp_type_hint = 'List[plasm.DataclassBase]'
        exp_dictator = 'AnyDictator'
        exp_meta = f"'dictator': dictators.{exp_dictator}, 'is_list': True"
        exp_default = 'default_factory=list'

        proto_field = neobuilder.generators.symbols.dataclass.ProtoField(proto_class.descriptor.fields_by_name[exp_field], proto_class)

        self.assertFalse(proto_field.is_single())
        self.assertTrue(proto_field.is_list())
        self.assertFalse(proto_field.is_map())

        self.assertTrue(proto_field.is_proto_repeated())

        self.assertTrue(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())

        self.assertTrue(proto_field.is_any())
        self.assertFalse(proto_field.is_duration())
        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())
        self.assertFalse(proto_field.is_enum())

        self.assertEqual(exp_field, proto_field.py_name())
        self.assertEqual(exp_type_hint, proto_field.get_type_hint())
        self.assertEqual(exp_dictator, proto_field.get_dictator_name())
        self.assertEqual(exp_meta, proto_field.get_metadata())
        self.assertEqual(f"{exp_field}: {exp_type_hint} = dataclasses.field({exp_default}, metadata={{{exp_meta}}})",
                         proto_field.render_py())

    def test_any_map(self):
        from sandbox.test import anytest_pb2
        proto_class = neobuilder.generators.symbols.dataclass.ProtoClass(anytest_pb2.AnyMessage.DESCRIPTOR,
                                                                         neobuilder.generators.symbols.modules.ProtoModule(anytest_pb2))
        exp_field = 'my_any_map'
        exp_type_hint = 'Dict[str, plasm.DataclassBase]'
        exp_dictator = 'AnyDictator'
        exp_meta = f"'dictator': dictators.{exp_dictator}, 'is_map': True"
        exp_default = 'default_factory=dict'

        proto_field = neobuilder.generators.symbols.dataclass.ProtoField(proto_class.descriptor.fields_by_name[exp_field], proto_class)

        self.assertFalse(proto_field.is_single())
        self.assertFalse(proto_field.is_list())
        self.assertTrue(proto_field.is_map())

        self.assertTrue(proto_field.is_proto_repeated())

        self.assertTrue(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())

        self.assertTrue(proto_field.is_any())
        self.assertFalse(proto_field.is_duration())
        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())
        self.assertFalse(proto_field.is_enum())

        self.assertEqual(exp_field, proto_field.py_name())
        self.assertEqual(exp_type_hint, proto_field.get_type_hint())
        self.assertEqual(exp_dictator, proto_field.get_dictator_name())
        self.assertEqual(exp_meta, proto_field.get_metadata())
        self.assertEqual(f"{exp_field}: {exp_type_hint} = dataclasses.field({exp_default}, metadata={{{exp_meta}}})",
                         proto_field.render_py())


class ProtoEnumFieldTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Remove old stuff...
        build_package = os.path.join(BUILD_ROOT, 'sandbox')
        if os.path.exists(build_package):
            shutil.rmtree(build_package)
            time.sleep(0.1)

        # Build stuff...
        builder = NeoBuilder(package='sandbox',
                             protopath=PROTO_ROOT,
                             build_root=BUILD_ROOT)
        builder.build()

        sys.path.append(BUILD_ROOT)

    def test_external_enum(self):
        from sandbox.test import enums_pb2
        proto_module = neobuilder.generators.symbols.modules.ProtoModule(enums_pb2)
        proto_enum = proto_module.enum_map['ExternalEnum']
        self.assertEqual('ExternalEnum', proto_enum.get_name())
        self.assertEqual('ExternalEnum', proto_enum.get_class_import_name())
        self.assertEqual("""THREE = ExternalEnum(3)
TWO = ExternalEnum(2)
ONE = ExternalEnum(1)
ZERO_AND_DEFAULT = ExternalEnum(0)""", proto_enum.render_py_consts().strip())
        self.assertEqual("""class ExternalEnum(enum.IntEnum):
    __proto_cls__ = pb2.ExternalEnum
    THREE = 3
    TWO = 2
    ONE = 1
    ZERO_AND_DEFAULT = 0""", proto_enum.render_py_class().strip())

    def test_external_enum_alias(self):
        from sandbox.test import enums_pb2
        proto_module = neobuilder.generators.symbols.modules.ProtoModule(enums_pb2)
        proto_enum = proto_module.enum_map['ExternalAliasEnum']
        self.assertEqual('ExternalAliasEnum', proto_enum.get_name())
        self.assertEqual('ExternalAliasEnum', proto_enum.get_class_import_name())
        self.assertEqual("""SEX = ExternalAliasEnum(3)
SIX = ExternalAliasEnum(3)
FIMM = ExternalAliasEnum(2)
FIVE = ExternalAliasEnum(2)
FJORIR = ExternalAliasEnum(1)
FOUR = ExternalAliasEnum(1)
ZERO = ExternalAliasEnum(0)
DEFAULT = ExternalAliasEnum(0)""", proto_enum.render_py_consts().strip())
        self.assertEqual("""class ExternalAliasEnum(enum.IntEnum):
    __proto_cls__ = pb2.ExternalAliasEnum
    SEX = 3
    SIX = 3
    FIMM = 2
    FIVE = 2
    FJORIR = 1
    FOUR = 1
    ZERO = 0
    DEFAULT = 0""", proto_enum.render_py_class().strip())

    def test_external_enum_field(self):
        from sandbox.test import enums_pb2
        proto_module = neobuilder.generators.symbols.modules.ProtoModule(enums_pb2)
        proto_class = proto_module.message_map['WithExternalEnum']
        proto_field = proto_class.field_map['my_enum']

        self.assertTrue(proto_field.is_single())
        self.assertFalse(proto_field.is_list())
        self.assertFalse(proto_field.is_map())

        self.assertFalse(proto_field.is_proto_repeated())

        self.assertFalse(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())
        self.assertTrue(proto_field.is_enum())

        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())

        self.assertEqual('my_enum', proto_field.py_name())
        self.assertEqual('ExternalEnum', proto_field.get_type_hint())
        self.assertEqual('EnumDictator', proto_field.get_dictator_name())
        self.assertEqual("'dictator': dictators.EnumDictator, 'is_enum': True", proto_field.get_metadata())
        self.assertEqual("my_enum: ExternalEnum = dataclasses.field(default=0, metadata={'dictator': dictators.EnumDictator, 'is_enum': True})", proto_field.render_py())

    def test_external_enum_alias_field(self):
        from sandbox.test import enums_pb2
        proto_module = neobuilder.generators.symbols.modules.ProtoModule(enums_pb2)
        proto_class = proto_module.message_map['WithExternalEnum']
        proto_field = proto_class.field_map['my_alias_enum']

        self.assertTrue(proto_field.is_single())
        self.assertFalse(proto_field.is_list())
        self.assertFalse(proto_field.is_map())

        self.assertFalse(proto_field.is_proto_repeated())

        self.assertFalse(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())
        self.assertTrue(proto_field.is_enum())

        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())

        self.assertEqual('my_alias_enum', proto_field.py_name())
        self.assertEqual('ExternalAliasEnum', proto_field.get_type_hint())
        self.assertEqual('EnumDictator', proto_field.get_dictator_name())
        self.assertEqual("'dictator': dictators.EnumDictator, 'is_enum': True", proto_field.get_metadata())
        self.assertEqual("my_alias_enum: ExternalAliasEnum = dataclasses.field(default=0, metadata={'dictator': dictators.EnumDictator, 'is_enum': True})", proto_field.render_py())

    def test_external_enum_list_field(self):
        from sandbox.test import enums_pb2
        proto_module = neobuilder.generators.symbols.modules.ProtoModule(enums_pb2)
        proto_class = proto_module.message_map['WithExternalEnum']
        exp_field = 'my_enum_list'
        exp_dictator = 'EnumDictator'
        exp_type_hint = 'List[ExternalEnum]'
        exp_meta = f"'dictator': dictators.{exp_dictator}, 'is_list': True, 'is_enum': True"
        exp_default = 'default_factory=list'

        proto_field = proto_class.field_map[exp_field]

        self.assertFalse(proto_field.is_single())
        self.assertTrue(proto_field.is_list())
        self.assertFalse(proto_field.is_map())

        self.assertTrue(proto_field.is_proto_repeated())

        self.assertFalse(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())
        self.assertTrue(proto_field.is_enum())

        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())

        self.assertEqual(exp_field, proto_field.py_name())
        self.assertEqual(exp_type_hint, proto_field.get_type_hint())
        self.assertEqual(exp_dictator, proto_field.get_dictator_name())
        self.assertEqual(exp_meta, proto_field.get_metadata())
        self.assertEqual(f"{exp_field}: {exp_type_hint} = dataclasses.field({exp_default}, metadata={{{exp_meta}}})", proto_field.render_py())

    def test_external_enum_alias_list_field(self):
        from sandbox.test import enums_pb2
        proto_module = neobuilder.generators.symbols.modules.ProtoModule(enums_pb2)
        proto_class = proto_module.message_map['WithExternalEnum']
        exp_field = 'my_alias_enum_list'
        exp_dictator = 'EnumDictator'
        exp_type_hint = 'List[ExternalAliasEnum]'
        exp_meta = f"'dictator': dictators.{exp_dictator}, 'is_list': True, 'is_enum': True"
        exp_default = 'default_factory=list'

        proto_field = proto_class.field_map[exp_field]

        self.assertFalse(proto_field.is_single())
        self.assertTrue(proto_field.is_list())
        self.assertFalse(proto_field.is_map())

        self.assertTrue(proto_field.is_proto_repeated())

        self.assertFalse(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())
        self.assertTrue(proto_field.is_enum())

        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())

        self.assertEqual(exp_field, proto_field.py_name())
        self.assertEqual(exp_type_hint, proto_field.get_type_hint())
        self.assertEqual(exp_dictator, proto_field.get_dictator_name())
        self.assertEqual(exp_meta, proto_field.get_metadata())
        self.assertEqual(f"{exp_field}: {exp_type_hint} = dataclasses.field({exp_default}, metadata={{{exp_meta}}})", proto_field.render_py())

    def test_external_enum_map_field(self):
        from sandbox.test import enums_pb2
        proto_module = neobuilder.generators.symbols.modules.ProtoModule(enums_pb2)
        proto_class = proto_module.message_map['WithExternalEnum']
        exp_field = 'my_enum_map'
        exp_dictator = 'EnumDictator'
        exp_type_hint = 'Dict[str, ExternalEnum]'
        exp_meta = f"'dictator': dictators.{exp_dictator}, 'is_map': True, 'is_enum': True"
        exp_default = 'default_factory=dict'

        proto_field = proto_class.field_map[exp_field]

        self.assertFalse(proto_field.is_single())
        self.assertFalse(proto_field.is_list())
        self.assertTrue(proto_field.is_map())

        self.assertTrue(proto_field.is_proto_repeated())

        self.assertFalse(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())
        self.assertTrue(proto_field.is_enum())

        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())

        self.assertEqual(exp_field, proto_field.py_name())
        self.assertEqual(exp_type_hint, proto_field.get_type_hint())
        self.assertEqual(exp_dictator, proto_field.get_dictator_name())
        self.assertEqual(exp_meta, proto_field.get_metadata())
        self.assertEqual(f"{exp_field}: {exp_type_hint} = dataclasses.field({exp_default}, metadata={{{exp_meta}}})", proto_field.render_py())

    def test_external_enum_alias_map_field(self):
        from sandbox.test import enums_pb2
        proto_module = neobuilder.generators.symbols.modules.ProtoModule(enums_pb2)
        proto_class = proto_module.message_map['WithExternalEnum']
        exp_field = 'my_alias_enum_map'
        exp_dictator = 'EnumDictator'
        exp_type_hint = 'Dict[str, ExternalAliasEnum]'
        exp_meta = f"'dictator': dictators.{exp_dictator}, 'is_map': True, 'is_enum': True"
        exp_default = 'default_factory=dict'

        proto_field = proto_class.field_map[exp_field]

        self.assertFalse(proto_field.is_single())
        self.assertFalse(proto_field.is_list())
        self.assertTrue(proto_field.is_map())

        self.assertTrue(proto_field.is_proto_repeated())

        self.assertFalse(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())
        self.assertTrue(proto_field.is_enum())

        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())

        self.assertEqual(exp_field, proto_field.py_name())
        self.assertEqual(exp_type_hint, proto_field.get_type_hint())
        self.assertEqual(exp_dictator, proto_field.get_dictator_name())
        self.assertEqual(exp_meta, proto_field.get_metadata())
        self.assertEqual(f"{exp_field}: {exp_type_hint} = dataclasses.field({exp_default}, metadata={{{exp_meta}}})", proto_field.render_py())

    def test_internal_enum(self):
        from sandbox.test import enums_pb2
        proto_module = neobuilder.generators.symbols.modules.ProtoModule(enums_pb2)
        proto_class = proto_module.message_map['WithInternalEnum']
        proto_enum = proto_class.enum_map['InternalEnum']
        self.assertEqual('InternalEnum', proto_enum.get_name())
        self.assertEqual('WithInternalEnum.InternalEnum', proto_enum.get_class_import_name())
        self.assertEqual("""SIX = InternalEnum(6)
FIVE = InternalEnum(5)
FOUR = InternalEnum(4)
ZERO_AND_DEFAULT = InternalEnum(0)""", proto_enum.render_py_consts().strip())
        self.assertEqual("""class InternalEnum(enum.IntEnum):
    __proto_cls__ = pb2.WithInternalEnum.InternalEnum
    SIX = 6
    FIVE = 5
    FOUR = 4
    ZERO_AND_DEFAULT = 0""", proto_enum.render_py_class().strip())

        self.assertEqual("""SIX = InternalEnum(6)
    FIVE = InternalEnum(5)
    FOUR = InternalEnum(4)
    ZERO_AND_DEFAULT = InternalEnum(0)""", proto_enum.render_py_consts(1).strip())
        self.assertEqual("""class InternalEnum(enum.IntEnum):
        __proto_cls__ = pb2.WithInternalEnum.InternalEnum
        SIX = 6
        FIVE = 5
        FOUR = 4
        ZERO_AND_DEFAULT = 0""", proto_enum.render_py_class(1).strip())

    def test_internal_enum_alias(self):
        from sandbox.test import enums_pb2
        proto_module = neobuilder.generators.symbols.modules.ProtoModule(enums_pb2)
        proto_class = proto_module.message_map['WithInternalEnum']
        proto_enum = proto_class.enum_map['InternalAliasEnum']
        self.assertEqual('InternalAliasEnum', proto_enum.get_name())
        self.assertEqual('WithInternalEnum.InternalAliasEnum', proto_enum.get_class_import_name())
        self.assertEqual("""NIU = InternalAliasEnum(9)
NINE = InternalAliasEnum(9)
ATTA = InternalAliasEnum(8)
EIGHT = InternalAliasEnum(8)
SJO = InternalAliasEnum(7)
SEVEN = InternalAliasEnum(7)
ZERO = InternalAliasEnum(0)
DEFAULT = InternalAliasEnum(0)""", proto_enum.render_py_consts().strip())
        self.assertEqual("""class InternalAliasEnum(enum.IntEnum):
    __proto_cls__ = pb2.WithInternalEnum.InternalAliasEnum
    NIU = 9
    NINE = 9
    ATTA = 8
    EIGHT = 8
    SJO = 7
    SEVEN = 7
    ZERO = 0
    DEFAULT = 0""", proto_enum.render_py_class().strip())

        self.assertEqual("""NIU = InternalAliasEnum(9)
    NINE = InternalAliasEnum(9)
    ATTA = InternalAliasEnum(8)
    EIGHT = InternalAliasEnum(8)
    SJO = InternalAliasEnum(7)
    SEVEN = InternalAliasEnum(7)
    ZERO = InternalAliasEnum(0)
    DEFAULT = InternalAliasEnum(0)""", proto_enum.render_py_consts(1).strip())
        self.assertEqual("""class InternalAliasEnum(enum.IntEnum):
        __proto_cls__ = pb2.WithInternalEnum.InternalAliasEnum
        NIU = 9
        NINE = 9
        ATTA = 8
        EIGHT = 8
        SJO = 7
        SEVEN = 7
        ZERO = 0
        DEFAULT = 0""", proto_enum.render_py_class(1).strip())

    def test_internal_enum_field(self):
        from sandbox.test import enums_pb2
        proto_module = neobuilder.generators.symbols.modules.ProtoModule(enums_pb2)
        proto_class = proto_module.message_map['WithInternalEnum']

        exp_field = 'my_internal_enum'
        exp_dictator = 'EnumDictator'
        exp_type_hint = 'WithInternalEnum.InternalEnum'
        exp_meta = f"'dictator': dictators.{exp_dictator}, 'is_enum': True"
        exp_default = 'default=0'

        proto_field = proto_class.field_map[exp_field]

        self.assertTrue(proto_field.is_single())
        self.assertFalse(proto_field.is_list())
        self.assertFalse(proto_field.is_map())

        self.assertFalse(proto_field.is_proto_repeated())

        self.assertFalse(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())
        self.assertTrue(proto_field.is_enum())

        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())

        self.assertEqual(exp_field, proto_field.py_name())
        self.assertEqual(exp_type_hint, proto_field.get_type_hint())
        self.assertEqual(exp_dictator, proto_field.get_dictator_name())
        self.assertEqual(exp_meta, proto_field.get_metadata())
        self.assertEqual(f"{exp_field}: {exp_type_hint} = dataclasses.field({exp_default}, metadata={{{exp_meta}}})", proto_field.render_py())

    def test_internal_enum_alias_field(self):
        from sandbox.test import enums_pb2
        proto_module = neobuilder.generators.symbols.modules.ProtoModule(enums_pb2)
        proto_class = proto_module.message_map['WithInternalEnum']

        exp_field = 'my_internal_alias_enum'
        exp_type_hint = 'WithInternalEnum.InternalAliasEnum'
        exp_dictator = 'EnumDictator'
        exp_meta = f"'dictator': dictators.{exp_dictator}, 'is_enum': True"
        exp_default = 'default=0'

        proto_field = proto_class.field_map[exp_field]

        self.assertTrue(proto_field.is_single())
        self.assertFalse(proto_field.is_list())
        self.assertFalse(proto_field.is_map())

        self.assertFalse(proto_field.is_proto_repeated())

        self.assertFalse(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())
        self.assertTrue(proto_field.is_enum())

        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())

        self.assertEqual(exp_field, proto_field.py_name())
        self.assertEqual(exp_type_hint, proto_field.get_type_hint())
        self.assertEqual(exp_dictator, proto_field.get_dictator_name())
        self.assertEqual(exp_meta, proto_field.get_metadata())
        self.assertEqual(f"{exp_field}: {exp_type_hint} = dataclasses.field({exp_default}, metadata={{{exp_meta}}})", proto_field.render_py())

    def test_internal_enum_list(self):
        from sandbox.test import enums_pb2
        proto_module = neobuilder.generators.symbols.modules.ProtoModule(enums_pb2)
        proto_class = proto_module.message_map['WithInternalEnum']

        exp_field = 'my_internal_enum_list'
        exp_type_hint = 'List[WithInternalEnum.InternalEnum]'
        exp_dictator = 'EnumDictator'
        exp_meta = f"'dictator': dictators.{exp_dictator}, 'is_list': True, 'is_enum': True"
        exp_default = 'default_factory=list'

        proto_field = proto_class.field_map[exp_field]

        self.assertFalse(proto_field.is_single())
        self.assertTrue(proto_field.is_list())
        self.assertFalse(proto_field.is_map())

        self.assertTrue(proto_field.is_proto_repeated())

        self.assertFalse(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())
        self.assertTrue(proto_field.is_enum())

        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())

        self.assertEqual(exp_field, proto_field.py_name())
        self.assertEqual(exp_type_hint, proto_field.get_type_hint())
        self.assertEqual(exp_dictator, proto_field.get_dictator_name())
        self.assertEqual(exp_meta, proto_field.get_metadata())
        self.assertEqual(f"{exp_field}: {exp_type_hint} = dataclasses.field({exp_default}, metadata={{{exp_meta}}})", proto_field.render_py())

    def test_internal_enum_alias_list(self):
        from sandbox.test import enums_pb2
        proto_module = neobuilder.generators.symbols.modules.ProtoModule(enums_pb2)
        proto_class = proto_module.message_map['WithInternalEnum']

        exp_field = 'my_internal_alias_enum_list'
        exp_type_hint = 'List[WithInternalEnum.InternalAliasEnum]'
        exp_dictator = 'EnumDictator'
        exp_meta = f"'dictator': dictators.{exp_dictator}, 'is_list': True, 'is_enum': True"
        exp_default = 'default_factory=list'

        proto_field = proto_class.field_map[exp_field]

        self.assertFalse(proto_field.is_single())
        self.assertTrue(proto_field.is_list())
        self.assertFalse(proto_field.is_map())

        self.assertTrue(proto_field.is_proto_repeated())

        self.assertFalse(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())
        self.assertTrue(proto_field.is_enum())

        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())

        self.assertEqual(exp_field, proto_field.py_name())
        self.assertEqual(exp_type_hint, proto_field.get_type_hint())
        self.assertEqual(exp_dictator, proto_field.get_dictator_name())
        self.assertEqual(exp_meta, proto_field.get_metadata())
        self.assertEqual(f"{exp_field}: {exp_type_hint} = dataclasses.field({exp_default}, metadata={{{exp_meta}}})", proto_field.render_py())

    def test_internal_enum_map(self):
        from sandbox.test import enums_pb2
        proto_module = neobuilder.generators.symbols.modules.ProtoModule(enums_pb2)
        proto_class = proto_module.message_map['WithInternalEnum']

        exp_field = 'my_internal_enum_map'
        exp_type_hint = 'Dict[str, WithInternalEnum.InternalEnum]'
        exp_dictator = 'EnumDictator'
        exp_meta = f"'dictator': dictators.{exp_dictator}, 'is_map': True, 'is_enum': True"
        exp_default = 'default_factory=dict'

        proto_field = proto_class.field_map[exp_field]

        self.assertFalse(proto_field.is_single())
        self.assertFalse(proto_field.is_list())
        self.assertTrue(proto_field.is_map())

        self.assertTrue(proto_field.is_proto_repeated())

        self.assertFalse(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())
        self.assertTrue(proto_field.is_enum())

        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())

        self.assertEqual(exp_field, proto_field.py_name())
        self.assertEqual(exp_type_hint, proto_field.get_type_hint())
        self.assertEqual(exp_dictator, proto_field.get_dictator_name())
        self.assertEqual(exp_meta, proto_field.get_metadata())
        self.assertEqual(f"{exp_field}: {exp_type_hint} = dataclasses.field({exp_default}, metadata={{{exp_meta}}})", proto_field.render_py())

    def test_internal_enum_alias_map(self):
        from sandbox.test import enums_pb2
        proto_module = neobuilder.generators.symbols.modules.ProtoModule(enums_pb2)
        proto_class = proto_module.message_map['WithInternalEnum']

        exp_field = 'my_internal_alias_enum_map'
        exp_type_hint = 'Dict[str, WithInternalEnum.InternalAliasEnum]'
        exp_dictator = 'EnumDictator'
        exp_meta = f"'dictator': dictators.{exp_dictator}, 'is_map': True, 'is_enum': True"
        exp_default = 'default_factory=dict'

        proto_field = proto_class.field_map[exp_field]

        self.assertFalse(proto_field.is_single())
        self.assertFalse(proto_field.is_list())
        self.assertTrue(proto_field.is_map())

        self.assertTrue(proto_field.is_proto_repeated())

        self.assertFalse(proto_field.is_scalar())
        self.assertFalse(proto_field.is_message())
        self.assertTrue(proto_field.is_enum())

        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())

        self.assertEqual(exp_field, proto_field.py_name())
        self.assertEqual(exp_type_hint, proto_field.get_type_hint())
        self.assertEqual(exp_dictator, proto_field.get_dictator_name())
        self.assertEqual(exp_meta, proto_field.get_metadata())
        self.assertEqual(f"{exp_field}: {exp_type_hint} = dataclasses.field({exp_default}, metadata={{{exp_meta}}})", proto_field.render_py())

    def test_foreign_import_type(self):
        from sandbox.test import beta_pb2
        proto_module = neobuilder.generators.symbols.modules.ProtoModule(beta_pb2)
        proto_class = proto_module.message_map['BetaMessage']

        exp_field = 'my_foreign_message'
        exp_type_hint = 'sandbox__test__alpha_dc.AlphaMessage'
        exp_dictator = 'BaseDictator'
        exp_meta = f"'dictator': dictators.{exp_dictator}, 'is_obj': True"
        exp_default = 'default=None'

        proto_field = proto_class.field_map[exp_field]

        self.assertTrue(proto_field.is_single())
        self.assertFalse(proto_field.is_list())
        self.assertFalse(proto_field.is_map())

        self.assertFalse(proto_field.is_proto_repeated())

        self.assertFalse(proto_field.is_scalar())
        self.assertTrue(proto_field.is_message())
        self.assertFalse(proto_field.is_enum())

        self.assertFalse(proto_field.is_timestamp())
        self.assertFalse(proto_field.is_bytes())

        self.assertEqual(exp_field, proto_field.py_name())
        self.assertEqual(exp_type_hint, proto_field.get_type_hint())
        self.assertEqual(exp_dictator, proto_field.get_dictator_name())
        self.assertEqual(exp_meta, proto_field.get_metadata())
        self.assertEqual(f"{exp_field}: {exp_type_hint} = dataclasses.field({exp_default}, metadata={{{exp_meta}}})", proto_field.render_py())

        self.assertEqual('from sandbox.test import alpha_dc as sandbox__test__alpha_dc\n', proto_module.render_imports())
