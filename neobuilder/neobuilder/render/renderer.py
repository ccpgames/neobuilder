__all__ = [
    'TemplateRenderer',
]
from ccptools.structs import Singleton
import jinja2
import os
import sys

import logging
log = logging.getLogger(__name__)

_PY_3_9_PLUS = sys.version_info >= (3, 9)


def _get_resource_path():
    if _PY_3_9_PLUS:
        from importlib import resources
        return str(resources.files('neobuilder').joinpath('data'))
    else:
        import pkg_resources  # noqa
        return str(pkg_resources.resource_filename('neobuilder', 'data'))  # noqa


class TemplateRenderer(metaclass=Singleton):
    def __init__(self):
        self.template_dir = os.path.join(_get_resource_path(), 'templates')

        self._env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(
                searchpath=self.template_dir
            ),
            lstrip_blocks=True,
            trim_blocks=True,
            undefined=jinja2.ChainableUndefined
        )

    def render_file(self, template_name: str, **kwargs) -> str:
        try:
            # log.debug(f'Rendering {template_name} with: {kwargs!r}')

            template = self._env.get_template(f'{template_name}.jinja2')
            return template.render(**kwargs)
        except Exception as ex:
            log.exception(f'Error in template: {template_name}: {ex!r}')
            raise ex


def main():
    t = TemplateRenderer()
    print(t.render_file('root_init',
                        version='(3, 1, 0, 0)',
                        protoplasm_version='(4, 0, 0, 0)'))


if __name__ == '__main__':
    main()
