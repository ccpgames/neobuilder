__all__ = [
    'NeoBuilder',
]


import sys
import os
import shutil
import time
from importlib import resources
import semver

from grpc_tools import protoc
from . import render

from ccptools.tpu import strimp

from neobuilder.generators.symbols import modules
from neobuilder.structs import *
from neobuilder import __version__ as neobuilder_version

import logging
log = logging.getLogger(__name__)

_PY_3_9_PLUS = sys.version_info >= (3, 9)


class NeoBuilder(object):
    VERSION = neobuilder_version

    def __init__(self,
                 package: str,
                 protopath: str = './proto',
                 build_root: str = './build',
                 major: bool = False,
                 patch: bool = False,
                 verbose: bool = False):

        self.package = package

        self.protopath = protopath.replace('\\', '/')
        self.build_root = build_root.replace('\\', '/')

        self.major = major
        self.patch = patch

        self.proto_files: List[ProtoFile] = []

        # Proto Build Arguments and stuff...
        self.proto_include = self._get_basic_proto_path()
        self.proto_build_args = ['protoc', f'-I{self.protopath}/']
        if self.proto_include:
            self.proto_build_args.append('-I{}'.format(self.proto_include))
        self.proto_build_args.append(f'--python_out={self.build_root}')

        self.last_version = None
        self._next_version = None
        self.commit_message = 'No commit message'
        self.verbose = verbose
        logging.basicConfig(level=(logging.DEBUG if self.verbose else logging.INFO),
                            format='%(levelname)8s - %(message)s')
        log.info(f'Initializing Neobuilder {self.neobuilder_version()}')

    @staticmethod
    def _get_basic_proto_path() -> str:
        if _PY_3_9_PLUS:
            from importlib import resources
            return str(resources.files('grpc_tools').joinpath('_proto'))
        else:
            import pkg_resources  # noqa
            return str(pkg_resources.resource_filename('grpc_tools', '_proto'))  # noqa

    @property
    def next_version(self):
        if self._next_version:
            return self._next_version
        return '0.1.0'

    @property
    def build_path(self) -> str:
        return os.path.join(self.build_root, self.package)

    def read_last_version(self):
        log.debug('Reading last version...')
        version_file = os.path.join(self.build_path, '__init__.py')
        if os.path.exists(version_file):
            try:
                m = strimp.get_module(self.package)
                version_var = getattr(m, '__version__', None)
                if not version_var:
                    log.warning('__version__ not found in package')

                else:
                    if isinstance(version_var, tuple):
                        if len(version_var) > 3:
                            ver_str = '.'.join(version_var[:3])
                        else:
                            ver_str = '.'.join(version_var)
                    else:
                        ver_str = version_var

                    self.last_version = ver_str
                    log.info(f'Last version: {self.last_version}')

            except Exception as ex:
                log.exception('package __init__ file import error: %r' % ex)

        else:
            log.warning('package __init__ file not found (is this a new/first build?)')

        if not self.last_version:
            log.warning('Assuming last version: 0.0.0.0')
            self.last_version = ''

    def read_next_version(self):
        log.debug('Reading next version...')
        version_file = os.path.join(self.protopath, self.package, 'VERSION')

        if os.path.exists(version_file):
            version_str = ''
            rest = []
            with open(version_file, 'r') as fin:
                first = True
                for line in fin:
                    if first:
                        version_str = line.strip()
                        first = False
                    else:
                        rest.append(line)

            if not version_str:
                log.warning('VERSION file empty!')

            else:
                try:
                    if '-' in version_str:
                        sv = semver.Version.parse(version_str)
                    else:
                        parts = version_str.split('.')
                        if len(parts) > 3:
                            sv = semver.Version.parse('.'.join(version_str[:3]))
                        else:
                            sv = semver.Version.parse(version_str)

                    self._next_version = str(sv)

                    if rest:
                        msg = '\n'.join(rest)
                        msg = msg.strip()
                        if msg:
                            self.commit_message = msg
                except Exception as ex:
                    log.exception('VERSION file parsing error: %r' % ex)

        else:
            log.warning('VERSION file not found!')

        if not self._next_version:
            log.info('Trying to calculate next version...')
            if not self.last_version:
                log.warning('No last version to calculate next version :(')

            self._next_version = self.calc_next_version()
        log.info(f'Next version: {self._next_version}')

    def calc_next_version(self):
        if self.last_version:
            this_ver = semver.Version.parse(self.last_version)
            if self.major:
                log.info('Bumping major version...')
                next_up = this_ver.bump_major()
            elif self.patch:
                log.info('Bumping patch version...')
                next_up = this_ver.bump_patch()
            else:
                log.info('Bumping minor version...')
                next_up = this_ver.bump_minor()
            return str(next_up)
        return '0.1.0'

    def collect_proto_files(self):
        log.debug('Collecting proto files...')

        def _grpc_check(filename):
            with open(filename, 'r') as fin:
                for line in fin:
                    if line.startswith('option py_generic_services = true'):
                        log.debug(f'Generic service... skip gRPC: {filename}')
                        return False
                    if line.startswith('service '):
                        log.debug(f'Service found: {filename}')
                        return True
            log.debug(f'Service not found: {filename}')
            return False

        self.proto_files = []
        walkroot = os.path.join(self.protopath, self.package)
        rel_root = os.path.join(self.protopath)
        for (dirpath, dirnames, filenames) in os.walk(walkroot):
            for f in filenames:
                if f.endswith('.proto'):
                    dirp = dirpath.replace('\\', '/')
                    rel_dir = dirp[len(rel_root):]
                    if rel_dir.startswith('/'):
                        rel_dir = rel_dir[1:]
                    if not rel_dir.startswith(self.package):
                        log.error(f'Error parsing relative path for {f}')
                    # log.debug(f'... {f=}')
                    # log.debug(f'... {rel_root=}')
                    # log.debug(f'... rel_root={rel_root!r}')
                    # log.debug(f'... {dirp=}')
                    # log.debug(f'... {rel_dir=}')
                    pf = ProtoFile(f, dirp, rel_dir)
                    pf.is_grpc_service = _grpc_check(pf.full_name())
                    self.proto_files.append(pf)
                    log.debug(f'Found proto file: {pf}')
        log.info(f'Found {len(self.proto_files)} proto files!')

    def delete_backup(self):
        backup_dir = f'{self.build_path}__backup'
        if os.path.exists(backup_dir):
            log.debug(f'Deleting backup dir: {backup_dir}')
            shutil.rmtree(backup_dir)
            time.sleep(0.1)

    def purge_old(self):
        backup_dir = f'{self.build_path}__backup'
        fail_dir = f'{self.build_path}__fail'
        if os.path.exists(fail_dir):
            log.debug(f'(purge old) Deleting old failed build dir: {fail_dir}')
            shutil.rmtree(fail_dir)
            time.sleep(0.1)

        if os.path.exists(self.build_path):
            if os.path.exists(backup_dir):
                log.debug(f'(purge old) Deleting backup dir: {fail_dir}')
                shutil.rmtree(backup_dir)
                time.sleep(0.1)

            log.debug(f'(purge old) Moving dir: {self.build_path} -> {backup_dir}')
            shutil.move(self.build_path, backup_dir)
            time.sleep(0.1)

    def revert_old(self):
        backup_dir = f'{self.build_path}__backup'
        fail_dir = f'{self.build_path}__fail'
        if os.path.exists(backup_dir) and os.path.exists(self.build_path):
            if os.path.exists(fail_dir):
                log.debug(f'(revert_old) Deleting old failed build: {fail_dir}')
                shutil.rmtree(fail_dir)
                time.sleep(0.1)
            log.debug(f'(revert_old) Moving dir: {self.build_path} -> {fail_dir}')
            shutil.move(self.build_path, fail_dir)
            time.sleep(0.1)
            log.debug(f'(revert_old) Moving dir: {backup_dir} -> {self.build_path}')
            shutil.move(backup_dir, self.build_path)
            time.sleep(0.1)

    def build(self):
        try:
            sys.path.extend([os.path.abspath(self.build_root)])
            log.debug(f'PATH={sys.path}')
            self.collect_proto_files()
            self.read_last_version()
            self.read_next_version()
            self.purge_old()
            log.info('Waiting 1 sec after IO operations before building proto files...')
            time.sleep(1)

            if not os.path.exists(self.build_path):
                log.debug(f'Generating build path: {self.build_path}')
                os.makedirs(self.build_path, exist_ok=True)

            try:
                log.info('Compiling protobuf files...')
                failed = []

                for pf in self.proto_files:
                    if not self.proto_build(pf):
                        failed.append(pf)

                if failed:
                    for f in failed:
                        log.error(f'Failed to compile proto file: {f}')
                    raise RuntimeError('failed to compile proto files')

            except Exception as ex:
                log.exception(ex)
                log.error('Reverting backup...')
                self.revert_old()
                self.fail_with_style(10, 'Failed to compile proto files with protoc')

            log.info('Waiting 1 sec after IO ops before building neobuf files...')
            time.sleep(1)
            log.info('Generating neobuf files...')
            try:
                for pf in self.proto_files:
                    self.plasm_build(pf)
            except Exception as ex:
                log.exception(ex)
                log.error('Reverting backup...')
                self.revert_old()
                self.fail_with_style(20, 'Failed to build neobuf files with protoplasm')

            log.info('Waiting 1 sec after IO ops before finalizing...')
            time.sleep(1)

            self.add_version()
            self.add_inits()
            self.add_everything()
            self.write_commit_file()
            self.delete_backup()
            log.info('Neobuilder Done!')
        except Exception as ex:
            log.exception(ex)
            self.fail_with_style(99, 'Got 99 problems and an unknown exception is one!')

    def proto_build(self, protofile: ProtoFile) -> bool:
        input_args = self.proto_build_args.copy()
        if protofile.is_grpc_service:
            input_args.append(f'--grpc_python_out={self.build_root}')
        input_args.append(protofile.full_name())
        log.debug(f'Executing: protoc {" ".join(input_args)}')

        ret_val = protoc.main(input_args)

        if ret_val != 0:
            return False
        return True

    def plasm_build(self, protofile: ProtoFile):
        log.info(f'Neobuffing {protofile}')
        m = strimp.get_module(protofile.pb2_module(), logger=log, reraise=True)
        if not m:
            log.error(f'protofile={protofile}')
            raise ImportError('ERROR! Module not found! %s' % protofile.pb2_module())
        else:
            try:
                p = modules.ProtoModule(m)
                p.write_rendered_file()
            except Exception as ex:
                log.exception(f'ERROR! Bad stuff happened! %r' % ex)
                raise

    def add_inits(self):
        log.debug('Adding __init__ files to generated modules...')
        for dirpath, dirnames, filenames in os.walk(self.build_path):
            if not dirpath.endswith('__pycache__'):
                if '__init__.py' not in filenames:
                    render.to_file(f'{dirpath}/__init__.py', render.init())

    def add_version(self):
        log.debug('Adding version to generated package root...')
        package_init = os.path.join(self.build_path, '__init__.py')
        if not os.path.exists(package_init):
            render.to_file(package_init, render.root_init(
                package_name=self.package,
                version_str=self.next_version
            ))
        else:
            raise ValueError('Package __init__ file (%s) already exists? :(', package_init)

    def write_commit_file(self):
        log.debug('Writing commit file...')
        with open(os.path.join(self.build_path, 'VERSION'), 'w', encoding='utf-8') as fout:
            fout.write(f'Version {self.next_version}')
            if self.commit_message:
                fout.write(' - ')
                fout.write(self.commit_message)
            fout.write('\n')

    def add_everything(self):
        # TODO(thordurm@ccpgames.com) 2022-06-07: If we start using __all__ directives then this may well change...
        log.debug('Generating __everything__ file...')
        everything_file = os.path.join(self.build_path, '__everything__.py')
        counter = 0
        with open(everything_file, 'w', encoding='utf-8') as fout:
            fout.write('# Autogenerated file that imports every proto and protoplasm file.\n')
            fout.write('# This is to ensure that the proto symbol database gets populated with everything\n')
            fout.write('# which is something required for Any deserialization to work\n\n')

            line_buffer = []

            for (dirpath, dirnames, filenames) in os.walk(self.build_path):
                for f in filenames:
                    if f.endswith('.py') and not f.endswith('__.py'):
                        fpath = os.path.join(dirpath, f).replace('\\', '/')
                        package_name = fpath[len(self.build_root)+1:-3].replace('/', '.')
                        line_buffer.append(f'import {package_name}')
                        counter += 1
            line_buffer.sort()
            fout.write('\n'.join(line_buffer))
            fout.write('\n')
        log.debug(f'Added {counter} imports to __everything__')

    @staticmethod
    def neobuilder_version() -> str:
        if isinstance(NeoBuilder.VERSION, tuple):
            return '.'.join([str(i) for i in NeoBuilder.VERSION])
        else:
            return NeoBuilder.VERSION

    @staticmethod
    def protoplasm_version() -> str:
        from protoplasm import __version__ as protoplasm_version
        if isinstance(protoplasm_version, tuple):
            return '.'.join([str(i) for i in protoplasm_version])
        else:
            return protoplasm_version

    @staticmethod
    def fail_with_style(code: int, message: str):
        log.error(message)
        sys.exit(code)
