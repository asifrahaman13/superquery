from anthropic import AsyncAnthropicBedrock
from src.infastructure.repositories.semantic_repo import (
    SemanticEmbeddingService,
    SemanticQdrantService,
    SemanticSearchRepo,
)
from src.use_cases.file_service import FileService
from src.infastructure.repositories.aws_repository import AWSRepo
from src.infastructure.repositories.neo4j_repo import Neo4jQueryRepo
from src.helper.embeddings_assistant import EmbeddingService
from src.helper.qdrant_service_assistant import QdrantService
from src.infastructure.repositories.qdrant_repo import QdrantQueryRepo
from src.infastructure.repositories.sqlite_repos import SqliteQueryRepo
from src.use_cases.configurations_service import ConfigurationService
from src.use_cases.auth_service import AuthService
from src.infastructure.repositories.auth_repository import AuthRepo
from src.infastructure.repositories.mysql_repo import MySqlQueryRepo
from src.infastructure.repositories.postgres_repo import (
    PostgresQueryRepo,
)
from src.infastructure.repositories.pinecone_repo import (
    PineconeQueryRepo,
)
from src.use_cases.query_service import QueryService
from src.infastructure.repositories.database_repo import (
    MongodbRepo,
)
from src.helper.handle_answer_types import HandleAnswerTypes
from pymongo import MongoClient
from src.config.config import (
    MONGO_DB_URI,
    QDRANT_API_ENDPOINT,
    QDRANT_API_KEY,
)
from src.config.config import (
    AWS_ACCESS_KEY_ID,
    AWS_BUCKET_NAME,
    AWS_SECRET_ACCESS_KEY,
)
from src.helper.llm_response import LlmResponse
from src.config.config import ANTHROPIC_MODEL


class DIContainer:
    def __init__(self):
        self.__instances = {}

    def get_auth_repository(self):
        if "auth_repository" not in self.__instances:
            self.__instances["auth_repository"] = AuthRepo()
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
            self.__instances["database_repository"] = MongodbRepo(
                mongodb_client, mongodb_database
            )
        return self.__instances["database_repository"]

    def get_vector_db_repository(self):
        if "vectordb_repoitory" not in self.__instances:
            embedding_service = SemanticEmbeddingService()
            qdrant_service = SemanticQdrantService(
                url=QDRANT_API_ENDPOINT, api_key=QDRANT_API_KEY
            )
            self.__instances["vectordb_repoitory"] = SemanticSearchRepo(
                embedding_service, qdrant_service
            )
        return self.__instances["vectordb_repoitory"]

    def get_mysql_query_repository(self):
        if "mysql_query_repository" not in self.__instances:
            AsyncAnthropicBedrock_client = AsyncAnthropicBedrock()
            self.__instances["mysql_query_repository"] = MySqlQueryRepo(
                HandleAnswerTypes(),
                LlmResponse(
                    AsyncAnthropicBedrock_client,
                    ANTHROPIC_MODEL,
                ),
            )
        return self.__instances["mysql_query_repository"]

    def get_postgres_query_repository(self):
        if "postgres_query_repository" not in self.__instances:
            AsyncAnthropicBedrock_client = AsyncAnthropicBedrock()
            self.__instances["postgres_query_repository"] = PostgresQueryRepo(
                HandleAnswerTypes(),
                LlmResponse(
                    AsyncAnthropicBedrock_client,
                    ANTHROPIC_MODEL,
                ),
            )
        return self.__instances["postgres_query_repository"]

    def get_sqlite_query_repository(self):
        if "sqlite_query_repository" not in self.__instances:
            AsyncAnthropicBedrock_client = AsyncAnthropicBedrock()
            self.__instances["sqlite_query_repository"] = SqliteQueryRepo(
                HandleAnswerTypes(),
                LlmResponse(
                    AsyncAnthropicBedrock_client,
                    ANTHROPIC_MODEL,
                ),
            )
        return self.__instances["sqlite_query_repository"]

    def get_pinecone_query_repository(self):
        if "pinecone_query_repository" not in self.__instances:
            self.__instances["pinecone_query_repository"] = PineconeQueryRepo()
        return self.__instances["pinecone_query_repository"]

    def get_qdrant_query_repository(self):
        if "qdrant_query_repository" not in self.__instances:
            embedding_service: EmbeddingService = EmbeddingService()
            qdrant_service: QdrantService = QdrantService()
            self.__instances["qdrant_query_repository"] = QdrantQueryRepo(
                embedding_service, qdrant_service
            )
        return self.__instances["qdrant_query_repository"]

    def get_neo4j_query_repository(self):
        if "neo4j_query_repository" not in self.__instances:
            self.__instances["neo4j_query_repository"] = Neo4jQueryRepo()
        return self.__instances["neo4j_query_repository"]

    def get_aws_repository(self):
        if "aws_repository" not in self.__instances:
            print(AWS_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
            self.__instances["aws_repository"] = AWSRepo(
                AWS_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
            )
        return self.__instances["aws_repository"]

    def get_mysql_query_database_service(self):
        if "mysql_query_service" not in self.__instances:
            self.__instances["mysql_query_service"] = QueryService(
                self.get_mysql_query_repository(),
                self.get_database_repository(),
                self.get_vector_db_repository(),
            )
        return self.__instances["mysql_query_service"]

    def get_postgres_query_database_service(self):
        if "postgres_query_service" not in self.__instances:
            self.__instances["postgres_query_service"] = QueryService(
                self.get_postgres_query_repository(),
                self.get_database_repository(),
                self.get_vector_db_repository(),
            )
        return self.__instances["postgres_query_service"]

    def get_sqlite_query_database_service(self):
        if "sqlite_query_service" not in self.__instances:
            self.__instances["sqlite_query_service"] = QueryService(
                self.get_sqlite_query_repository(),
                self.get_database_repository(),
                self.get_vector_db_repository(),
            )
        return self.__instances["sqlite_query_service"]

    def get_mongodb_query_database_service(self):
        if "mongodb_query_service" not in self.__instances:
            self.__instances["mongodb_query_service"] = QueryService(
                self.get_mongodb_query_repository(),
                self.get_database_repository(),
                self.get_vector_db_repository(),
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
                self.get_neo4j_query_repository(),
                self.get_database_repository(),
                self.get_vector_db_repository(),
            )
        return self.__instances["neo4j_query_service"]

    def get_configuration_service(self):
        if "configuration_service" not in self.__instances:
            self.__instances["configuration_service"] = ConfigurationService(
                self.get_database_repository()
            )
        return self.__instances["configuration_service"]

    def get_aws_service(self):
        if "aws_service" not in self.__instances:
            self.__instances["aws_service"] = FileService(
                self.get_database_repository(), self.get_aws_repository()
            )
        return self.__instances["aws_service"]
