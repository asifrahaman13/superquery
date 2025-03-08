from typing import List
import ollama


class EmbeddingService:
    @staticmethod
    def get_embeddings(
        text: str, api_key: str, embedding_model: str = "mxbai-embed-large"
    ) -> List[float]:
        response = ollama.embed(
            model=embedding_model,
            input=text,
        )
        return response.embeddings
