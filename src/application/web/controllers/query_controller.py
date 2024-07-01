from fastapi import APIRouter, Depends
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
    query_service: QueryService = Depends(get_mysql_query_database_service),
):
    try:
        response = query_service.query_db("asifr", query.query, "mysql")
        print("############", response)
        return response
    except Exception as e:
        return {"error": "Some error occured."}


@query_controller.post("/mongodb-query", response_model=dict)
async def query_mongodb(
    query: Query,
    query_service: QueryService = Depends(get_mongodb_query_database_service),
):
    try:
        response = query_service.query_db(query.query)
        return response
    except Exception as e:
        return {"error": "Some error occured."}
