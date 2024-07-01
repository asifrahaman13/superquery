from fastapi import WebSocket
import redis


"""
The ConnectionManager class is responsible for managing WebSocket connections. It stores the WebSocket objects 
in a dictionary with the connection ID as the key. The connection ID is generated when a new connection is established 
and is used to identify the connection in the system. The ConnectionManager uses the redis in memory service to store 
the connections.
"""


class ConnectionManager:
    def __init__(self):
        self.redis_client = redis.Redis(
            host="localhost", port=6379, decode_responses=True
        )
        self.active_connections = {}

    async def connect(
        self,
        websocket: WebSocket,
        connection_id: str,
        connection_type: str = "active_connections",
    ):
        # Generate a unique connection ID

        # Store the connection ID in Redis
        self.redis_client.sadd(connection_type, connection_id)

        # Store the WebSocket object in a dictionary with the connection ID as key
        self.active_connections[connection_id] = websocket

        # Accept the connection
        await websocket.accept()

    async def disconnect(
        self, websocket: WebSocket, connection_type: str = "active_connections"
    ):
        # Find the connection ID for the given WebSocket object
        connection_id = self.find_connection_id(websocket)
        if connection_id:
            # Remove the connection ID from the active_connections set
            self.redis_client.srem(connection_type, connection_id)
            # Remove the connection from the active connections dictionary
            del self.active_connections[connection_id]

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_json(message)

    async def broadcast(self, message: str):
        # Get all active connection IDs
        active_connections = self.redis_client.smembers("active_connections")
        for connection_id in active_connections:
            # Retrieve the WebSocket object for each connection ID
            stored_websocket = self.active_connections.get(connection_id)
            if stored_websocket:
                # Send the message to the WebSocket object
                await stored_websocket.send_text(message)

    def find_connection_id(self, websocket: WebSocket) -> str:
        # Find the connection ID for the given WebSocket object
        for connection_id, stored_websocket in self.active_connections.items():
            if stored_websocket == websocket:
                return connection_id
        return None
