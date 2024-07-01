from fastapi import APIRouter, Depends
from src.internal.use_cases.query_service import QueryService
from src.internal.use_cases.data_service import DataService
from src.internal.entities.auth import Token
from exports.exports import get_mysql_query_database_service, get_mongodb_query_database_service

auth_router = APIRouter()


@auth_router.post("/mysql-query", response_model=dict)
async def decode_token(
    token: Token,
    query_service: QueryService = Depends(get_mysql_query_database_service),
):
    try:
        id_info = query_service.query_db(token.token)
        print(id_info)
        return id_info
    except Exception as e:
        return {"error": "Invalid token"}
    

@auth_router.post("/mongodb-query", response_model=dict)
async def decode_token(
    token: Token,
    query_service: QueryService = Depends(get_mongodb_query_database_service),
):
    try:
        id_info = query_service.query_db(token.token)
        print(id_info)
        return id_info
    except Exception as e:
        return {"error": "Invalid token"}