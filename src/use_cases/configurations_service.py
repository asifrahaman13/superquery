from typing import Any

from src.constants.databases.available_databases import DatabaseKeys

from ..repositories.ddl_repo import DDLRepo


class ConfigurationService:
    def __init__(self, database_repo, ddl_repo):
        self.database_repo = database_repo
        self.ddl_repo = ddl_repo
        self.__db_keys = DatabaseKeys.get_keys()

    async def get_project_configurations(self, user: str, db_type: str) -> str:
        configurations = await self.database_repo.find_single_entity_by_field_name(
            "configurations", "username", user
        )
        return configurations.get(self.__db_keys.get(db_type))

    async def update_project_configurations(
        self, user: str, db_type: str, field_value: dict[str, Any]
    ) -> str:
        db_key = self.__db_keys.get(db_type)
        if not db_key:
            return None
        previous_configurations = (
            await self.database_repo.find_single_entity_by_field_name(
                "configurations", "username", user
            )
        )
        if previous_configurations is None:
            return None
        ddl_commands = DDLRepo.get_ddl_commands(
            db_type, field_value["connection_string"]
        )

        if not ddl_commands:
            return None
        previous_configurations[db_key] = field_value
        previous_configurations[db_key]["ddl_commands"] = ddl_commands
        updated_configurations = await self.database_repo.update_entity(
            "username",
            user,
            {db_key: previous_configurations[db_key]},
            "configurations",
        )
        return updated_configurations
