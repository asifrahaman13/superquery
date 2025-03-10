from typing import Awaitable

import instructor

from src.constants.prompts.prompts import PromptTemplates
from src.helper import Utils
from src.model import AIResponse, Databases


class LlmResponse:
    def __init__(self, anthropic_client, model: str) -> None:
        self.client = instructor.from_anthropic(anthropic_client)
        self.max_tokens = 5000
        self.model = model

    async def bulk_llm_response(
        self,
        query: str,
        ddl_commands: list[str],
        examples: list[dict[str, str]],
        db_type: str,
    ) -> Awaitable[str]:
        if db_type == Databases.MYSQL.value:
            return await self._generate_response(
                query, ddl_commands, examples, PromptTemplates.MYSQL
            )
        elif db_type == Databases.POSTGRES.value:
            return await self._generate_response(
                query, ddl_commands, examples, PromptTemplates.POSTGRES
            )
        elif db_type == Databases.SQLITE.value:
            return await self._generate_response(
                query, ddl_commands, examples, PromptTemplates.SQLITE
            )
        elif db_type == Databases.NEO4J.value:
            return await self._generate_response(
                query, ddl_commands, examples, PromptTemplates.NEO4J
            )
        else:
            return "No response"

    async def _generate_response(
        self,
        query: str,
        ddl_commands: list[str],
        examples: list[dict[str, str]],
        template: str,
    ) -> Awaitable[str]:
        ddl_commands_str, examples_str = Utils.format_ddl_and_examples(
            ddl_commands, examples
        )
        system_message = template.format(
            ddl_commands_str=ddl_commands_str, examples_str=examples_str
        )

        completion = await self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            messages=[
                {
                    "role": "assistant",
                    "content": system_message,
                },
                {"role": "user", "content": query},
            ],
            response_model=AIResponse,
        )

        assert isinstance(completion, AIResponse)
        raw_response = completion.raw_response

        sql_query = None
        if completion.sql_query is not None:
            sql_query = completion.sql_query.strip("```sql\n").strip("```")
        return (raw_response, sql_query)
