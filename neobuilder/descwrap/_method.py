__all__ = [
    'MethodDescriptorWrapper',
]

import dataclasses

from neobuilder.structs import *
from google.protobuf.json_format import descriptor
from protoplasm.casting import castutils


@dataclasses.dataclass
class MethodDescriptorWrapper:
    """This is a wrapper around Google's protobuf MethodDescriptor.

    Its point is twofold.

    1. To mask complex lookups and evaluations behind a simpler facade to use
       in the rest of the code.
    2. To abstract away the exact structure of Google's descriptor to guard
       against future code changes, especially in internal parts that aren't
       part of the official API.
    """
    real_descriptor: descriptor.MethodDescriptor = dataclasses.field(repr=False)

    name: str = dataclasses.field(default='', init=False)
    under_name: str = dataclasses.field(default='', init=False)

    client_streaming: bool = False
    server_streaming: bool = False

    input_type: Optional[descriptor.Descriptor] = dataclasses.field(default=None, init=False, repr=False)
    output_type: Optional[descriptor.Descriptor] = dataclasses.field(default=None, init=False, repr=False)

    io_type: MethodIoType = dataclasses.field(default=MethodIoType._UNKNOWN, init=False)

    service_descriptor: descriptor.ServiceDescriptor = dataclasses.field(default=None, init=False, repr=False)
    file_descriptor: descriptor.FileDescriptor = dataclasses.field(default=None, init=False, repr=False)

    def __post_init__(self):
        self.name = self.real_descriptor.name
        self.under_name = castutils.humps_to_under(self.name)
        self.input_type = self.real_descriptor.input_type
        self.output_type = self.real_descriptor.output_type
        self.client_streaming = self.real_descriptor.client_streaming
        self.server_streaming = self.real_descriptor.server_streaming
        if self.client_streaming:
            self.io_type |= MethodIoType._INPUT_STREAM
        else:
            self.io_type |= MethodIoType._INPUT_UNARY
        if self.server_streaming:
            self.io_type |= MethodIoType._OUTPUT_STREAM
        else:
            self.io_type |= MethodIoType._OUTPUT_UNARY

        self.service_descriptor = self.real_descriptor.containing_service
        self.file_descriptor = self.service_descriptor.file
