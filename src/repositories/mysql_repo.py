import asyncio
from typing import Any, AsyncGenerator, Optional

from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy import text

from src.model.router_models import QueryResponse


class MySqlQueryRepo:
    def __init__(self, handle_answer_type, llm_response) -> None:
        self.handle_answer_type = handle_answer_type
        self.anthropic_client = llm_response

    async def query_database(
        self, user_query: str, *args, **kwargs
    ) -> AsyncGenerator[Optional[QueryResponse], None]:
        connection_string: str = kwargs.get("connection_string")
        ddl_commands = kwargs.get("ddl_commands")
        examples = kwargs.get("examples")
        await asyncio.sleep(0)
        yield QueryResponse(message="Thinking of the answer", status=True)
        await asyncio.sleep(0)

        llm_generated_query = await self.anthropic_client.bulk_llm_response(
            user_query, ddl_commands, examples, "mysql"
        )
        async for response in self.handle_answer_type.handle_mysql_query(
            llm_generated_query, connection_string
        ):
            yield response

    def general_raw_query(self, query: str, *args, **kwargs) -> list[dict[str, Any]]:
        connection_string: str = kwargs.get("connection_string")
        engine = create_engine(connection_string)
        SQLModel.metadata.create_all(engine)
        with Session(engine) as session:
            result = session.exec(text(query))
            columns = result.keys()
            response = [dict(zip(columns, row)) for row in result.fetchall()]
            session.close()
            return response
