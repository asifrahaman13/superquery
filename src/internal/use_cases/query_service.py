from src.internal.interfaces.services.query_interface import QueryInterface


class QueryService(QueryInterface):
    
    def __init__(self, query_database) -> None:
        self.query_database=query_database

    def query_db(self, query: str) -> dict:
        return self.query_database.query_database(query)