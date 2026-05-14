from dataclasses import dataclass

from core.exceptions import BaseDomainException


@dataclass(frozen=True)
class UploadFileVO:
    name: str
    content: bytes
    content_type: str | None
    size: int

    def __post_init__(self):
        allowed_method = ['image/jpeg', 'image/png', 'image/webp']

        if self.content_type not in allowed_method:
            raise BaseDomainException('file not compatible')

        if self.size > 5 * 1024 * 1024:
            raise ValueError('file is high')
