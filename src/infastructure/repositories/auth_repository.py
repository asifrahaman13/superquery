from datetime import datetime, timedelta, timezone
import logging
from jose import jwt
from google.oauth2 import id_token
from google.auth.transport import requests
from config.config import (
    GOOGLE_CLIENT_ID,
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)

"""
AuthRepository class is used to create and verify access tokens.
"""


class AuthRepository:

    def __init__(self) -> None:
        self.__secret_key = SECRET_KEY
        self.__google_client_id = GOOGLE_CLIENT_ID
        self.__algorithm = ALGORITHM
        self.__expires = ACCESS_TOKEN_EXPIRE_MINUTES

    def create_access_token(self, data: dict):
        # Create a new access token
        to_encode = data.copy()

        # Set the expiration time for the token
        expire = datetime.now(timezone.utc) + timedelta(hours=self.__expires)

        # Add the expiration time to the token
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode, self.__secret_key, algorithm=self.__algorithm
        )
        return encoded_jwt

    def verify_google_access_token(self, token: str):
        try:
            # Verify the access token
            id_info = id_token.verify_oauth2_token(
                token, requests.Request(), self.__google_client_id
            )

            # Return the user information
            return id_info
        except ValueError:
            # Invalid token
            return None

    def decode_access_token(self, token: str):
        logging.info("The token received is: ")
        logging.info(token)
        try:
            # Decode the access token
            payload = jwt.decode(
                token, self.__secret_key, algorithms=[self.__algorithm]
            )

            # Return the payload
            return payload
        except jwt.ExpiredSignatureError:
            # Token has expired
            return {"error": "Token has expired"}
        except jwt.JWTError:
            # Invalid token
            return {"error": "Invalid token"}
