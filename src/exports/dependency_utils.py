from fastapi import Depends, HTTPException, Header

from exports import get_auth_service
from src.use_cases import AuthService


def get_current_user(
    token: str = Header(..., alias="Authorization"),
    auth_service: AuthService = Depends(get_auth_service),
) -> dict:
    try:
        user = auth_service.user_info(token.split(" ")[1])
        if user is None:
            raise HTTPException(
                status_code=401, detail="Invalid token or user not found."
            )
        return user
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token or user not found.")
