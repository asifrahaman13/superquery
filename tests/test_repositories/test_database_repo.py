import pytest
from unittest.mock import AsyncMock, MagicMock
from src.repositories.database_repo import MongodbRepo


@pytest.fixture
def mongodb_repo():
    mock_collection = AsyncMock()
    mock_database = MagicMock()
    mock_database.__getitem__.return_value = mock_collection
    mock_client = MagicMock()
    mock_client.__getitem__.return_value = mock_database
    repo = MongodbRepo(mock_client, "test_database")
    repo._mock_collection = mock_collection
    return repo


@pytest.mark.asyncio
async def test_find_single_entity_by_field_name(mongodb_repo):
    mock_collection = mongodb_repo._mock_collection
    mock_collection.find_one.return_value = {"_id": "123", "name": "test"}
    result = await mongodb_repo.find_single_entity_by_field_name(
        "test_collection", "name", "test"
    )
    assert result == {"_id": "123", "name": "test"}
    mock_collection.find_one.assert_called_once_with({"name": "test"})


@pytest.mark.asyncio
async def test_find_all_model_by_field_name(mongodb_repo):
    mock_collection = mongodb_repo._mock_collection
    mock_cursor = MagicMock()
    mock_cursor.__aiter__.return_value = [
        {"_id": "123", "name": "test1"},
        {"_id": "456", "name": "test2"},
    ]
    mock_collection.find = MagicMock(return_value=mock_cursor)
    result = await mongodb_repo.find_all_model_by_field_name(
        "test_collection", "name", "test"
    )
    assert result == [
        {"_id": "123", "name": "test1"},
        {"_id": "456", "name": "test2"},
    ]
    mock_collection.find.assert_called_once_with({"name": "test"})


@pytest.mark.asyncio
async def test_save_entity(mongodb_repo):
    mock_collection = mongodb_repo._mock_collection
    mock_insert_result = MagicMock()
    mock_insert_result.inserted_id = "123"
    mock_collection.insert_one = AsyncMock(return_value=mock_insert_result)
    result = await mongodb_repo.save_entity("test_collection", {"name": "test"})
    assert result == "123"
    mock_collection.insert_one.assert_called_once_with({"name": "test"})


@pytest.mark.asyncio
async def test_update_entity(mongodb_repo):
    mock_collection = mongodb_repo._mock_collection
    mock_collection.update_one = AsyncMock()
    result = await mongodb_repo.update_entity(
        "name", "test", {"name": "updated_test"}, "test_collection"
    )
    assert result == {"name": "updated_test"}
    mock_collection.update_one.assert_called_once_with(
        {"name": "test"}, {"$set": {"name": "updated_test"}}
    )
