from typing import Dict
from fastapi import Depends, HTTPException, Header
from exports.exports import get_auth_service
from src.internal.use_cases.auth_service import AuthService

"""
A dependency function to get the current user from the token.
Validates if the user is valid and authenticated.
"""
def get_current_user(
    token: str = Header(..., alias="Authorization"),
    auth_service: AuthService = Depends(get_auth_service),
) -> Dict:
    if token is None:
        raise HTTPException(status_code=400, detail="Token is required.")
    try:
        user = auth_service.user_info(token.split(" ")[1])
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid token or user not found.")
        return user
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token or user not found.")