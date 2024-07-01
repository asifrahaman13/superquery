from fastapi import APIRouter, Depends
from src.internal.use_cases.data_service import DataService
from src.internal.entities.auth import Token
from exports.exports import get_database_service

auth_router = APIRouter()


@auth_router.post("/mysql-query", response_model=dict)
async def decode_token(
    token: Token,
    data_service: DataService = Depends(get_database_service),
):
    try:
        id_info = data_service.query_sql(token.token)
        print(id_info)
        return id_info
    except Exception as e:
        return {"error": "Invalid token"}
