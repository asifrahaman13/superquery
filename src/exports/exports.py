from anthropic import AsyncAnthropicBedrock
from motor.motor_asyncio import AsyncIOMotorClient

from src.config.config import (
    ANTHROPIC_MODEL,
    AWS_ACCESS_KEY_ID,
    AWS_BUCKET_NAME,
    AWS_SECRET_ACCESS_KEY,
    MONGO_DB_URI,
    QDRANT_API_ENDPOINT,
    QDRANT_API_KEY,
)
from src.helper.handle_answer_types import HandleAnswerTypes
from src.helper.llm_response import LlmResponse
from src.repositories.auth_repo import AuthRepo
from src.repositories.aws_repo import AWSRepo
from src.repositories.database_repo import MongodbRepo
from src.repositories.mysql_repo import MySqlQueryRepo
from src.repositories.neo4j_repo import Neo4jQueryRepo
from src.repositories.postgres_repo import PostgresQueryRepo
from src.repositories.semantic_repo import (
    SemanticEmbeddingService,
    SemanticQdrantService,
    SemanticSearchRepo,
)
from src.repositories.sqlite_repos import SqliteQueryRepo
from src.use_cases.auth_service import AuthService
from src.use_cases.configurations_service import ConfigurationService
from src.use_cases.file_service import FileService
from src.use_cases.query_service import QueryService


class DIContainer:
    def __init__(self):
        self.__instances = {}

    def get_auth_repo(self):
        if "auth_repo" not in self.__instances:
            self.__instances["auth_repo"] = AuthRepo()
        return self.__instances["auth_repo"]

    def get_auth_service(self):
        if "auth_service" not in self.__instances:
            self.__instances["auth_service"] = AuthService(
                self.get_auth_repo(), self.get_database_repo()
            )
        return self.__instances["auth_service"]

    def get_database_repo(self):
        if "database_repo" not in self.__instances:
            mongodb_client = AsyncIOMotorClient(MONGO_DB_URI)
            mongodb_database = "octo"
            self.__instances["database_repo"] = MongodbRepo(
                mongodb_client, mongodb_database
            )
        return self.__instances["database_repo"]

    def get_vector_db_repo(self):
        if "vectordb_repoitory" not in self.__instances:
            embedding_service = SemanticEmbeddingService()
            qdrant_service = SemanticQdrantService(
                url=QDRANT_API_ENDPOINT, api_key=QDRANT_API_KEY
            )
            self.__instances["vectordb_repoitory"] = SemanticSearchRepo(
                embedding_service, qdrant_service
            )
        return self.__instances["vectordb_repoitory"]

    def get_mysql_query_repo(self):
        if "mysql_query_repo" not in self.__instances:
            AsyncAnthropicBedrock_client = AsyncAnthropicBedrock()
            self.__instances["mysql_query_repo"] = MySqlQueryRepo(
                HandleAnswerTypes(),
                LlmResponse(
                    AsyncAnthropicBedrock_client,
                    ANTHROPIC_MODEL,
                ),
            )
        return self.__instances["mysql_query_repo"]

    def get_postgres_query_repo(self):
        if "postgres_query_repo" not in self.__instances:
            AsyncAnthropicBedrock_client = AsyncAnthropicBedrock()
            self.__instances["postgres_query_repo"] = PostgresQueryRepo(
                HandleAnswerTypes(),
                LlmResponse(
                    AsyncAnthropicBedrock_client,
                    ANTHROPIC_MODEL,
                ),
            )
        return self.__instances["postgres_query_repo"]

    def get_sqlite_query_repo(self):
        if "sqlite_query_repo" not in self.__instances:
            AsyncAnthropicBedrock_client = AsyncAnthropicBedrock()
            self.__instances["sqlite_query_repo"] = SqliteQueryRepo(
                HandleAnswerTypes(),
                LlmResponse(
                    AsyncAnthropicBedrock_client,
                    ANTHROPIC_MODEL,
                ),
            )
        return self.__instances["sqlite_query_repo"]

    def get_neo4j_query_repo(self):
        if "neo4j_query_repo" not in self.__instances:
            AsyncAnthropicBedrock_client = AsyncAnthropicBedrock()
            self.__instances["neo4j_query_repo"] = Neo4jQueryRepo(
                HandleAnswerTypes(),
                LlmResponse(
                    AsyncAnthropicBedrock_client,
                    ANTHROPIC_MODEL,
                ),
            )
        return self.__instances["neo4j_query_repo"]

    def get_aws_repo(self):
        if "aws_repo" not in self.__instances:
            print(AWS_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
            self.__instances["aws_repo"] = AWSRepo(
                AWS_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
            )
        return self.__instances["aws_repo"]

    def get_mysql_query_database_service(self):
        if "mysql_query_service" not in self.__instances:
            self.__instances["mysql_query_service"] = QueryService(
                self.get_mysql_query_repo(),
                self.get_database_repo(),
                self.get_vector_db_repo(),
            )
        return self.__instances["mysql_query_service"]

    def get_postgres_query_database_service(self):
        if "postgres_query_service" not in self.__instances:
            self.__instances["postgres_query_service"] = QueryService(
                self.get_postgres_query_repo(),
                self.get_database_repo(),
                self.get_vector_db_repo(),
            )
        return self.__instances["postgres_query_service"]

    def get_sqlite_query_database_service(self):
        if "sqlite_query_service" not in self.__instances:
            self.__instances["sqlite_query_service"] = QueryService(
                self.get_sqlite_query_repo(),
                self.get_database_repo(),
                self.get_vector_db_repo(),
            )
        return self.__instances["sqlite_query_service"]

    def get_neo4j_query_database_service(self):
        if "neo4j_query_service" not in self.__instances:
            self.__instances["neo4j_query_service"] = QueryService(
                self.get_neo4j_query_repo(),
                self.get_database_repo(),
                self.get_vector_db_repo(),
            )
        return self.__instances["neo4j_query_service"]

    def get_configuration_service(self):
        if "configuration_service" not in self.__instances:
            self.__instances["configuration_service"] = ConfigurationService(
                self.get_database_repo()
            )
        return self.__instances["configuration_service"]

    def get_aws_service(self):
        if "aws_service" not in self.__instances:
            self.__instances["aws_service"] = FileService(
                self.get_database_repo(), self.get_aws_repo()
            )
        return self.__instances["aws_service"]
