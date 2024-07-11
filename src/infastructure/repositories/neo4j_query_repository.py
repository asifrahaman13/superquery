from neo4j import GraphDatabase


class Neo4jDriver:
    def __init__(self, connection_string: str, auth: tuple):
        self.driver = GraphDatabase.driver(connection_string, auth=auth)

    def __enter__(self):
        self.session = self.driver.session()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()
        self.driver.close()

    def query(self, query: str, parameters=None):
        if parameters is None:
            parameters = {}
        print("Querying Neo4j:", query, parameters)
        with self.session.begin_transaction() as tx:
            result = tx.run(query, parameters)
            return result.data()


class Neo4jQueryRepository:

    @staticmethod
    def query_database(query: str, *args, **kwargs):
        auth = (kwargs.get("username"), kwargs.get("neo4j_password"))
        connection_string = kwargs.get("api_endpoint")
        with Neo4jDriver(connection_string, auth) as driver:
            result = driver.query(query)
            return result

    @staticmethod
    def general_raw_query(query: str, *args, **kwargs):
        auth = (kwargs.get("username"), kwargs.get("neo4j_password"))
        connection_string = kwargs.get("api_endpoint")
        with Neo4jDriver(connection_string, auth) as driver:
            result = driver.query(query)
            return result
