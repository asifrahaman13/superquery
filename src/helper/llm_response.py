import ollama


class LlmResponse:
    def __init__(self, anthropic_client, model: str) -> None:
        self.client = anthropic_client
        self.max_tokens = 5000
        self.model = model

    def embed_text(self, text: str, model_name: str) -> dict:
        response = ollama.embed(
            model=model_name,
            input=text,
        )
        return response.embeddings[0]

    async def bulk_llm_response(
        self,
        query: str,
        ddl_commands: list[str],
        examples: list[dict[str, str]],
        db_type: str,
    ) -> str:
        if db_type == "mysql":
            return await self._mysql_response(query, ddl_commands, examples)
        elif db_type == "postgres":
            return await self._postgres_response(query, ddl_commands, examples)
        elif db_type == "sqlite":
            return await self._sqlite_response(query, ddl_commands, examples)
        elif db_type == "pinecone":
            return await self._pinecone_response(query)
        elif db_type == "qdrant":
            return await self._qdrant_response(query)
        else:
            return "No response"

    async def _mysql_response(
        self, query: str, ddl_commands: list[str], examples: list[dict[str, str]]
    ) -> str:
        ddl_commands_str = "\n".join(ddl_commands)
        examples_str = "\n".join(
            [f"{i + 1}. {example['text']}\n" for i, example in enumerate(examples)]
        )

        system_message = f"""You are a master in mysql query. You are going to help me with generating mysql query from the natural language. I will provide you the natural language query and you will convert it into mysql query. Take care of all the details of the user query. Each small information of the user query matters. Depending upon that generate accurate sql query for mysql.\n
        We have three tables. They are created with the following SQL commands:\n
        {ddl_commands_str}\n
        Give me the SQL query corresponding to the user prompt. Example.\n
        {examples_str}\n
        Give only the sql command. Do not give any other text or information. Remember to take care of all the details of the user query. Each small information of the user query matters. Depending upon that generate accurate sql query for mysql.
        """

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

    async def _postgres_response(
        self, query: str, ddl_commands: list[str], examples: list[dict[str, str]]
    ) -> str:
        ddl_commands_str = "\n".join(ddl_commands)
        examples_str = "\n".join(
            [f"{i + 1}. {example['text']}\n" for i, example in enumerate(examples)]
        )

        system_message = f"""You are a master in postgres query. You are going to help me with generating postgres query from the natural language. I will provide you the natural language query and you will convert it into postgres query. Take care of all the details of the user query. Each small information of the user query matters. Depending upon that generate accurate sql query for postgres.\n
        We have three tables. They are created with the following SQL commands:\n
        {ddl_commands_str}\n
        Give me the SQL query corresponding to the user prompt. Example.\n
        {examples_str}\n
        Give only the sql command. Do not give any other text or information. Remember to take care of all the details of the user query. Each small information of the user query matters. Depending upon that generate accurate sql query for postgres.
        """

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

    async def _sqlite_response(
        self, query: str, ddl_commands: list[str], examples: list[dict[str, str]]
    ) -> str:
        ddl_commands_str = "\n".join(ddl_commands)
        examples_str = "\n".join(
            [f"{i + 1}. {example['text']}\n" for i, example in enumerate(examples)]
        )
        system_message = f"""You are a master in sqlite query. You are going to help me with generating sqlite query from the natural language. I will provide you the natural language query and you will convert it into sqlite query. Take care of all the details of the user query. Each small information of the user query matters. Depending upon that generate accurate sql query for sqlite.\n
        We have three tables. They are created with the following SQL commands:\n
        {ddl_commands_str}\n
        Give me the SQL query corresponding to the user prompt. Example of some of the correct user queries and the corresponding sql queries are: .\n
        {examples_str}\n
        Give only the sql command. Do not give any other text or information. Remember to take care of all the details of the user query. Each small information of the user query matters. Depending upon that generate accurate sql query for sqlite.
        """
        print(f"Using the model: {self.model}")
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

    async def _pinecone_response(self, query: str) -> str:
        completion = await self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            messages=[
                {
                    "role": "assistant",
                    "content": """You are a helpful assistant who is pro at pinecone vector semantic search. You have been asked to provide a response. You have the semantic search result from the source. You need to to check the result from the semantic search of the pinecone and give the result as per the query of the user in a natural language. The data source from which you need to answer is: \n
                   
                  """,
                },
                {"role": "user", "content": query},
            ],
        )

        response = completion.content[0].text
        return response

    async def _qdrant_response(self, query: str) -> str:
        completion = await self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            messages=[
                {
                    "role": "assistant",
                    "content": """You are a helpful assistant who is pro at qdrant vector semantic search. You have been asked to provide a response. You have the semantic search result from the source. You need to to check the result from the semantic search of the qdrant and give the result as per the query of the user in a natural language. The data source from which you need to answer is: \n
            
                  """,
                },
                {"role": "user", "content": query},
            ],
        )

        response = completion.content[0].text
        return response
