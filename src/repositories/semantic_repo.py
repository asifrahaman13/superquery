import logging
from collections import OrderedDict

import uuid
from qdrant_client import QdrantClient, models
from qdrant_client.models import PointStruct, Filter, FieldCondition, MatchValue
from qdrant_client.http.models import VectorParams, Distance
import ollama

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class SemanticEmbeddingService:
    def __init__(self, cache_size: int = 1000) -> None:
        self.embeddings_cache: OrderedDict[str, list[float]] = OrderedDict()
        self.cache_size = cache_size

    def get_embeddings(
        self, text: str, embeddin_model: str = "mxbai-embed-large"
    ) -> list[float]:
        if text in self.embeddings_cache:
            self.embeddings_cache.move_to_end(text)
            return self.embeddings_cache[text]
        else:
            response = ollama.embed(model=embeddin_model, input=text)
            self.embeddings_cache[text] = response.embeddings[0]
            logging.info(f"Embedding for {text} is done")
            if len(self.embeddings_cache) > self.cache_size:
                self.embeddings_cache.popitem(last=False)

            return self.embeddings_cache[text]


class SemanticQdrantService:
    def __init__(self, url: str, api_key: str) -> None:
        self.client = QdrantClient(url=url, api_key=api_key)

    def collection_exists(self, collection_name: str) -> bool:
        try:
            response = self.client.get_collection(collection_name)
            return response is not None
        except Exception:
            return False

    def create_collection(self, collection_name: str) -> None:
        if self.collection_exists:
            pass
        else:
            self.client.create_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(size=1024, distance=Distance.COSINE),
            )

    def upsert_points(self, collection_name: str, points: list[PointStruct]) -> None:
        self.client.upsert(collection_name=collection_name, points=points)

    def search(
        self, query_embedding: list[float], user: str, database: str, limit: int = 5
    ) -> list[PointStruct]:
        filter_condition = Filter(
            must=[
                FieldCondition(key="user", match=MatchValue(value=user)),
                FieldCondition(key="database", match=MatchValue(value=database)),
            ]
        )
        return self.client.search(
            collection_name="superquery",
            query_vector=query_embedding,
            limit=limit,
            query_filter=filter_condition,
        )


class SemanticSearchRepo:
    def __init__(
        self,
        embedding_service: SemanticEmbeddingService,
        qdrant_service: SemanticQdrantService,
    ):
        self.embedding_service = embedding_service
        self.qdrant_service = qdrant_service

    def prepare_points(
        self, texts: list[str], metadata: list[dict]
    ) -> list[PointStruct]:
        return [
            PointStruct(
                id=str(uuid.uuid4()),
                vector=self.embedding_service.get_embeddings(text),
                payload={"text": text, **meta},
            )
            for _, (text, meta) in enumerate(zip(texts, metadata))
        ]

    async def create_collection(
        self, collection_name: str, embedding_dim: int = 1024
    ) -> None:
        collection_exists = self.qdrant_service.client.collection_exists(
            collection_name=collection_name
        )
        if collection_exists is False:
            self.qdrant_service.client.create_collection(
                collection_name,
                vectors_config=models.VectorParams(
                    size=embedding_dim, distance=models.Distance.COSINE
                ),
            )

    def initialize_qdrant(
        self, texts: list[str], metadata: list[dict[str, str]]
    ) -> bool:
        points = self.prepare_points(texts, metadata)
        result = self.qdrant_service.upsert_points("superquery", points)
        print(result)
        return True

    def query_text(
        self, query_text: str, user: str, database: str, threshold: float = 0.5
    ) -> list[dict]:
        try:
            query_embedding = self.embedding_service.get_embeddings(query_text)
            response = self.qdrant_service.search(query_embedding, user, database)
            logging.info(f"Query: {query_text}")
            result = []

            logging.info(f"Response: {response}")
            for data in response:
                if data.score > threshold:
                    result.append(
                        {
                            "score": data.score,
                            "text": data.payload["text"],
                            "metadata": data.payload,
                        }
                    )
            return result
        except Exception as e:
            logging.error(f"Failed to search: {e}")
            return []
