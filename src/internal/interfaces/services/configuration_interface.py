from abc import ABC, abstractmethod


class ConfigurationInterface(ABC):
    @abstractmethod
    def get_project_configurations(self, user: str, db_type: str) -> str:
        pass
