from core.exceptions import BaseDomainException


class SchoolNotFoundException(BaseDomainException):
    pass


class ConflictFieldsException(BaseDomainException):
    pass
