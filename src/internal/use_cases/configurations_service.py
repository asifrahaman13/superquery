from typing import Any, Dict
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

    def update_project_configurations(
        self, user: str, db_type: str, field_value: Dict[str, Any]
    ) -> str:

        if db_type == "mysql":

            previous_configurations = (
                self.__database_repository.find_single_entity_by_field_name(
                    "configurations", "username", user
                )
            )

            if previous_configurations is None:
                return None

            previous_configurations["mysql"] = field_value

            updated_configurations = self.__database_repository.update_entity(
                "username",
                user,
                {"mysql": previous_configurations["mysql"]},
                "configurations",
            )
            return updated_configurations

        return None
