from abc import ABC, abstractmethod
from uuid import UUID

from apps.Users.application.dto import (
    CoordinatorOutDTO,
    DirectorOutDTO,
    StudentOutDTO,
)


class IStudentQueryService(ABC):
    @abstractmethod
    def get_by_id(self, id: UUID) -> StudentOutDTO | None:
        ...


class ICoordinatorQueryService(ABC):
    @abstractmethod
    def get_by_id(self, id: UUID) -> CoordinatorOutDTO | None:
        ...


class IDirectorQueryService(ABC):
    @abstractmethod
    def get_by_id(self, id: UUID) -> DirectorOutDTO | None:
        ...
