from uuid import UUID

from ninja import File, Form, Router, UploadedFile

from django.db import transaction

from apps.Users.api.dependencies import UsersContainer
from apps.Users.api.schemas import StudentIn, StudentOut, UpdateStudentIn
from apps.Users.application.dto import StudentInDTO
from apps.Users.domain.value_objects import UploadFileVO


router_student = Router()

router_coordinator = Router()

container = UsersContainer()


@router_student.post('/', response={201: StudentOut})
@transaction.atomic
def register_student(request, data: Form[StudentIn], img: File[UploadedFile]):
    photo = UploadFileVO(
        name=img.name,
        content=img.read(),
        content_type=img.content_type,
        size=img.size
    )

    dto = StudentInDTO(
        name=data.name,
        email=data.email,
        password=data.password,
        classroom=data.classroom,
        date_birth=data.date_birth,
        photo=photo,
    )

    use_case = container.register_student_use_case()

    student = use_case.execute(dto)

    return 201, StudentOut.from_domain(student)

@router_student.get('/{id}', response={200: StudentOut})
def response_student(request, id: UUID):
    use_case = container.response_student_use_case()

    student = use_case.execute(id)

    return 200, student

@router_student.patch('/{id}', response={200: StudentOut})
@transaction.atomic
def update_student(request, id: UUID, data: UpdateStudentIn):
    dto = data.to_dto()

    use_case = container.update_student_use_case()

    student = use_case.execute(id, dto)

    return 200, StudentOut.from_domain(student)

@router_student.delete('/{id}', response={200: StudentOut})
@transaction.atomic
def deactive_student(request, id: UUID):
    use_case = container.deactive_student_use_case()

    student = use_case.execute(id)

    return 200, student
