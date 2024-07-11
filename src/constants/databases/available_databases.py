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
