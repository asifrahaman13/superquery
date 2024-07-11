from typing import Any, AsyncGenerator, Dict
from src.internal.interfaces.services.query_interface import QueryInterface
from src.constants.databases.available_databases import DatabaseKeys


class QueryService(QueryInterface):

    def __init__(self, query_database, database) -> None:
        self.query_database = query_database
        self.database = database
        self.__db_keys = DatabaseKeys.get_keys()

    async def query_db(
        self, user: str, query: str, db: str
    ) -> AsyncGenerator[Dict[str, Any], None]:
        db_key = self.__db_keys.get(db)
        if not db_key:
            return

        available_client = self.database.find_single_entity_by_field_name(
            "configurations", "username", user
        )
        if available_client and db_key in available_client:
            connection_string = available_client[db_key]
            async for response in self.query_database.query_database(
                query, **connection_string
            ):
                yield response
                yield response

    def general_raw_query(self, user: str, query: str, db: str):
        db_key = self.__db_keys.get(db)
        if not db_key:
            return None

        available_client = self.database.find_single_entity_by_field_name(
            "configurations", "username", user
        )
        if available_client and db_key in available_client:
            connection_string = available_client[db_key]
            print(
                "normal client...........................................",
                connection_string,
            )
            # print("** client...........................................", **connection_string)

            return self.query_database.general_raw_query(query, **connection_string)
        return None
