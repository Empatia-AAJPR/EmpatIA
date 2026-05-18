from core.exceptions import BaseDomainException


class UserNotFoundException(BaseDomainException):
    pass


class ConflictEntityException(BaseDomainException):
    pass
