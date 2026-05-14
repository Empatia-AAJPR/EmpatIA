from datetime import date
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr

from apps.Accounts.domain.rules import UserRules
from apps.Users.domain.value_objects import UploadFileVO


class StudentInDTO(BaseModel):
    user: UUID
    name: str
    email: EmailStr
    password: str
    classroom: UUID
    date_birth: date
    photo: UploadFileVO


class StudentOutDTO(BaseModel):
    id: UUID
    name: str
    email: str
    active: bool
    rule: UserRules
    user: UUID
    classroom: UUID
    date_birth: date
    photo: UploadFileVO

    @classmethod
    def from_domain(cls, model):
        return cls(
            id=model.id,
            name=model.user.name,
            email=model.user.email,
            active=model.user.active,
            rule=model.user.rule,
            user=model.user.id,
            classroom=model.classroom,
            date_birth=model.date_birth,
            photo=model.photo.url,
        )


class StudentUpdateDTO(BaseModel):
    classroom: Optional[UUID] = None
    date_birth: Optional[date] = None


class CoordinatorInDTO(BaseModel):
    user: UUID
    nucleos_group: UUID


class CoordinatorOutDTO(BaseModel):
    id: UUID
    user: UUID
    nucleos_group: UUID

    @classmethod
    def from_domain(cls, model):
        return cls(
            id=model.id, user=model.user, nucleos_group=model.nucleos_group
        )


class DirectorInDTO(BaseModel):
    user: UUID


class DirectorOutDTO(BaseModel):
    id: UUID
    user: UUID

    @classmethod
    def from_domain(cls, model):
        return cls(id=model.id, user=model.user)
