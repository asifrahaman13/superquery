from src.infastructure.repositories.neo4j_query_repository import Neo4jQueryRepository
from src.infastructure.repositories.helper.embeddings_assistant import EmbeddingService
from src.infastructure.repositories.helper.qdrant_service_assistant import QdrantService
from src.infastructure.repositories.qdrant_query_repository import QdrantQueryRepository
from src.infastructure.repositories.sqlite_query_repository import SqliteQueryRepository
from src.internal.use_cases.configurations_service import ConfigurationService
from src.internal.use_cases.auth_service import AuthService
from src.infastructure.repositories.auth_repository import AuthRepository
from src.infastructure.repositories.mongodb_query_repository import (
    MongodbQueryRepository,
)
from src.infastructure.repositories.mysql_query_repository import MySqlQueryRepository
from src.infastructure.repositories.postgres_query_repository import (
    PostgresQueryRepository,
)
from src.infastructure.repositories.pinecone_query_repository import (
    PineconeQueryRepository,
)
from src.internal.use_cases.query_service import QueryService
from src.ConnectionManager.ConnectionManager import ConnectionManager
from src.infastructure.repositories.database_repository import (
    MongodbRepository,
)
from src.infastructure.repositories.helper.handle_answer_types import HandleAnswerTypes
from pymongo import MongoClient
from config.config import MONGO_DB_URI, OPEN_AI_API_KEY
from config.config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD
from src.infastructure.repositories.helper.llm_response import LlmResponse


class DIContainer:
    def __init__(self):
        self.__instances = {}

    def get_auth_repository(self):
        if "auth_repository" not in self.__instances:
            self.__instances["auth_repository"] = AuthRepository()
        return self.__instances["auth_repository"]

    def get_auth_service(self):
        if "auth_service" not in self.__instances:
            self.__instances["auth_service"] = AuthService(
                self.get_auth_repository(), self.get_database_repository()
            )
        return self.__instances["auth_service"]

    def get_database_repository(self):
        if "database_repository" not in self.__instances:
            mongodb_client = MongoClient(MONGO_DB_URI)
            mongodb_database = "octo"
            self.__instances["database_repository"] = MongodbRepository(
                mongodb_client, mongodb_database
            )
        return self.__instances["database_repository"]

    def get_mysql_query_repository(self):
        if "mysql_query_repository" not in self.__instances:
            self.__instances["mysql_query_repository"] = MySqlQueryRepository(
                HandleAnswerTypes()
            )
        return self.__instances["mysql_query_repository"]

    def get_postgres_query_repository(self):
        if "postgres_query_repository" not in self.__instances:
            self.__instances["postgres_query_repository"] = PostgresQueryRepository(
                HandleAnswerTypes()
            )
        return self.__instances["postgres_query_repository"]

    def get_sqlite_query_repository(self):
        if "sqlite_query_repository" not in self.__instances:
            self.__instances["sqlite_query_repository"] = SqliteQueryRepository(
                HandleAnswerTypes()
            )
        return self.__instances["sqlite_query_repository"]

    def get_mongodb_query_repository(self):
        if "mongodb_query_repository" not in self.__instances:
            self.__instances["mongodb_query_repository"] = MongodbQueryRepository(
                MongoClient(MONGO_DB_URI), "test"
            )
        return self.__instances["mongodb_query_repository"]

    def get_pinecone_query_repository(self):
        if "pinecone_query_repository" not in self.__instances:
            self.__instances["pinecone_query_repository"] = PineconeQueryRepository()
        return self.__instances["pinecone_query_repository"]

    def get_qdrant_query_repository(self):
        if "qdrant_query_repository" not in self.__instances:

            embedding_service: EmbeddingService = EmbeddingService()
            qdrant_service: QdrantService = QdrantService()
            self.__instances["qdrant_query_repository"] = QdrantQueryRepository(
                embedding_service, qdrant_service 
            )
        return self.__instances["qdrant_query_repository"]
    
    def get_neo4j_query_repository(self):
        if "neo4j_query_repository" not in self.__instances:
            self.__instances["neo4j_query_repository"] = Neo4jQueryRepository()
        return self.__instances["neo4j_query_repository"]

    def get_mysql_query_database_service(self):
        if "mysql_query_service" not in self.__instances:

            self.__instances["mysql_query_service"] = QueryService(
                self.get_mysql_query_repository(), self.get_database_repository()
            )
        return self.__instances["mysql_query_service"]

    def get_postgres_query_database_service(self):
        if "postgres_query_service" not in self.__instances:
            self.__instances["postgres_query_service"] = QueryService(
                self.get_postgres_query_repository(), self.get_database_repository()
            )
        return self.__instances["postgres_query_service"]

    def get_sqlite_query_database_service(self):
        if "sqlite_query_service" not in self.__instances:
            self.__instances["sqlite_query_service"] = QueryService(
                self.get_sqlite_query_repository(), self.get_database_repository()
            )
        return self.__instances["sqlite_query_service"]

    def get_mongodb_query_database_service(self):
        if "mongodb_query_service" not in self.__instances:
            self.__instances["mongodb_query_service"] = QueryService(
                self.get_mongodb_query_repository(), self.get_database_repository()
            )
        return self.__instances["mongodb_query_service"]

    def get_pinecone_query_database_service(self):
        if "pinecone_query_service" not in self.__instances:
            self.__instances["pinecone_query_service"] = QueryService(
                self.get_pinecone_query_repository(), self.get_database_repository()
            )
        return self.__instances["pinecone_query_service"]
    
    def get_qdrant_query_database_service(self):
        if "qdrant_query_service" not in self.__instances:
            self.__instances["qdrant_query_service"] = QueryService(
                self.get_qdrant_query_repository(), self.get_database_repository()
            )
        return self.__instances["qdrant_query_service"]
    
    def get_neo4j_query_database_service(self):
        if "neo4j_query_service" not in self.__instances:
            self.__instances["neo4j_query_service"] = QueryService(
                self.get_neo4j_query_repository(), self.get_database_repository()
            )
        return self.__instances["neo4j_query_service"]

    def get_configuration_service(self):
        if "configuration_service" not in self.__instances:
            self.__instances["configuration_service"] = ConfigurationService(
                self.get_database_repository()
            )
        return self.__instances["configuration_service"]


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
