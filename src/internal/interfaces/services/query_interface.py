from abc import ABC, abstractmethod


class QueryInterface(ABC):
    @abstractmethod
    def query_db(self, user: str, query: str, db: str) -> dict:
        pass
