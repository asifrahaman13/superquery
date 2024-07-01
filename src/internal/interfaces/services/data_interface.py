from abc import ABC, abstractmethod
from typing import Dict


class DataInterface(ABC):

    @abstractmethod
    def query_sql(self, query: str) -> str:
        pass
