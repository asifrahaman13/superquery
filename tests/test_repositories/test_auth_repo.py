import pytest
from datetime import datetime, timedelta, timezone
from jose import jwt
from src.repositories.auth_repo import AuthRepo


@pytest.fixture
def auth_repo():
    secret_key = "test_secret_key"
    return AuthRepo(secret_key)


def test_create_refresh_token(auth_repo):
    data = {"sub": "test_user"}
    token = auth_repo.create_refresh_token(data)
    decoded_token = jwt.decode(token, auth_repo.secret_key, algorithms=["HS256"])
    assert decoded_token["sub"] == "test_user"
    assert "exp" in decoded_token


def test_create_access_token(auth_repo):
    data = {"sub": "test_user"}
    token = auth_repo.create_access_token(data)
    decoded_token = jwt.decode(token, auth_repo.secret_key, algorithms=["HS256"])
    assert decoded_token["sub"] == "test_user"
    assert "exp" in decoded_token


def test_is_access_token_expired(auth_repo):
    valid_token = jwt.encode(
        {
            "sub": "test_user",
            "exp": (datetime.now(timezone.utc) + timedelta(minutes=5)).timestamp(),
        },
        auth_repo.secret_key,
        algorithm="HS256",
    )
    expired_token = jwt.encode(
        {
            "sub": "test_user",
            "exp": (datetime.now(timezone.utc) - timedelta(minutes=5)).timestamp(),
        },
        auth_repo.secret_key,
        algorithm="HS256",
    )
    assert not auth_repo.is_access_token_expired(valid_token)
    assert auth_repo.is_access_token_expired(expired_token)


def test_generate_access_token_from_refresh_token(auth_repo):
    refresh_token = jwt.encode(
        {
            "sub": "test_user",
            "exp": (datetime.now(timezone.utc) + timedelta(hours=1)).timestamp(),
        },
        auth_repo.secret_key,
        algorithm="HS256",
    )
    access_token = auth_repo.generate_access_token_from_refresh_token(refresh_token)
    decoded_access_token = jwt.decode(
        access_token, auth_repo.secret_key, algorithms=["HS256"]
    )
    assert decoded_access_token["sub"] == "test_user"
    assert "exp" in decoded_access_token


def test_generate_access_token_from_refresh_token_missing_user_id(auth_repo):
    refresh_token = jwt.encode(
        {"exp": (datetime.now(timezone.utc) + timedelta(hours=1)).timestamp()},
        auth_repo.secret_key,
        algorithm="HS256",
    )
    with pytest.raises(ValueError, match="Refresh token is missing user ID"):
        auth_repo.generate_access_token_from_refresh_token(refresh_token)


def test_get_current_user(auth_repo):
    token = jwt.encode(
        {
            "sub": "test_user",
            "exp": (datetime.now(timezone.utc) + timedelta(hours=1)).timestamp(),
        },
        auth_repo.secret_key,
        algorithm="HS256",
    )
    user = auth_repo.get_current_user(token)
    assert user["sub"] == "test_user"
