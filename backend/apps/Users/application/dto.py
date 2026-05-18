from datetime import date
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr

from apps.Accounts.domain.rules import UserRules
from apps.Users.domain.value_objects import UploadFileVO


class StudentInDTO(BaseModel):
    name: str
    email: EmailStr
    password: str
    date_birth: date
    photo: Optional[UploadFileVO] = None
    classroom: UUID


class StudentOutDTO(BaseModel):
    id: UUID
    name: str
    email: str
    active: bool
    rule: UserRules
    user: UUID
    classroom: UUID
    date_birth: date
    photo: str

    @classmethod
    def from_domain(cls, model):
        return cls(
            id=model.id,
            name=model.user.name,
            email=model.user.email,
            active=model.user.active,
            rule=model.user.rule,
            user=model.user.id,
            classroom=model.classroom.id,
            date_birth=model.date_birth,
            photo=model.photo.url,
        )


class StudentUpdateDTO(BaseModel):
    date_birth: Optional[date] = None
    classroom: Optional[UUID] = None


class CoordinatorInDTO(BaseModel):
    name: str
    email: EmailStr
    password: str
    date_birth: date
    school: UUID


class CoordinatorOutDTO(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    password: str
    rule: UserRules
    active: bool
    user: UUID
    school: UUID

    @classmethod
    def from_domain(cls, model):
        return cls(
            id=model.id,
            user=model.user.id,
            name=model.user.name,
            email=model.user.email,
            password=model.user.password,
            rule=model.user.rule,
            school=model.school.id,
            active=model.user.active,
        )


class CoordinatorUpdateDTO(BaseModel):
    school: Optional[UUID] = None


class DirectorInDTO(BaseModel):
    name: str
    email: EmailStr
    password: str
    school: UUID


class DirectorOutDTO(BaseModel):
    id: UUID
    user: UUID
    name: str
    email: EmailStr
    password: str
    active: bool
    school: UUID

    @classmethod
    def from_domain(cls, model):
        return cls(
            id=model.id,
            user=model.user.id,
            name=model.user.name,
            email=model.user.email,
            password=model.user.password,
            active=model.user.active,
            school=model.school.id,
        )
