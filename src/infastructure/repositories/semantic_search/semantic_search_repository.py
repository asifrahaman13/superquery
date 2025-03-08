import logging
from typing import Dict, List
from qdrant_client import QdrantClient

# from qdrant_client.models import PointStruct, VectorParams, Distance
from qdrant_client.models import PointStruct
from qdrant_client.http.models import (
    VectorParams,
    Distance,
)
import ollama


class SemanticEmbeddingService:
    def __init__(self):
        self.embeddings_cache: Dict[str, List[float]] = {}

    def get_embeddings(self, text: str) -> List[float]:
        if text in self.embeddings_cache:
            return self.embeddings_cache[text]
        else:
            response = ollama.embed(model="mxbai-embed-large", input=text)
            self.embeddings_cache[text] = response["embedding"]
            return self.embeddings_cache[text]


class SemanticQdrantService:
    def __init__(self, url, api_key):
        self.client = QdrantClient(url=url, api_key=api_key)

    def collection_exists(self, collection_name):
        try:
            response = self.client.get_collection(collection_name)
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
            self.client.create_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
            )

    def upsert_points(self, collection_name, points):
        self.client.upsert(collection_name=collection_name, points=points)

    def search(self, query_embedding, id, limit=5):
        # filter_condition = Filter(
        #     must=[FieldCondition(key="id", match=MatchValue(value=id))]
        # )
        return self.client.search(
            collection_name="superquery",
            query_vector=query_embedding,
            limit=limit,
            # query_filter=filter_condition,
        )


class SemanticSearchRepository:
    def __init__(
        self,
        embedding_service: SemanticEmbeddingService,
        qdrant_service: SemanticQdrantService,
    ):
        self.embedding_service = embedding_service
        self.qdrant_service = qdrant_service

    def prepare_points(
        self, texts: List[str], metadata: List[Dict]
    ) -> List[PointStruct]:
        import uuid

        return [
            PointStruct(
                id=str(uuid.uuid4()),
                vector=self.embedding_service.get_embeddings(text),
                payload={"text": text, **meta},
            )
            for idx, (text, meta) in enumerate(zip(texts, metadata))
        ]

    def initialize_qdrant(self, texts: List[str], metadata: List[Dict]):
        points = self.prepare_points(texts, metadata)
        # self.qdrant_service.create_collection("superquery")
        self.qdrant_service.upsert_points("superquery", points)
        return True

    def query_text(self, query_text: str, id: str):
        try:
            query_embedding = self.embedding_service.get_embeddings(query_text)
            response = self.qdrant_service.search(query_embedding, id)
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
