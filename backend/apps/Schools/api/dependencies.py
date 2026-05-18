from dependency_injector import containers, providers

from apps.Schools.application.use_cases import (
    DeactiveSchoolUseCase,
    RegisterSchoolUseCase,
    ResponseSchoolByCNPJUseCase,
    ResponseSchoolByIDUseCase,
    UpdateSchoolUseCase,
)
from apps.Schools.infrastructure.adapters.file_adapters import ImageFileAdapter
from apps.Schools.infrastructure.repository import (
    SchoolRepository,
)


class SchoolsContainer(containers.DeclarativeContainer):
    school_repo = providers.Factory(SchoolRepository)

    file_adapter = providers.Factory(ImageFileAdapter)

    register_school_use_case = providers.Factory(
        RegisterSchoolUseCase,
        school_repo=school_repo,
        file_adapter=file_adapter,
    )

    response_school_by_id_use_case = providers.Factory(
        ResponseSchoolByIDUseCase, school_repo=school_repo
    )

    response_school_by_cnpj_use_case = providers.Factory(
        ResponseSchoolByCNPJUseCase, school_repo=school_repo
    )

    update_school_use_case = providers.Factory(
        UpdateSchoolUseCase, school_repo=school_repo
    )

    dective_school_use_case = providers.Factory(
        DeactiveSchoolUseCase, school_repo=school_repo
    )
