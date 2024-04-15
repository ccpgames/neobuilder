# md5: 36323cc32ccfce021255f28584a556e2
# Auto-Generated file - DO NOT EDIT!
# Source module: sandbox.test.interfaceonly_pb2
# Generated at: 2022-06-26T12:07:56.419594
__all__ = [
    'InterfaceOnlyServiceInterface',
]
import datetime
from typing import *
from protoplasm import plasm

from sandbox.test import interfaceonly_dc as dc

import logging
log = logging.getLogger(__name__)


class InterfaceOnlyServiceInterface:
    def on_hello(self, greeting: str = None) -> str:
        raise plasm.Unimplemented()

