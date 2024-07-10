from datetime import datetime, timedelta, timezone
from jose import ExpiredSignatureError, JWTError, jwt
from config.config import SECRET_KEY
from datetime import datetime, UTC


class AuthRepository:

    def __init__(self) -> None:
        self.secret_key = SECRET_KEY
        self.expires_delta = timedelta(hours=100)

    # Create a refresh token
    def create_refresh_token(self, data: dict) -> str:
        """
        Create a refresh token.
        """
        # Create a copy of the data and add the expiry time to the data
        to_encode = data.copy()

        # Get the current time and add the expiry time to it
        expire = datetime.now(UTC) + self.expires_delta

        to_encode.update({"exp": expire})

        # Encode the data with the secret key and return the token
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm="HS256")

        return encoded_jwt

    # Create a JWT token with the data and the expiry time
    def create_access_token(self, data: dict) -> str:

        # Create a copy of the data and add the expiry time to the data
        to_encode = data.copy()

        # Get the current time and add the expiry time to it
        expire = datetime.now(timezone.utc) + self.expires_delta

        to_encode.update({"exp": expire})

        # Encode the data with the secret key and return the token
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm="HS256")

        print(encoded_jwt)

        return encoded_jwt

    def is_access_token_expired(self, token: str) -> bool:
        """
        Check if the access token has expired.
        """
        try:
            decoded_token = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            expiry_time = decoded_token.get("exp")
            if expiry_time:
                current_time = datetime.now(timezone.utc).timestamp()
                return current_time > expiry_time
            else:
                return True  # Token has no expiry time
        except jwt.ExpiredSignatureError:
            return True  # Token has expired
        except jwt.InvalidTokenError:
            return True  # Token is invalid

    def generate_access_token_from_refresh_token(self, refresh_token: str) -> str:
        """
        Generate a new access token from a refresh token.
        """
        try:
            decoded_token = jwt.decode(
                refresh_token, self.secret_key, algorithms=["HS256"]
            )
            user_id = decoded_token.get("sub")
            if user_id:
                # Optionally, you can check if the refresh token is valid in your database
                # Here, we assume the refresh token is valid and generate a new access token
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

        try:
            # Decode the token with the secret key
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])

            print("###################", payload)

            return payload

        except JWTError:
            return None
