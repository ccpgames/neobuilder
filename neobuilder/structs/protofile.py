__all__ = [
    'ProtoFile',
]

import dataclasses
import os


@dataclasses.dataclass
class ProtoFile:  # E.g. ./proto/ccpgears/enrichment/ebs/eve/character/character.proto
    name: str  # E.g. character.proto
    path: str  # E.g. ./proto/ccpgears/enrichment/ebs/eve/character/
    rel_path: str  # E.g. ccpgears/enrichment/ebs/eve/character/
    is_grpc_service: bool = dataclasses.field(default=False)

    def full_name(self) -> str:
        return os.path.join(self.path, self.name).replace('\\', '/')

    def pb2_module(self) -> str:
        return f'{os.path.join(self.rel_path, self.name)[:-6].replace("/", ".")}_pb2'.replace('\\', '.')
