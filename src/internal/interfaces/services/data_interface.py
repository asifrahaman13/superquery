from abc import ABC, abstractmethod


class DataInterface(ABC):
    @abstractmethod
    def query_sql(self, query: str) -> str:
        pass
