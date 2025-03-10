import asyncio
import logging
from typing import Any, AsyncGenerator, Optional

from neo4j import GraphDatabase

from src.model.router_models import QueryResponse


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


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
        logging.info("Querying Neo4j:", query, parameters)
        with self.session.begin_transaction() as tx:
            result = tx.run(query, parameters)
            return result.data()


class Neo4jQueryRepo:
    def __init__(self, handle_answer_type, llm_response) -> None:
        self.handle_answer_type = handle_answer_type
        self.anthropic_client = llm_response

    async def query_database(
        self, user_query: str, *args, **kwargs
    ) -> AsyncGenerator[Optional[QueryResponse], None]:
        ddl_commands = kwargs.get("ddl_commands")
        examples = kwargs.get("examples")
        await asyncio.sleep(0)
        yield QueryResponse(message="Thinking of the answer", status=True)
        llm_generated_query = await self.anthropic_client.bulk_llm_response(
            user_query, ddl_commands, examples, "neo4j"
        )
        async for response in self.handle_answer_type.handle_neo4j_query(
            llm_generated_query, **kwargs
        ):
            await asyncio.sleep(0)
            yield response

    def general_raw_query(
        self, user_query: str, *args, **kwargs
    ) -> list[dict[str, Any]]:
        auth = (kwargs.get("username"), kwargs.get("neo4j_password"))
        connection_string = kwargs.get("api_endpoint")
        with Neo4jDriver(connection_string, auth) as driver:
            result = driver.query(user_query)
            return result
