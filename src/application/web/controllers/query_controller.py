import asyncio
from fastapi import APIRouter, Depends, Response, WebSocket, WebSocketDisconnect
from src.entities.router_models import TrainData
from src.use_cases.auth_service import AuthService
from src.use_cases.query_service import QueryService
from src.exports.index import (
    get_auth_service,
    get_mysql_query_database_service,
    get_neo4j_query_database_service,
    get_pinecone_query_database_service,
    get_postgres_query_database_service,
    get_qdrant_query_database_service,
    get_sqlite_query_database_service,
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
    except WebSocketDisconnect:
        await manager.disconnect(websocket)


@query_controller.websocket("/postgres-query/{client_id}")
async def query_postgres(
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
    except WebSocketDisconnect:
        await manager.disconnect(websocket)


@query_controller.websocket("/sqlite-query/{client_id}")
async def query_sqlite(
    websocket: WebSocket,
    client_id: str,
    query_service: QueryService = Depends(get_sqlite_query_database_service),
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
            async for response in query_service.query_db(user["sub"], query, "sqlite"):
                await asyncio.sleep(0)
                await manager.send_personal_message(response.model_dump(), websocket)
    except WebSocketDisconnect:
        await manager.disconnect(websocket)


@query_controller.websocket("/pinecone-query/{client_id}")
async def query_pinecone(
    websocket: WebSocket,
    client_id: str,
    query_service: QueryService = Depends(get_pinecone_query_database_service),
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
                user["sub"], query, "pinecone"
            ):
                await asyncio.sleep(0)
                await manager.send_personal_message(response.model_dump(), websocket)
    except WebSocketDisconnect:
        await manager.disconnect(websocket)


@query_controller.websocket("/qdrant-query/{client_id}")
async def query_qdrant(
    websocket: WebSocket,
    client_id: str,
    query_service: QueryService = Depends(get_qdrant_query_database_service),
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
            async for response in query_service.query_db(user["sub"], query, "qdrant"):
                await asyncio.sleep(0)
                await manager.send_personal_message(response.model_dump(), websocket)
    except WebSocketDisconnect:
        await manager.disconnect(websocket)


@query_controller.websocket("/neo4j-query/{client_id}")
async def query_neo4j(
    websocket: WebSocket,
    client_id: str,
    query_service: QueryService = Depends(get_neo4j_query_database_service),
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
            async for response in query_service.query_db(user["sub"], query, "neo4j"):
                print("Response:", response)
                await asyncio.sleep(0)
                await manager.send_personal_message(response.model_dump(), websocket)
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
    except Exception as e:
        await manager.disconnect(websocket)


@query_controller.post("/data")
async def train_model(
    train_data: TrainData,
    query_service: QueryService = Depends(get_sqlite_query_database_service),
):
    try:
        response = query_service.add_data_to_vector_db(
            train_data.user_query, train_data.sql_query, train_data.source
        )
        if response is True:
            return Response(status_code=200, content="Data added successfully")
    except Exception as e:
        return Response(status_code=500, content="Internal Server Error")
