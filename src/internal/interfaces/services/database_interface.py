from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class DatabaseInterface(ABC):

    @abstractmethod
    def find_one(
        self, field: str, field_value: str, collection_name: str
    ) -> Optional[Dict[str, Any]]:
        """Find a single document in the specified collection where the field matches the field_value."""
        pass

    @abstractmethod
    def insert_one(self, data: Dict[str, Any], collection_name: str) -> Any:
        """Insert a single document into the specified collection."""
        pass

    @abstractmethod
    def find_all(self, collection_name: str) -> List[Dict[str, Any]]:
        """Find all documents in the specified collection."""
        pass

    @abstractmethod
    def find_all_documents_from_field(
        self, field: str, field_value: str, collection_name: str
    ) -> List[Dict[str, Any]]:
        """Find all documents in the specified collection where the field matches the field_value."""
        pass
