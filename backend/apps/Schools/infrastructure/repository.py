from uuid import UUID

from apps.Schools.domain.entities import SchoolEntity
from apps.Schools.domain.repositories import (
    ISchoolRepository,
)
from apps.Schools.domain.value_objects import CNPJ
from apps.Schools.infrastructure.models import School


class SchoolRepository(ISchoolRepository):
    def save(self, school: SchoolEntity) -> SchoolEntity | None:
        School.objects.update_or_create(
            id=school.id,
            defaults={
                'name': school.name,
                'cnpj': school.cnpj.value,
                'logo': school.logo,
                'gre': school.gre,
                'created_at': school.created_at,
                'deleted_at': school.deleted_at,
            },
        )

        return school

    def find_by_id(self, id: UUID) -> SchoolEntity | None:
        try:
            return self._to_model(School.objects.get(id=id))

        except School.DoesNotExist:
            return None

    def find_by_cnpj(self, cnpj: CNPJ) -> SchoolEntity | None:
        try:
            return self._to_model(School.objects.get(id=cnpj.value))

        except School.DoesNotExist:
            return None

    def existis_cnpj(self, cnpj: CNPJ) -> bool:
        return School.objects.filter(cnpj=cnpj.value).exists()

    def _to_model(self, model: School) -> SchoolEntity:
        return SchoolEntity(
            id=model.id,
            name=model.name,
            cnpj=CNPJ(value=model.cnpj),
            logo=model.logo.name if model.logo else None,
            gre=model.gre,
            created_at=model.created_at,
            deleted_at=model.deleted_at,
        )
