from fastapi import APIRouter, Depends
from src.internal.use_cases.query_service import QueryService
from src.internal.use_cases.data_service import DataService
from src.internal.entities.auth import Token
from exports.exports import get_mysql_query_database_service, get_mongodb_query_database_service

query_controller = APIRouter()


@query_controller.post("/mysql-query", response_model=dict)
async def query_mysql(
    token: Token,
    query_service: QueryService = Depends(get_mysql_query_database_service),
):
    try:
        id_info = query_service.query_db(token.token)
        print(id_info)
        return id_info
    except Exception as e: 
        return {"error": "Invalid token"}

@query_controller.post("/mongodb-query", response_model=dict)
async def query_mongodb(
    token: Token,
    query_service: QueryService = Depends(get_mongodb_query_database_service),
):
    try:
        id_info = query_service.query_db(token.token)
        print(id_info)
        return id_info
    except Exception as e:
        return {"error": "Some error occured."}