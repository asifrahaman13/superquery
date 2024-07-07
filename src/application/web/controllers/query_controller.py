import asyncio
from fastapi import APIRouter, Depends, Header, WebSocket, WebSocketDisconnect
from src.internal.use_cases.auth_service import AuthService
from src.internal.use_cases.query_service import QueryService
from exports.exports import (
    get_auth_service,
    get_mysql_query_database_service,
    get_postgres_query_database_service,
    get_mongodb_query_database_service,
    websocket_manager as manager,
)

query_controller = APIRouter()


@query_controller.websocket("/mysql-query/{client_id}")
async def query_mysql(
    websocket: WebSocket,
    client_id: str,
    query_service: QueryService = Depends(get_mysql_query_database_service),
    auth_service: AuthService = Depends(get_auth_service),
):

    user = auth_service.user_info(client_id)
    if user is None:
        await websocket.close()
    await manager.connect(websocket, client_id)
    try:
        while True:
            user_input = await websocket.receive_json()
            query = user_input["query"]
            async for response in query_service.query_db(user["sub"], query, "mysql"):
                await asyncio.sleep(0)
                await manager.send_personal_message(response.model_dump(), websocket)
                await asyncio.sleep(0)
    except WebSocketDisconnect:
        await manager.disconnect(websocket)


@query_controller.websocket("/postgres-query/{client_id}")
async def query_mysql(
    websocket: WebSocket,
    client_id: str,
    query_service: QueryService = Depends(get_postgres_query_database_service),
    auth_service: AuthService = Depends(get_auth_service),
):

    user = auth_service.user_info(client_id)
    if user is None:
        await websocket.close()
    await manager.connect(websocket, client_id)
    try:
        while True:
            user_input = await websocket.receive_json()
            query = user_input["query"]
            async for response in query_service.query_db(
                user["sub"], query, "postgres"
            ):
                await asyncio.sleep(0)
                await manager.send_personal_message(response.model_dump(), websocket)
                await asyncio.sleep(0)
    except WebSocketDisconnect:
        await manager.disconnect(websocket)


@query_controller.websocket("/mongodb-query/{client_id}")
async def query_mongodb(
    websocket: WebSocket,
    client_id: str,
    query_service: QueryService = Depends(get_mongodb_query_database_service),
    auth_service: AuthService = Depends(get_auth_service),
):
    user = auth_service.user_info(client_id)
    if user is None:
        await websocket.close()
    await manager.connect(websocket, client_id)
    try:
        while True:
            user_input = await websocket.receive_json()
            query = user_input["query"]
            response = query_service.query_db(user["sub"], query, "mongodb")
            await asyncio.sleep(0)
            await manager.send_personal_message(response, websocket)
            await asyncio.sleep(0)
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
