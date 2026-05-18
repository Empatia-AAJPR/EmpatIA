from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from apps.Classroom.domain.entities import ClassroomEntity
from apps.Classroom.infrastructure.models import Classroom


class IClassroomRepository(ABC):
    @abstractmethod
    def save(self, classroom: ClassroomEntity) -> ClassroomEntity:
        ...

    @abstractmethod
    def find_by_id(self, id: UUID) -> ClassroomEntity | None:
        ...

    @abstractmethod
    def find_by_course(self, course: str) -> ClassroomEntity | None:
        ...

    @abstractmethod
    def exists_course(self, course: str) -> bool:
        ...

    @abstractmethod
    def list_classrooms_by_school(self, school: UUID) -> List[ClassroomEntity]:
        ...
