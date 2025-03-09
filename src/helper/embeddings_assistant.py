import ollama


class EmbeddingService:
    @staticmethod
    def get_embeddings(
        text: str, embedding_model: str = "mxbai-embed-large"
    ) -> list[float]:
        response = ollama.embed(
            model=embedding_model,
            input=text,
        )
        return response.embeddings[0]
