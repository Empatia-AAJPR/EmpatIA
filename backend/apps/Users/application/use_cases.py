from apps.Accounts.domain.entities import UserEntity
from apps.Accounts.domain.repositories import IHashService, IUserRepository
from apps.Accounts.domain.rules import UserRules
from apps.Users.application.dto import StudentInDTO
from apps.Users.domain.entities import StudentEntity
from apps.Users.domain.repositories import IStudentRepository
from apps.Users.domain.servicies import IStudentQueryService
from apps.Users.infrastructure.adapters.interface_adapter import IImageFileAdapter
from core.exceptions import BaseDomainException


class RegisterStudentUseCase:
    def __init__(self, user_repo: IUserRepository, hash_service: IHashService, student_repo: IStudentRepository, query_service: IStudentQueryService, file_adapter: IImageFileAdapter) -> None:
        self.user_repo = user_repo
        self.hash_service = hash_service
        self.student_repo = student_repo
        self.query_service = query_service
        self.file_adapter = file_adapter

    def execute(self, dto: StudentInDTO):
        if self.user_repo.exists_email(dto.email):
            ...

        password_hash = self.hash_service.hash_password(dto.password)

        file_img = None
        if dto.photo:
            file_img = self.file_adapter.file_upload((dto.photo))

        user = UserEntity(
            name=dto.name,
            email=dto.email,
            password=password_hash,
            rule=UserRules.STUDENT,
        )

        self.user_repo.save(user)

        student = StudentEntity(
            user=user.id,
            classroom=dto.classroom,
            date_birth=dto.date_birth,
            photo=file_img
        )

        self.student_repo.save(student)

        user_student = self.query_service.get_by_id(student.id)
        if not user_student:
            raise BaseDomainException("error in request user student")
        
        return user_student
