from typing import List
from openai import Client

"""
Embedding service is used to create embeddings from the text using OpenAI API.
Currently we are using the open ai embeddings but any open sourced embedding models can also be used.
"""


class EmbeddingService:
    """
    Embedding service to get embeddings from the text using OpenAI API.
    """

    @staticmethod
    def get_embeddings(text: str, api_key: str, embedding_model: str) -> List[float]:
        """
        Check if the embeddings are already cached.
        If already cached then we do not need to perform the embeddings again.
        We can directly reuse the data from  cache. Currently it's in-memory cache.
        """

        openai_client = Client(api_key=api_key)

        result = openai_client.embeddings.create(input=[text], model=embedding_model)
        return result.data[0].embedding
