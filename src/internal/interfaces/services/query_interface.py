from abc import  ABC, abstractmethod

class QueryInterface(ABC):
    @abstractmethod
    def query_db(self, query: str) -> dict:
        pass