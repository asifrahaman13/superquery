class DatabaseKeys:
    MYSQL = "mysql"
    POSTGRES = "postgres"
    SQLITE = "sqlite"
    PINECONE = "pinecone"
    QDRANT = "qdrant"
    NEO4J = "neo4j"

    @classmethod
    def get_keys(cls):
        return {
            cls.MYSQL: cls.MYSQL,
            cls.POSTGRES: cls.POSTGRES,
            cls.SQLITE: cls.SQLITE,
            cls.PINECONE: cls.PINECONE,
            cls.QDRANT: cls.QDRANT,
            cls.NEO4J: cls.NEO4J,
        }


INITIAL_DASHBOARD = {
    "mysql": {
        "db_type": "mysql",
        "project_name": "",
        "username": "",
        "description": "",
        "connection_string": "",
        "ddl_commands": [""],
    },
    "postgres": {
        "db_type": "postgres",
        "project_name": "",
        "username": "",
        "description": ".",
        "connection_string": "",
        "ddl_commands": [
            "",
        ],
    },
    "sqlite": {
        "db_type": "sqlite",
        "project_name": "",
        "username": "",
        "description": "",
        "connection_string": "",
        "ddl_commands": [""],
    },
    "neo4j": {
        "db_type": "neo4j",
        "project_name": "",
        "username": "",
        "description": "",
        "neo4j_password": "",
        "api_endpoint": "",
        "ddl_commands": [""],
    },
}
