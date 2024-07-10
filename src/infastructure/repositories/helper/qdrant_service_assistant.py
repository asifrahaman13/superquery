from qdrant_client import QdrantClient
from qdrant_client.http.models import (
    Filter,
    FieldCondition,
    MatchValue,
)
from openai import Client


class QdrantService:
    @staticmethod
    def collection_exists(client: Client, collection_name: str) -> bool:
        try:
            response = client.get_collection(collection_name)
            return response is not None
        except Exception as e:
            if "404" in str(e):
                return False
            else:
                raise e

    @staticmethod
    def search(
        query_embedding, collection_name, api_endpoint=None, qdrant_api_key=None
    ):
        client = QdrantClient(url=api_endpoint, api_key=qdrant_api_key)
        # filter_condition = Filter(
        #     must=[FieldCondition(key="qrId", match=MatchValue(value=qr_id))]
        # )
        return client.search(
            collection_name=collection_name,
            query_vector=query_embedding,
            limit=5,
            # query_filter=filter_condition,
        )
