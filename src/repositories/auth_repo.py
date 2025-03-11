from datetime import datetime, timedelta, timezone
from jose import ExpiredSignatureError, JWTError, jwt
from datetime import UTC


class AuthRepo:
    def __init__(self, secret_key: str) -> None:
        self.secret_key = secret_key
        self.expires_delta = timedelta(hours=100)

    def create_refresh_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(UTC) + self.expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm="HS256")
        return encoded_jwt

    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + self.expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm="HS256")
        return encoded_jwt

    def is_access_token_expired(self, token: str) -> bool:
        try:
            decoded_token = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            expiry_time = decoded_token.get("exp")
            if expiry_time:
                current_time = datetime.now(timezone.utc).timestamp()
                return current_time > expiry_time
            else:
                return True
        except jwt.ExpiredSignatureError:
            return True
        except jwt.InvalidTokenError:
            return True

    def generate_access_token_from_refresh_token(self, refresh_token: str) -> str:
        try:
            decoded_token = jwt.decode(
                refresh_token, self.secret_key, algorithms=["HS256"]
            )
            user_id = decoded_token.get("sub")
            if user_id:
                access_token_expires = timedelta(hours=6)
                access_token = self.create_access_token(
                    {"sub": user_id}, access_token_expires
                )
                return access_token
            else:
                raise ValueError("Refresh token is missing user ID")
        except ExpiredSignatureError:
            raise ValueError("Refresh token has expired")
        except JWTError:
            raise ValueError("Invalid refresh token")

    def get_current_user(self, token) -> str:
        payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
        return payload
