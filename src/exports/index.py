from src.exports.exports import DIContainer
from src.ConnectionManager.ConnectionManager import ConnectionManager
from src.config.config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD

container = DIContainer()
websocket_manager = ConnectionManager(REDIS_HOST, REDIS_PORT, REDIS_PASSWORD)


def get_mysql_query_database_service():
    return container.get_mysql_query_database_service()


def get_postgres_query_database_service():
    return container.get_postgres_query_database_service()


def get_sqlite_query_database_service():
    return container.get_sqlite_query_database_service()


def get_mongodb_query_database_service():
    return container.get_mongodb_query_database_service()


def get_pinecone_query_database_service():
    return container.get_pinecone_query_database_service()


def get_qdrant_query_database_service():
    return container.get_qdrant_query_database_service()


def get_neo4j_query_database_service():
    return container.get_neo4j_query_database_service()


def get_auth_service():
    return container.get_auth_service()


def get_configuration_service():
    return container.get_configuration_service()


def get_aws_service():
    return container.get_aws_service()
