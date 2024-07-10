import asyncio
from pinecone import Pinecone
from src.internal.entities.router_models import QueryResponse


class PineconeQueryRepository:
    def __init__(self, open_ai_client) -> None:
        self.open_ai_client = open_ai_client

    async def query_database(
        self,
        query: str,
        *args,
        **kwargs,
    ):
        index_name = kwargs.get("index_name")
        model_name = kwargs.get("model_name")
        pinecone_api_key = kwargs.get("pinecone_api_key")

        # Initialize Pinecone
        pinecone = Pinecone(api_key=pinecone_api_key)
        index = pinecone.Index(index_name)

        await asyncio.sleep(0)
        yield QueryResponse(
            message="Querying Pinecone", status=True, answer_type="plain_answer"
        )
        await asyncio.sleep(0)

        # Perform a semantic search
        query_embedding = self.open_ai_client.embed_text(query, model_name)

        # Query the index with the new data
        result = index.query(
            vector=query_embedding,
            top_k=3,
            include_metadata=True,
        )

        data_source = result.to_dict() if hasattr(result, "to_dict") else result

        await asyncio.sleep(0)
        yield QueryResponse(
            message="Framing answer", status=True, answer_type="plain_answer"
        )
        await asyncio.sleep(0)

        response = self.open_ai_client.bulk_llm_response(query, data_source, "pinecone")

        await asyncio.sleep(0)
        yield QueryResponse(message=response, status=False, answer_type="plain_answer")
        await asyncio.sleep(0)

    def general_raw_query(self, query: str, *args, **kwargs):

        index_name = kwargs.get("index_name")
        model_name = kwargs.get("model_name")
        pinecone_api_key = kwargs.get("pinecone_api_key")

        # Initialize Pinecone
        pinecone = Pinecone(api_key=pinecone_api_key)
        index = pinecone.Index(index_name)

        # Perform a semantic search
        query_embedding = self.open_ai_client.embed_text(query, model_name)

        # Query the index with the new data
        result = index.query(
            vector=query_embedding,
            top_k=3,
            include_metadata=True,
        )

        data_source = result.to_dict() if hasattr(result, "to_dict") else result

        return data_source
