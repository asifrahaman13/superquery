import logging
from typing import Dict, List
import openai
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from qdrant_client.http.models import (
    VectorParams,
    Distance,
    Filter,
    FieldCondition,
    MatchValue,
)

"""
Embedding service is used to create embeddings from the text using OpenAI API.
Currently we are using the open ai embeddings but any open sourced embedding models can also be used.
"""
from config.config import OPEN_AI_API_KEY, EMBEDDING_MODEL


class SemanticEmbeddingService:
    """
    Embedding service to get embeddings from the text using OpenAI API.
    """

    def __init__(self):

        self.__openai_client = openai.Client(api_key=OPEN_AI_API_KEY)
        self.__embedding_model = EMBEDDING_MODEL
        self.__embeddings_cache: Dict[str, List[float]] = {}

    def get_embeddings(self, text: str) -> List[float]:
        """
        Check if the embeddings are already cached.
        If already cached then we do not need to perform the embeddings again.
        We can directly reuse the data from  cache. Currently it's in-memory cache.
        """
        if text in self.__embeddings_cache:
            return self.__embeddings_cache[text]
        else:
            result = self.__openai_client.embeddings.create(
                input=[text], model=self.__embedding_model
            )
            self.__embeddings_cache[text] = result.data[0].embedding
            return self.__embeddings_cache[text]


class SemanticQdrantService:
    def __init__(self, url, api_key):
        self.__client = QdrantClient(url=url, api_key=api_key)

    def collection_exists(self, collection_name):
        try:
            response = self.__client.get_collection(collection_name)
            return response is not None
        except Exception as e:
            if "404" in str(e):
                return False
            else:
                raise e

    def create_collection(self, collection_name):

        if self.collection_exists:
            pass
        else:
            self.__client.create_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
            )

    def upsert_points(self, collection_name, points):
        self.__client.upsert(collection_name=collection_name, points=points)

    def search(self, query_embedding, id, limit=5):
        # filter_condition = Filter(
        #     must=[FieldCondition(key="id", match=MatchValue(value=id))]
        # )
        return self.__client.search(
            collection_name="superquery",
            query_vector=query_embedding,
            limit=limit,
            # query_filter=filter_condition,
        )


class SemanticSearchRepository:
    """
    Search repository is used to initialize the qdrant service and prepare the points.
    It also has the query_text method which is used to search the text.
    """

    def __init__(
        self,
        embedding_service: SemanticEmbeddingService,
        qdrant_service: SemanticQdrantService,
    ):
        self.__embedding_service = embedding_service
        self.__qdrant_service = qdrant_service

    """
    Prepare the points from the text and metadata. Metadata includes the front end configuration 
    data for the screens.
    """

    def prepare_points(
        self, texts: List[str], metadata: List[Dict]
    ) -> List[PointStruct]:
        import uuid

        return [
            PointStruct(
                id=str(uuid.uuid4()),
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

    def initialize_qdrant(self, texts: List[str], metadata: List[Dict]):
        points = self.prepare_points(texts, metadata)
        # self.__qdrant_service.create_collection("superquery")
        self.__qdrant_service.upsert_points("superquery", points)
        return True

    def query_text(self, query_text: str, id: str):
        try:
            # Get the embeddings for the query text.
            query_embedding = self.__embedding_service.get_embeddings(query_text)

            # Search the text using the embeddings.
            response = self.__qdrant_service.search(query_embedding, id)
            # print("########################################", response)

            logging.info(f"Query: {query_text}")
            result = []
            for data in response:
                if data.score > 0.5:
                    result.append(
                        {
                            "score": data.score,
                            "text": data.payload["text"],
                            "source": data.payload["source"],
                            "metadata": data.payload,
                        }
                    )
            return result
        except Exception as e:
            logging.error(f"Failed to search: {e}")
            return []
