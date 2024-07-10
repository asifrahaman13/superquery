import asyncio
import logging
from typing import Dict, List
from qdrant_client.models import PointStruct
from src.internal.entities.router_models import QueryResponse
from src.infastructure.repositories.helper.embeddings_assistant import EmbeddingService
from src.infastructure.repositories.helper.qdrant_service_assistant import QdrantService
from openai import Client


class QdrantQueryRepository:
    """
    Search repository is used to initialize the qdrant service and prepare the points.
    It also has the query_text method which is used to search the text.
    """

    def __init__(
        self,
        embedding_service: EmbeddingService,
        qdrant_service: QdrantService,
        open_ai_client: Client,
    ):
        self.__embedding_service = embedding_service
        self.__qdrant_service = qdrant_service
        self.__open_ai_client = open_ai_client

    """
    Prepare the points from the text and metadata. Metadata includes the front end configuration 
    data for the screens.
    """

    def prepare_points(
        self, texts: List[str], metadata: List[Dict]
    ) -> List[PointStruct]:
        return [
            PointStruct(
                id=idx,
                vector=self.__embedding_service.get_embeddings(text),
                payload={"text": text, **meta},
            )
            for idx, (text, meta) in enumerate(zip(texts, metadata))
        ]

    """
    This function will be called before the start of the FastAPI application server.
    The function initializes the data points, creates the collection, and upserts the static data points.
    They will be later used as cached data for the vector search.
    """

    async def query_database(
        self,
        query_text: str,
        *args,
        **kwargs,
    ):
        collection_name = kwargs.get("collection_name")
        embedding_model_name = kwargs.get("embedding_model_name")
        open_ai_api_key = kwargs.get("open_ai_api_key")
        qdrant_api_key = kwargs.get("qdrant_api_key")
        api_endpoint = kwargs.get("api_endpoint")
        try:
            await asyncio.sleep(0)
            yield QueryResponse(
                message="Querying Qdrant", status=True, answer_type="plain_answer"
            )
            await asyncio.sleep(0)
            # Get the embeddings for the query text.
            query_embedding = self.__embedding_service.get_embeddings(
                query_text,
                api_key=open_ai_api_key,
                embedding_model=embedding_model_name,
            )

            # Search the text using the embeddings.
            response = self.__qdrant_service.search(
                query_embedding,
                collection_name,
                api_endpoint=api_endpoint,
                qdrant_api_key=qdrant_api_key,
            )

            logging.info(f"qdrant service response: {response}")

            llm_response = self.__open_ai_client.bulk_llm_response(
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
        open_ai_api_key = kwargs.get("open_ai_api_key")
        qdrant_api_key = kwargs.get("qdrant_api_key")
        api_endpoint = kwargs.get("api_endpoint")
        try:

            # Get the embeddings for the query text.
            query_embedding = self.__embedding_service.get_embeddings(
                query_text,
                api_key=open_ai_api_key,
                embedding_model=embedding_model_name,
            )

            # Search the text using the embeddings.
            response = self.__qdrant_service.search(
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
