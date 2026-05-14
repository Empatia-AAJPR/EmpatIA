from abc import ABC, abstractmethod
from uuid import UUID

from apps.Users.domain.entities import (
    CoordinatorEntity,
    DirectorEntity,
    StudentEntity,
)


class IStudentRepository(ABC):
    @abstractmethod
    def save(self, student: StudentEntity) -> StudentEntity:
        ...

    @abstractmethod
    def find_by_id(self, id: UUID) -> StudentEntity | None:
        ...


class ICoordinatorRepository(ABC):
    @abstractmethod
    def save(self, coordinator: CoordinatorEntity) -> CoordinatorEntity:
        ...

    @abstractmethod
    def find_by_id(self, id: UUID) -> CoordinatorEntity | None:
        ...


class IDirectorRepository(ABC):
    @abstractmethod
    def save(self, director: DirectorEntity) -> DirectorEntity:
        ...

    @abstractmethod
    def find_by_id(self, id: UUID) -> DirectorEntity | None:
        ...
