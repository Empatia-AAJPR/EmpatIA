from uuid import UUID

from apps.Schools.application.dto import (
    SchoolInDTO,
    SchoolOutDTO,
    UpdateSchoolInDTO,
)
from apps.Schools.domain.entities import SchoolEntity
from apps.Schools.domain.exceptions import (
    ConflictFieldsException,
    SchoolNotFoundException,
)
from apps.Schools.domain.repositories import (
    ISchoolRepository,
)
from apps.Schools.domain.value_objects import CNPJ
from apps.Schools.infrastructure.adapters.i_file_adapter import (
    IImageFileAdapter,
)
from core.exceptions import BaseDomainException


class RegisterSchoolUseCase:
    def __init__(
        self, school_repo: ISchoolRepository, file_adapter: IImageFileAdapter
    ):
        self.school_repo = school_repo
        self.file_adapter = file_adapter

    def execute(self, dto: SchoolInDTO):
        if self.school_repo.existis_cnpj(dto.cnpj):
            raise ConflictFieldsException('cnpj already register')

        logo = None
        if dto.logo:
            logo = self.file_adapter.file_upload(dto.logo)

            if not logo:
                raise BaseDomainException('logo not found for register')

        school = SchoolEntity(
            name=dto.name, cnpj=dto.cnpj, gre=dto.gre, logo=logo
        )
        self.school_repo.save(school)

        return SchoolOutDTO.from_domain(school)


class ResponseSchoolByIDUseCase:
    def __init__(self, school_repo: ISchoolRepository) -> None:
        self.school_repo = school_repo

    def execute(self, id: UUID):
        school = self.school_repo.find_by_id(id)

        if not school:
            raise SchoolNotFoundException('school not found')

        return SchoolOutDTO.from_domain(school)


class ResponseSchoolByCNPJUseCase:
    def __init__(self, school_repo: ISchoolRepository) -> None:
        self.school_repo = school_repo

    def execute(self, cnpj: CNPJ):
        school = self.school_repo.find_by_cnpj(cnpj)
        if not school:
            raise SchoolNotFoundException('school not found')

        return SchoolOutDTO.from_domain(school)


class UpdateSchoolUseCase:
    def __init__(self, school_repo: ISchoolRepository) -> None:
        self.school_repo = school_repo

    def execute(self, id: UUID, dto: UpdateSchoolInDTO):
        school = self.school_repo.find_by_id(id)
        if not school:
            raise SchoolNotFoundException('school not found')

        if dto.name:
            school.change_name(dto.name)

        if dto.cnpj:
            school.change_cnpj(dto.cnpj)

        if dto.gre:
            school.change_gre(dto.gre)

        self.school_repo.save(school)

        return SchoolOutDTO.from_domain(school)


class DeactiveSchoolUseCase:
    def __init__(self, school_repo: ISchoolRepository) -> None:
        self.school_repo = school_repo

    def execute(self, id: UUID):
        school = self.school_repo.find_by_id(id)
        if not school:
            raise SchoolNotFoundException('school not found')

        school.deactive()

        self.school_repo.save(school)

        return SchoolOutDTO.from_domain(school)
