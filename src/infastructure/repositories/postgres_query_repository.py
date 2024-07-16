import asyncio
from src.internal.entities.router_models import QueryResponse
from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy import text
from src.infastructure.repositories.helper.format_assistant import FormatAssistant


class PostgresQueryRepository:
    def __init__(self, handle_answer_type, llm_response) -> None:
        self.handle_answer_type = handle_answer_type
        self.open_ai_client = llm_response

    async def query_database(self, user_query: str, *args, **kwargs):
        connection_string: str = kwargs.get("connectionString")
        ddl_commands = kwargs.get("ddlCommands")
        examples = kwargs.get("examples")
        await asyncio.sleep(0)
        yield QueryResponse(message="Thinking of the answer", status=True)
        await asyncio.sleep(0)

        answer_type = FormatAssistant().run_answer_type_assistant(user_query)

        if answer_type["answer_type"] == "plain_answer":
            llm_generated_query = self.open_ai_client.bulk_llm_response(
                user_query, ddl_commands, examples, "postgres"
            )
            async for response in self.handle_answer_type.handle_plain_answer(
                llm_generated_query, connection_string
            ):
                yield response

        elif answer_type["answer_type"] == "bar_chart":
            async for response in self.handle_answer_type.handle_bar_chart(
                user_query, connection_string
            ):
                yield response

        elif answer_type["answer_type"] == "line_chart":
            async for response in self.handle_answer_type.handle_line_chart(
                user_query, connection_string
            ):
                yield response

        elif answer_type["answer_type"] == "pie_chart":
            async for response in self.handle_answer_type.handle_pie_chart(
                user_query, connection_string
            ):
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
