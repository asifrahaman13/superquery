from src.use_cases.query_service import QueryService


class QueryServiceMapping:
    MYSQL = "mysql"
    POSTGRES = "postgres"
    SQLITE = "sqlite"
    NEO4J = "neo4j"

    @classmethod
    def get_mapping(
        cls,
        mysql_service: QueryService,
        postgres_service: QueryService,
        sqlite_service: QueryService,
        neo4j_service: QueryService,
    ):
        return {
            cls.MYSQL: (mysql_service, "table"),
            cls.POSTGRES: (postgres_service, "table"),
            cls.SQLITE: (sqlite_service, "table"),
            cls.NEO4J: (neo4j_service, "json"),
        }
