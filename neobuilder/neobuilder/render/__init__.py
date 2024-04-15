from .renderer import TemplateRenderer
from typing import *


def to_file(file: str, content: str):
    with open(file, 'w', encoding='utf-8') as fout:
        fout.write(content)
        fout.write('\n')


def init() -> str:
    return TemplateRenderer().render_file('init')


def root_init(package_name: str,
              version_str) -> str:
    from protoplasm import __version__ as ppv
    from neobuilder import __version__ as nbv
    if isinstance(ppv, tuple):
        if len(ppv) > 3:
            ppv = '.'.join(str(i) for i in ppv[:3])
        else:
            ppv = '.'.join(str(i) for i in ppv)
    if isinstance(nbv, tuple):
        if len(nbv) > 3:
            nbv = '.'.join(str(i) for i in nbv[:3])
        else:
            nbv = '.'.join(str(i) for i in nbv)

    return TemplateRenderer().render_file('root_init',
                                          version=version_str,
                                          protoplasm_version=ppv,
                                          neobuilder_version=nbv,
                                          package_name=package_name)


