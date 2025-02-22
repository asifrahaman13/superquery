from abc import ABC, abstractmethod
from typing import Any, AsyncGenerator, Dict


class QueryInterface(ABC):
    @abstractmethod
    def query_db(
        self, user: str, query: str, db: str
    ) -> AsyncGenerator[Dict[str, Any], None]:
        pass

    @abstractmethod
    def general_raw_query(self, user: str, query: str, db: str) -> dict:
        pass
