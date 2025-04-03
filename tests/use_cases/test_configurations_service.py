# import pytest
# from unittest.mock import AsyncMock, MagicMock
# from src.use_cases.configurations_service import ConfigurationService
# from src.constants.databases.available_databases import DatabaseKeys
# from src.model.products import Databases


# @pytest.mark.asyncio
# async def test_get_project_configurations():
#     # Arrange
#     mock_database_repo = AsyncMock()
#     mock_ddl_repo = MagicMock()
#     service = ConfigurationService(mock_database_repo, mock_ddl_repo)

#     user = "test_user"
#     db_type = "postgres"
#     db_key = DatabaseKeys.get_keys().get(db_type)
#     mock_database_repo.find_single_entity_by_field_name.return_value = {
#         db_key: "test_configuration"
#     }

#     # Act
#     result = await service.get_project_configurations(user, db_type)

#     # Assert
#     assert result == "test_configuration"
#     mock_database_repo.find_single_entity_by_field_name.assert_awaited_once_with(
#         "configurations", "username", user
#     )


# @pytest.mark.asyncio
# async def test_update_project_configurations_success():
#     # Arrange
#     mock_database_repo = AsyncMock()
#     mock_ddl_repo = MagicMock()
#     service = ConfigurationService(mock_database_repo, mock_ddl_repo)

#     user = "asifrahaman162@gmail.com"
#     db_type = "postgres"
#     db_key = DatabaseKeys.get_keys().get(db_type)
#     field_value = {"connection_string": "postgresql://postgres:password@localhost:5432/mydata"}
#     previous_configurations = {db_key: {}}

#     mock_database_repo.find_single_entity_by_field_name.return_value = previous_configurations
#     mock_database_repo.update_entity.return_value = "updated_configuration"
#     mock_ddl_repo.get_ddl_commands.return_value = ["CREATE TABLE test;"]

#     # Act
#     result = await service.update_project_configurations(user, db_type, field_value)

#     # Assert
#     assert result == "updated_configuration"
#     mock_database_repo.find_single_entity_by_field_name.assert_awaited_once_with(
#         "configurations", "username", user
#     )
#     mock_database_repo.update_entity.assert_awaited_once_with(
#         "username",
#         user,
#         {db_key: {"connection_string": field_value["connection_string"], "ddl_commands": ["CREATE TABLE test;"]}},
#         "configurations",
#     )


# @pytest.mark.asyncio
# async def test_update_project_configurations_no_db_key():
#     # Arrange
#     mock_database_repo = AsyncMock()
#     mock_ddl_repo = MagicMock()
#     service = ConfigurationService(mock_database_repo, mock_ddl_repo)

#     user = "test_user"
#     db_type = "unknown_db"
#     field_value = {"connection_string": "test_connection_string"}

#     # Act
#     result = await service.update_project_configurations(user, db_type, field_value)

#     # Assert
#     assert result is None
#     mock_database_repo.find_single_entity_by_field_name.assert_not_awaited()
#     mock_database_repo.update_entity.assert_not_awaited()


# @pytest.mark.asyncio
# async def test_update_project_configurations_no_previous_configurations():
#     # Arrange
#     mock_database_repo = AsyncMock()
#     mock_ddl_repo = MagicMock()
#     service = ConfigurationService(mock_database_repo, mock_ddl_repo)

#     user = "test_user"
#     db_type = "postgres"
#     field_value = {"connection_string": "test_connection_string"}

#     mock_database_repo.find_single_entity_by_field_name.return_value = None

#     # Act
#     result = await service.update_project_configurations(user, db_type, field_value)

#     # Assert
#     assert result is None
#     mock_database_repo.find_single_entity_by_field_name.assert_awaited_once_with(
#         "configurations", "username", user
#     )
#     mock_database_repo.update_entity.assert_not_awaited()


# @pytest.mark.asyncio
# async def test_update_project_configurations_no_ddl_commands():
#     # Arrange
#     mock_database_repo = AsyncMock()
#     mock_ddl_repo = MagicMock()
#     service = ConfigurationService(mock_database_repo, mock_ddl_repo)

#     user = "asifrahaman162@gmail.com"
#     db_type = "postgres"
#     db_key = DatabaseKeys.get_keys().get(db_type)
#     field_value = {"connection_string": "postgresql://postgres:password@localhost:5432/mydata"}
#     previous_configurations = {db_key: {}}

#     mock_database_repo.find_single_entity_by_field_name.return_value = previous_configurations
#     mock_ddl_repo.get_ddl_commands.return_value = None

#     # Act
#     result = await service.update_project_configurations(user, db_type, field_value)

#     print("======================================")
#     print(result)

#     # Assert
#     assert result is None
#     mock_database_repo.find_single_entity_by_field_name.assert_awaited_once_with(
#         "configurations", "username", user
#     )
#     mock_database_repo.update_entity.assert_not_awaited()