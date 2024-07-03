from src.internal.interfaces.services.configuration_interface import (
    ConfigurationInterface,
)


class ConfigurationService(ConfigurationInterface):
    def __init__(self, database_repository):
        self.__database_repository = database_repository

    def get_project_configurations(self, user: str, db_type: str) -> str:
        configurations = self.__database_repository.find_single_entity_by_field_name(
            "configurations", "username", user
        )

        if db_type == "mysql":
            return configurations["mysql"]
        return None
