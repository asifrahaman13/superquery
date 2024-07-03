from fastapi import APIRouter, Depends, Header
from exports.exports import get_auth_service, get_mysql_query_database_service
from src.internal.entities.router_models import QueryBase
from src.internal.use_cases.auth_service import AuthService
from src.internal.use_cases.query_service import QueryService

raw_query_controller = APIRouter()


@raw_query_controller.post("/raw-query")
async def raw_query_mysql(
    query: QueryBase,
    token: str = Header(..., alias="Authorization"),
    query_service: QueryService = Depends(get_mysql_query_database_service),
    auth_service: AuthService = Depends(get_auth_service),
):
    try:
        user = auth_service.user_info(token.split(" ")[1])
        if user is None:
            return {"error": "Some error occured."}
        response = query_service.general_raw_query(
            user["sub"], query.raw_query, query.db_type
        )

        print("############################## controller", response)
        return response
    except Exception as e:
        return {"error": "Some error occured."}
