from anthropic import AsyncAnthropicBedrock
from motor.motor_asyncio import AsyncIOMotorClient

from src.helper import HandleAnswerTypes, LlmResponse
from src.repositories import (
    AuthRepo,
    AWSRepo,
    MongodbRepo,
    MySqlQueryRepo,
    Neo4jQueryRepo,
    PostgresQueryRepo,
    SemanticEmbeddingService,
    SemanticQdrantService,
    SemanticSearchRepo,
    SqliteQueryRepo,
)
from src.use_cases import AuthService, ConfigurationService, FileService, QueryService
from src.config.config import config


class DIContainer:
    def __init__(self):
        self.__instances = {}

    def get_auth_repo(self):
        if "auth_repo" not in self.__instances:
            self.__instances["auth_repo"] = AuthRepo(config.secret_key)
        return self.__instances["auth_repo"]

    def get_auth_service(self):
        if "auth_service" not in self.__instances:
            self.__instances["auth_service"] = AuthService(
                self.get_auth_repo(), self.get_database_repo()
            )
        return self.__instances["auth_service"]

    def get_database_repo(self):
        if "database_repo" not in self.__instances:
            mongodb_client = AsyncIOMotorClient(config.mongo_db_uri)
            mongodb_database = "superquery"
            self.__instances["database_repo"] = MongodbRepo(
                mongodb_client, mongodb_database
            )
        return self.__instances["database_repo"]

    def get_vector_db_repo(self):
        if "vectordb_repoitory" not in self.__instances:
            embedding_service = SemanticEmbeddingService()
            qdrant_service = SemanticQdrantService(
                url=config.qdrant_api_endpoint, api_key=config.qdrant_api_key
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
                    config.anthropic_model,
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
                    config.anthropic_model,
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
                    config.anthropic_model,
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
                    config.anthropic_model,
                ),
            )
        return self.__instances["neo4j_query_repo"]

    def get_aws_repo(self):
        if "aws_repo" not in self.__instances:
            print(
                config.aws_bucket_name,
                config.aws_access_key_id,
                config.aws_secret_access_key,
            )
            self.__instances["aws_repo"] = AWSRepo(
                config.aws_bucket_name,
                config.aws_access_key_id,
                config.aws_secret_access_key,
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
