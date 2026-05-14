from uuid import UUID

from apps.Users.application.dto import StudentOutDTO
from apps.Users.domain.servicies import IStudentQueryService
from apps.Users.infrastructure.models import Student


class StudentQueryService(IStudentQueryService):
    def get_by_id(self, id: UUID) -> StudentOutDTO | None:
        student = Student.objects.select_related('user').get(id=id)
        if not student:
            return None
        
        return StudentOutDTO.from_domain(student)
