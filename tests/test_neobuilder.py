import unittest

from neobuilder.neobuilder import NeoBuilder
import os
import shutil

import logging
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
import time

HERE = os.path.dirname(__file__)

PROTO_ROOT = os.path.join(HERE, 'res', 'proto')
BUILD_ROOT = os.path.join(HERE, 'res', 'build')
EXPECTED_ROOT = os.path.join(HERE, 'res', 'expected')

EXPECTED_NUMBER_OF_FILES_CHECKED = 38

from neobuilder import __version__ as neobuilder_version
from protoplasm import __version__ as protoplasm_version


class NeobuilderTest(unittest.TestCase):
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

    def test_files_were_built(self):
        def assert_exists(file_to_check):
            self.assertTrue(os.path.exists(os.path.join(BUILD_ROOT, file_to_check)), msg=f'{file_to_check} not found')

        for (dirpath, dirnames, filenames) in os.walk(EXPECTED_ROOT):
            for f in filenames:
                assert_exists(os.path.join(dirpath, f))

    def test_code_in_files(self):
        def assert_files_are_same(file_to_check):
            file_to_check = file_to_check.replace('\\', '/')
            lines_to_check = []
            lines_skipped = 0
            with open(os.path.join(BUILD_ROOT, file_to_check), 'r') as fin:
                for line in fin:
                    if not line.strip().startswith('# '):
                        stripped_line = line.rstrip()
                        if stripped_line:
                            lines_to_check.append(stripped_line)
                    else:
                        lines_skipped += 1

            lines_should_be = []
            with open(os.path.join(EXPECTED_ROOT, file_to_check), 'r') as fin:
                for line in fin:
                    if not line.strip().startswith('# '):
                        if file_to_check == 'sandbox/__init__.py':
                            if line.startswith('__protoplasm_version__ = ('):
                                line = f'__protoplasm_version__ = {protoplasm_version}'
                            if line.startswith('__neobuilder_version__ = ('):
                                line = f'__neobuilder_version__ = {neobuilder_version}'
                        stripped_line = line.rstrip()
                        if stripped_line:
                            lines_should_be.append(stripped_line)

            self.assertEqual(len(lines_should_be), len(lines_to_check), msg=f'Line number mismatch in {file_to_check}')

            if len(lines_to_check) == len(lines_should_be):
                for i in range(len(lines_should_be)):
                    self.assertEqual(lines_should_be[i], lines_to_check[i],
                                     msg=f'Line no {i+lines_skipped+1} in {file_to_check} does not match!')

        file_count = 0
        for (dirpath, dirnames, filenames) in os.walk(EXPECTED_ROOT):
            for f in filenames:
                if not (f.endswith('_pb2.py') or f.endswith('_pb2_grpc.py')):  # We don't test the pb2 files!
                    rel_f = os.path.relpath(os.path.join(dirpath, f), EXPECTED_ROOT)
                    file_count += 1
                    assert_files_are_same(rel_f)

        self.assertEqual(EXPECTED_NUMBER_OF_FILES_CHECKED, file_count, msg='Did not check the expected number of files!')
