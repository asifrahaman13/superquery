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
        "projectName": "",
        "username": "",
        "description": "",
        "connectionString": "",
        "ddlCommands": ["", "", ""],
    },
    "postgres": {
        "db_type": "postgres",
        "projectName": "",
        "username": "",
        "description": ".",
        "connectionString": "",
        "ddlCommands": ["", "", ""],
    },
    "sqlite": {
        "db_type": "sqlite",
        "projectName": "",
        "username": "",
        "description": "",
        "connectionString": "",
        "ddlCommands": ["", "", ""],
    },
    "pinecone": {
        "db_type": "pinecone",
        "projectName": "",
        "username": "",
        "description": "",
        "api_key": "",
        "model_name": "",
        "index_name": "",
        "open_ai_api_key": "",
    },
    "qdrant": {
        "db_type": "qdrant",
        "projectName": "",
        "username": "",
        "description": "",
        "qdrant_api_key": "",
        "open_ai_api_key": "",
        "api_endpoint": "",
        "embedding_model_name": "",
        "collection_name": "",
    },
    "neo4j": {
        "db_type": "neo4j",
        "projectName": "",
        "username": "",
        "description": "",
        "neo4j_password": "",
        "open_ai_api_key": "",
        "api_endpoint": "",
        "embedding_model_name": "",
        "collection_name": "",
    },
}
