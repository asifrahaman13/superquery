from abc import ABC, abstractmethod
from typing import Any, Dict


class ConfigurationInterface(ABC):
    @abstractmethod
    def get_project_configurations(self, user: str, db_type: str) -> str:
        pass

    @abstractmethod
    def update_project_configurations(
        self, user: str, db_type: str, field_value: Dict[str, Any]
    ) -> str:
        pass
