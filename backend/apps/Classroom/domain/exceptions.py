from core.exceptions import BaseDomainException


class ConflictFieldsExceptions(BaseDomainException):
    pass


class FieldISRequiredException(BaseDomainException):
    pass


class ClassroomNotFound(BaseDomainException):
    pass
