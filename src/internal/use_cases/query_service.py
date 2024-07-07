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
                    query, available_mysql_client["mysql"]["connectionString"]
                ):
                    yield response
        elif db == "postgres":
            available_postgres_client = self.database.find_single_entity_by_field_name(
                "configurations", "username", user
            )
            if available_postgres_client:
                async for response in self.query_database.query_database(
                    query, available_postgres_client["postgres"]["connectionString"]
                ):
                    yield response

        elif db == "sqlite":
            available_sqlite_client = self.database.find_single_entity_by_field_name(
                "configurations", "username", user
            )
            if available_sqlite_client:
                async for response in self.query_database.query_database(
                    query, available_sqlite_client["sqlite"]["connectionString"]
                ):
                    yield response

    def general_raw_query(self, user: str, query: str, db: str):
        if db == "mysql":
            available_mysql_client = self.database.find_single_entity_by_field_name(
                "configurations", "username", user
            )
            if available_mysql_client:
                return self.query_database.general_raw_query(
                    query, available_mysql_client["mysql"]["connectionString"]
                )
        elif db == "postgres":
            available_postgres_client = self.database.find_single_entity_by_field_name(
                "configurations", "username", user
            )
            if available_postgres_client:
                return self.query_database.general_raw_query(
                    query, available_postgres_client["postgres"]["connectionString"]
                )

        elif db == "sqlite":
            available_sqlite_client = self.database.find_single_entity_by_field_name(
                "configurations", "username", user
            )
            if available_sqlite_client:
                return self.query_database.general_raw_query(
                    query, available_sqlite_client["sqlite"]["connectionString"]
                )
        return {"error": "Some error occured."}
