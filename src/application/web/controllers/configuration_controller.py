from fastapi import APIRouter, Depends, Header
from exports.exports import get_auth_service, get_configuration_service
from src.internal.entities.router_models import ConfigurationBase, UpdateConfig
from src.internal.use_cases.auth_service import AuthService
from src.internal.use_cases.configurations_service import ConfigurationService

configuration_controller = APIRouter()


@configuration_controller.post("/configurations", response_model=dict)
async def get_mysql_configurations(
    db_type: ConfigurationBase,
    token: str = Header(..., alias="Authorization"),
    auth_service: AuthService = Depends(get_auth_service),
    configuration_service: ConfigurationService = Depends(get_configuration_service),
):
    assert token is not None, "Token is required"
    try:
        token = token.split(" ")[1]
        user = auth_service.user_info(token)
        if user is None:
            return {"error": "Some error occured."}
        response = configuration_service.get_project_configurations(
            user["sub"], db_type.db_type
        )
        print("##############################", response)
        return response
    except Exception as e:
        return {"error": "Some error occured."}


@configuration_controller.put("/configurations", response_model=dict)
async def update_mysql_configurations(
    db_type: UpdateConfig,
    token: str = Header(..., alias="Authorization"),
    auth_service: AuthService = Depends(get_auth_service),
    configuration_service: ConfigurationService = Depends(get_configuration_service),
):
    assert token is not None, "Token is required"
    try:
        token = token.split(" ")[1]
        user = auth_service.user_info(token)
        if user is None:
            return {"error": "Not authenticated"}
        response = configuration_service.update_project_configurations(
            user["sub"], db_type.db_type, db_type.model_dump()
        )
        return response
    except Exception as e:
        return {"error": "Some error occured in server."}
