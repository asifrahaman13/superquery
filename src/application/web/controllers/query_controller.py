from fastapi import APIRouter, Depends
from exports.dependency_utils import get_current_user
from src.internal.use_cases.query_service import QueryService
from src.internal.entities.router_models import Query
from exports.exports import (
    get_mysql_query_database_service,
    get_mongodb_query_database_service,
)

query_controller = APIRouter()


@query_controller.post("/mysql-query", response_model=dict)
async def query_mysql(
    query: Query,
    user: dict = Depends(get_current_user),
    query_service: QueryService = Depends(get_mysql_query_database_service),
):
    try:
        response = query_service.query_db(user["sub"], query.query, "mysql")
        return response
    except Exception as e:
        return {"error": "Some error occurred."}


@query_controller.post("/mongodb-query", response_model=dict)
async def query_mongodb(
    query: Query,
    user: dict = Depends(get_current_user),
    query_service: QueryService = Depends(get_mongodb_query_database_service),
):
    try:
        response = query_service.query_db(user["sub"], query.query)
        return response
    except Exception as e:
        return {"error": "Some error occurred."}
