from pydantic.dataclasses import dataclass

from validate_docbr import CNPJ as CNPJValidate


@dataclass(frozen=True)
class CNPJ:
    value: str

    def __post_init__(self):
        if self.value == '':
            return

        validate = CNPJValidate()
        if not validate.validate(self.value):
            raise ValueError(f'invalide cnpj: {self.value}')
