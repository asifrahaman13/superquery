from typing import Any, AsyncGenerator, Dict
from src.internal.interfaces.services.query_interface import QueryInterface


class QueryService(QueryInterface):

    def __init__(self, query_database, database) -> None:
        self.query_database = query_database
        self.database = database

    async def query_db(
        self, user: str, query: str, db: str
    ) -> AsyncGenerator[Dict[str, Any], None]:
        if db == "mysql":

            available_mysql_client = self.database.find_single_entity_by_field_name(
                "configurations", "username", user
            )
            if available_mysql_client:
                async for response in self.query_database.query_database(
                    query, available_mysql_client["mysql"]["mysqlConnectionString"]
                ):
                    yield response

    def general_raw_query(self, user: str, query: str, db: str):
        if db == "mysql":
            available_mysql_client = self.database.find_single_entity_by_field_name(
                "configurations", "username", user
            )
            if available_mysql_client:
                return self.query_database.general_raw_query(
                    query, available_mysql_client["mysql"]["mysqlConnectionString"]
                )
        return {"error": "Some error occured."}
