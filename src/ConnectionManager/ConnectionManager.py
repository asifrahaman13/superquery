from fastapi import WebSocket
import redis


class ConnectionManager:
    def __init__(self, redis_host: str, redis_port: str, redis_password: str):
        self.redis_client = redis.Redis(
            host=redis_host, port=redis_port, password=redis_password
        )
        self.active_connections = {}

    async def connect(
        self,
        websocket: WebSocket,
        connection_id: str,
        connection_type: str = "active_connections",
    ):
        self.redis_client.sadd(connection_type, connection_id)
        self.active_connections[connection_id] = websocket
        await websocket.accept()

    async def disconnect(
        self, websocket: WebSocket, connection_type: str = "active_connections"
    ):
        connection_id = self.find_connection_id(websocket)
        if connection_id:
            self.redis_client.srem(connection_type, connection_id)
            del self.active_connections[connection_id]

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_json(message)

    async def broadcast(self, message: str):
        active_connections = self.redis_client.smembers("active_connections")
        for connection_id in active_connections:
            stored_websocket = self.active_connections.get(connection_id)
            if stored_websocket:
                await stored_websocket.send_text(message)

    def find_connection_id(self, websocket: WebSocket) -> str:
        for connection_id, stored_websocket in self.active_connections.items():
            if stored_websocket == websocket:
                return connection_id
        return None
