from src.use_cases.query_service import QueryService


class QueryServiceMapping:
    MYSQL = "mysql"
    POSTGRES = "postgres"
    SQLITE = "sqlite"
    PINECONE = "pinecone"
    QDRANT = "qdrant"
    NEO4J = "neo4j"

    @classmethod
    def get_mapping(
        cls,
        mysql_service: QueryService,
        postgres_service: QueryService,
        sqlite_service: QueryService,
        pinecone_service: QueryService,
        qdrant_service: QueryService,
        neo4j_service: QueryService,
    ):
        return {
            cls.MYSQL: (mysql_service, "table"),
            cls.POSTGRES: (postgres_service, "table"),
            cls.SQLITE: (sqlite_service, "table"),
            cls.PINECONE: (pinecone_service, "json"),
            cls.QDRANT: (qdrant_service, "json"),
            cls.NEO4J: (neo4j_service, "json"),
        }
