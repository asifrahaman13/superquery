import pytest
from unittest.mock import AsyncMock, MagicMock
from src.use_cases.auth_service import AuthService


@pytest.mark.asyncio
async def test_signup_user_already_exists():
    mock_auth_repo = MagicMock()
    mock_database_repo = AsyncMock()
    mock_database_repo.find_single_entity_by_field_name.return_value = {
        "username": "test_user"
    }

    auth_service = AuthService(mock_auth_repo, mock_database_repo)

    result = await auth_service.signup("test_user", "test@example.com", "password123")

    assert result is None
    mock_database_repo.find_single_entity_by_field_name.assert_called_once_with(
        "users", "username", "test_user"
    )


@pytest.mark.asyncio
async def test_signup_save_user_fails():
    mock_auth_repo = MagicMock()
    mock_database_repo = AsyncMock()
    mock_database_repo.find_single_entity_by_field_name.return_value = None
    mock_database_repo.save_entity.return_value = None

    auth_service = AuthService(mock_auth_repo, mock_database_repo)

    result = await auth_service.signup("test_user", "test@example.com", "password123")

    assert result is None
    mock_database_repo.save_entity.assert_called()


@pytest.mark.asyncio
async def test_signup_success():
    mock_auth_repo = MagicMock()
    mock_database_repo = AsyncMock()
    mock_database_repo.find_single_entity_by_field_name.return_value = None
    mock_database_repo.save_entity.side_effect = [{"id": 1}, {"id": 2}]

    auth_service = AuthService(mock_auth_repo, mock_database_repo)

    result = await auth_service.signup("test_user", "test@example.com", "password123")

    assert result == {"id": 1}
    mock_database_repo.save_entity.assert_called()


@pytest.mark.asyncio
async def test_login_invalid_credentials():
    mock_auth_repo = MagicMock()
    mock_database_repo = AsyncMock()
    mock_database_repo.find_single_entity_by_field_name.return_value = None

    auth_service = AuthService(mock_auth_repo, mock_database_repo)

    result = await auth_service.login("test_user", "wrong_password")

    assert result is None
    mock_database_repo.find_single_entity_by_field_name.assert_called_once_with(
        "users", "username", "test_user"
    )


@pytest.mark.asyncio
async def test_login_success():
    mock_auth_repo = MagicMock()
    mock_auth_repo.create_access_token.return_value = "mock_token"
    mock_database_repo = AsyncMock()
    mock_database_repo.find_single_entity_by_field_name.return_value = {
        "username": "test_user",
        "password": "password123",
    }

    auth_service = AuthService(mock_auth_repo, mock_database_repo)

    result = await auth_service.login("test_user", "password123")

    assert result == "mock_token"
    mock_auth_repo.create_access_token.assert_called_once_with({"sub": "test_user"})


def test_user_info():
    mock_auth_repo = MagicMock()
    mock_auth_repo.get_current_user.return_value = {"username": "test_user"}
    mock_database_repo = MagicMock()

    auth_service = AuthService(mock_auth_repo, mock_database_repo)

    result = auth_service.user_info("mock_token")

    assert result == {"username": "test_user"}
    mock_auth_repo.get_current_user.assert_called_once_with("mock_token")
