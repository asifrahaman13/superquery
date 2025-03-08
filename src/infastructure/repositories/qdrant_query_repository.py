import asyncio
import logging
from typing import Dict, List
from qdrant_client.models import PointStruct
from src.infastructure.repositories.helper.llm_response import LlmResponse
from src.internal.entities.router_models import QueryResponse
from src.infastructure.repositories.helper.embeddings_assistant import EmbeddingService
from src.infastructure.repositories.helper.qdrant_service_assistant import QdrantService
from openai import Client


class QdrantQueryRepository:
    def __init__(
        self,
        embedding_service: EmbeddingService,
        qdrant_service: QdrantService,
    ):
        self.embedding_service = embedding_service
        self.qdrant_service = qdrant_service

    def prepare_points(
        self, texts: List[str], metadata: List[Dict]
    ) -> List[PointStruct]:
        return [
            PointStruct(
                id=idx,
                vector=self.embedding_service.get_embeddings(text),
                payload={"text": text, **meta},
            )
            for idx, (text, meta) in enumerate(zip(texts, metadata))
        ]

    async def query_database(
        self,
        query_text: str,
        *args,
        **kwargs,
    ):
        collection_name = kwargs.get("collection_name")
        embedding_model_name = kwargs.get("embedding_model_name")
        anthropic_api_key = kwargs.get("anthropic_api_key")
        qdrant_api_key = kwargs.get("qdrant_api_key")
        api_endpoint = kwargs.get("api_endpoint")
        try:
            await asyncio.sleep(0)
            yield QueryResponse(
                message="Querying Qdrant", status=True, answer_type="plain_answer"
            )
            await asyncio.sleep(0)
            query_embedding = self.embedding_service.get_embeddings(
                query_text,
                api_key=anthropic_api_key,
                embedding_model=embedding_model_name,
            )

            response = self.qdrant_service.search(
                query_embedding,
                collection_name,
                api_endpoint=api_endpoint,
                qdrant_api_key=qdrant_api_key,
            )
            logging.info(f"qdrant service response: {response}")
            anthropic_client = LlmResponse(Client(api_key=anthropic_api_key))
            llm_response = anthropic_client.bulk_llm_response(
                query_text, response, "qdrant"
            )
            await asyncio.sleep(0)
            yield QueryResponse(
                message=llm_response, status=False, answer_type="plain_answer"
            )
            await asyncio.sleep(0)
        except Exception as e:
            logging.error(f"Failed to search: {e}")
            yield QueryResponse(
                message="Failed to search", status=False, answer_type="plain_answer"
            )

    def general_raw_query(self, query_text: str, *args, **kwargs):
        collection_name = kwargs.get("collection_name")
        embedding_model_name = kwargs.get("embedding_model_name")
        anthropic_api_key = kwargs.get("anthropic_api_key")
        qdrant_api_key = kwargs.get("qdrant_api_key")
        api_endpoint = kwargs.get("api_endpoint")
        try:
            query_embedding = self.embedding_service.get_embeddings(
                query_text,
                api_key=anthropic_api_key,
                embedding_model=embedding_model_name,
            )
            response = self.qdrant_service.search(
                query_embedding,
                collection_name,
                api_endpoint=api_endpoint,
                qdrant_api_key=qdrant_api_key,
            )
            logging.info(f"qdrant service response: {response}")
            return response

        except Exception as e:
            logging.error(f"Failed to search: {e}")
            return {"error": "Some error occured. sorry"}
