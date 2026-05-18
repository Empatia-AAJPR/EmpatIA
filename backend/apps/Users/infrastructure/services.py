from uuid import UUID

from apps.Users.application.dto import StudentOutDTO
from apps.Users.domain.servicies import (
    ICoordinatorQueryService,
    IDirectorQueryService,
    IStudentQueryService,
)
from apps.Users.infrastructure.models import Coordinator, Director, Student
from apps.Users.application.dto import (
    CoordinatorOutDTO,
    DirectorOutDTO,
)


class StudentQueryService(IStudentQueryService):
    def get_by_id(self, id: UUID) -> StudentOutDTO | None:
        student = Student.objects.select_related('user').get(id=id)
        if not student:
            return None

        return StudentOutDTO.from_domain(student)


class CoordinatorQueryService(ICoordinatorQueryService):
    def get_by_id(self, id: UUID) -> CoordinatorOutDTO | None:
        coordinator = Coordinator.objects.select_related('user').get(id=id)
        if not coordinator:
            return None

        return CoordinatorOutDTO.from_domain(coordinator)


class DirectorQueryService(IDirectorQueryService):
    def get_by_id(self, id: UUID) -> DirectorOutDTO | None:
        director = Director.objects.select_related('user').get(id=id)
        if not director:
            return None

        return DirectorOutDTO.from_domain(director)
