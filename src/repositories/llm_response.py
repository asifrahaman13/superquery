from typing import Awaitable
from src.constants.prompts.prompts import PromptTemplates
from src.helper import Utils


class LlmResponse:
    def __init__(self, anthropic_client, model: str) -> None:
        self.client = anthropic_client
        self.max_tokens = 5000
        self.model = model

    async def bulk_llm_response(
        self,
        query: str,
        ddl_commands: list[str],
        examples: list[dict[str, str]],
        db_type: str,
    ) -> Awaitable[str]:
        if db_type == "mysql":
            return await self._generate_response(
                query, ddl_commands, examples, PromptTemplates.MYSQL
            )
        elif db_type == "postgres":
            return await self._generate_response(
                query, ddl_commands, examples, PromptTemplates.POSTGRES
            )
        elif db_type == "sqlite":
            return await self._generate_response(
                query, ddl_commands, examples, PromptTemplates.SQLITE
            )
        elif db_type == "neo4j":
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
        )
        response = completion.content[0].text.strip("```sql\n").strip("```")
        return response
