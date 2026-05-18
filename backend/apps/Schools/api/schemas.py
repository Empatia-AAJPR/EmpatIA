from datetime import datetime
from typing import Optional
from uuid import UUID

from ninja import Schema
from pydantic import field_validator

from apps.Schools.application.dto import (
    SchoolInDTO,
    SchoolOutDTO,
    UpdateSchoolInDTO,
)
from apps.Schools.domain.value_objects import CNPJ
from apps.Users.domain.value_objects import UploadFileVO

from apps.Schools.domain.value_objects import CNPJValidate


class SchoolIn(Schema):
    name: str
    cnpj: str
    gre: str

    @field_validator('cnpj')
    @classmethod
    def validator_cnpj(cls, v):
        validade = CNPJValidate()
        if not validade.validate(v):
            raise ValueError('invalid cnpj')
        return v

    def to_dto(self) -> SchoolInDTO:
        return SchoolInDTO(name=self.name, cnpj=CNPJ(self.cnpj), gre=self.gre)


class SchoolOut(Schema):
    id: UUID
    name: str
    cnpj: str
    logo: Optional[UploadFileVO] | str = None
    gre: str
    deleted_at: datetime | None

    @staticmethod
    def from_domain(dto: SchoolOutDTO):
        return SchoolOut(
            id=dto.id,
            name=dto.name,
            cnpj=dto.cnpj,
            logo=dto.logo if dto.logo else None,
            gre=dto.gre,
            deleted_at=dto.deleted_at,
        )


class UpdateSchoolIn(Schema):
    name: Optional[str] = None
    cnpj: Optional[str] = None
    gre: Optional[str] = None

    @field_validator('cnpj')
    @classmethod
    def validator_cnpj(cls, v):
        if not v:
            return v

        validade = CNPJValidate()
        if not validade.validate(v):
            raise ValueError('invalid cnpj')
        return v

    def to_dto(self) -> UpdateSchoolInDTO:
        return UpdateSchoolInDTO(
            name=self.name,
            cnpj=CNPJ(self.cnpj) if self.cnpj else None,
            gre=self.gre,
        )
