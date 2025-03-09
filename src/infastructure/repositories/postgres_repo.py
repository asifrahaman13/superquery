import asyncio
from src.entities.router_models import QueryResponse
from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy import text


class PostgresQueryRepo:
    def __init__(self, handle_answer_type, llm_response) -> None:
        self.handle_answer_type = handle_answer_type
        self.anthropic_client = llm_response

    async def query_database(self, user_query: str, *args, **kwargs):
        connection_string: str = kwargs.get("connectionString")
        ddl_commands = kwargs.get("ddlCommands")
        examples = kwargs.get("examples")
        await asyncio.sleep(0)
        yield QueryResponse(message="Thinking of the answer", status=True)
        llm_generated_query = await self.anthropic_client.bulk_llm_response(
            user_query, ddl_commands, examples, "postgres"
        )
        async for response in self.handle_answer_type.handle_postgres_query(
            llm_generated_query, connection_string
        ):
            await asyncio.sleep(0)
            yield response

    def general_raw_query(self, query: str, *args, **kwargs):
        connection_string: str = kwargs.get("connectionString")
        engine = create_engine(connection_string)
        SQLModel.metadata.create_all(engine)
        with Session(engine) as session:
            result = session.exec(text(query))
            columns = result.keys()
            response = [dict(zip(columns, row)) for row in result.fetchall()]
            session.close()
            return response
