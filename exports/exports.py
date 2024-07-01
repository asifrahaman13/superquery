from src.ConnectionManager.ConnectionManager import ConnectionManager
from src.infastructure.repositories.database_repository import (
    DatabaseRepository,
)
from src.infastructure.repositories.auth_repository import AuthRepository
from src.internal.use_cases.auth_service import AuthService
from src.internal.use_cases.database_service import DatabaseService


"""
The connection manager is a class that manages the connections to the websocket.
This is used by multiple services and endpoints.
"""
manager = ConnectionManager()


"""
The database repository is a class that manages the connection to the database.
Multiple services use this repository to interact with the database.
"""
database_repository = DatabaseRepository()
database_service = DatabaseService(database_repository)
database_interface = DatabaseService(database_service)

""" 
Authentication module helps to authenticate the user and generate access tokens.
"""
auth_repository = AuthRepository()
auth_service = AuthService(auth_repository)
auth_interface = AuthService(auth_service)


