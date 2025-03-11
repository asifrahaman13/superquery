import asyncio

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Header,
    Response,
    WebSocket,
    WebSocketDisconnect,
)

from src.model.router_models import TrainData
from src.use_cases import QueryService, AuthService
from src.exports import (
    get_auth_service,
    get_mysql_query_database_service,
    get_neo4j_query_database_service,
    get_postgres_query_database_service,
    get_sqlite_query_database_service,
    websocket_manager as manager,
)
from src.model import Databases

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
            async for response in query_service.query_db(
                user["sub"], query, Databases.MYSQL.value
            ):
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
                user["sub"], query, Databases.POSTGRES.value
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
            async for response in query_service.query_db(
                user["sub"], query, Databases.SQLITE.value
            ):
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
            async for response in query_service.query_db(
                user["sub"], query, Databases.NEO4J.value
            ):
                print("Response:", response)
                await asyncio.sleep(0)
                await manager.send_personal_message(response.model_dump(), websocket)
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
    except Exception:
        await manager.disconnect(websocket)


@query_controller.post("/data")
async def train_model(
    train_data: TrainData,
    token: str = Header(..., alias="Authorization"),
    auth_service: AuthService = Depends(get_auth_service),
    query_service: QueryService = Depends(get_sqlite_query_database_service),
):
    try:
        user = auth_service.user_info(token.split(" ")[1])
        if user is None:
            raise HTTPException(status_code=401, detail="Authentication failed")

        train_data.metadata = [
            {
                "user": user["sub"],
                "database": train_data.metadata[0]["database"],
            }
        ]
        response = await query_service.add_data_to_vector_db(
            train_data.user_query, train_data.sql_query, train_data.metadata
        )
        if response is True:
            return Response(status_code=200, content="Data added successfully")
    except Exception:
        return HTTPException(status_code=500, detail="Failed to add data")
