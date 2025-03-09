from fastapi import APIRouter, Depends, HTTPException, Header
from fastapi.responses import JSONResponse
from src.exports.index import get_auth_service, get_configuration_service
from src.entities.router_models import ConfigurationBase, UpdateConfig
from src.use_cases.auth_service import AuthService
from src.use_cases.configurations_service import ConfigurationService

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
            return JSONResponse(
                content={"error": "Some error occured."}, status_code=400
            )
        response = await configuration_service.get_project_configurations(
            user["sub"], db_type.db_type
        )
        return JSONResponse(content=response)
    except Exception:
        raise HTTPException(status_code=400, detail="Some error occured.")


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
            return JSONResponse(content={"error": "Not authenticated"}, status_code=401)
        response = await configuration_service.update_project_configurations(
            user["sub"], db_type.db_type, db_type.model_dump()
        )
        return JSONResponse(content=response)
    except Exception:
        raise HTTPException(status_code=400, detail="Some error occured.")
