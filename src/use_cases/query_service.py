import asyncio
import logging
from typing import Any, AsyncGenerator

from src.model.router_models import QueryResponse
from src.constants.databases.available_databases import DatabaseKeys

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class QueryService:
    def __init__(
        self, query_database, database, semantic_search_repository=None
    ) -> None:
        self.query_database = query_database
        self.database = database
        self.__db_keys = DatabaseKeys.get_keys()
        self.semantic_search_repository = semantic_search_repository

    async def query_db(
        self, user: str, messages: list[dict[str, str]], db: str
    ) -> AsyncGenerator[dict[str, Any], None]:
        db_key = self.__db_keys.get(db)
        if not db_key:
            return

        user_query = messages[-1]["content"]

        logging.info(
            f"Querying database with user: {user}, query: {user_query}, db: {db}"
        )

        available_client = await self.database.find_single_entity_by_field_name(
            "configurations", "username", user
        )
        await asyncio.sleep(0)
        yield QueryResponse(message="Thinking...", status=True)
        if available_client and db_key in available_client:
            configurations = available_client[db_key]
            examples = self.semantic_search_repository.query_text(user_query, user, db)

            logging.info(f"Querying database with configurations: {configurations}")
            configurations["examples"] = examples
            async for response in self.query_database.query_database(
                messages, **configurations
            ):
                await asyncio.sleep(0)
                yield response

    async def general_raw_query(self, user: str, query: str, db: str) -> Any:
        db_key = self.__db_keys.get(db)
        if not db_key:
            return None

        available_client = await self.database.find_single_entity_by_field_name(
            "configurations", "username", user
        )
        if available_client and db_key in available_client:
            connection_string = available_client[db_key]
            return self.query_database.general_raw_query(query, **connection_string)
        return None

    async def add_data_to_vector_db(
        self, user_query: str, sql_query: str, metadata: list[dict[str, Any]]
    ):
        data = [
            {
                "text": f"User prompt: {user_query}\n Sql query: {sql_query}",
            }
        ]
        texts = [d["text"] for d in data]
        return self.semantic_search_repository.initialize_qdrant(texts, metadata)
