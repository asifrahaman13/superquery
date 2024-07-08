class LlmResponse:
    def __init__(self, open_ai_client) -> None:
        self.client = open_ai_client

    def embed_text(self, text, model_name):
        response = self.client.embeddings.create(model=model_name, input=text)
        return response.data[0].embedding

    def bulk_llm_response(self, query, data_source: str, db_type: str):

        if db_type == "pinecone":
            completion = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": f"""You are a helpful assistant who is pro at pinecone vector semantic search. You have been asked to provide a response. You have the semantic search result from the source. You need to to check the result from the semantic search of the pinecone and give the result as per the query of the user in a natural language. The data source from which you need to answer is: \n
                       {str(data_source)}
                      """,
                    },
                    {"role": "user", "content": query},
                ],
            )
            return completion.choices[0].message.content
        else:
            return "No response"
