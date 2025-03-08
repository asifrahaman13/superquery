from fastapi import APIRouter, Depends, Header
from src.exports.index import get_auth_service
from src.use_cases.auth_service import AuthService
from src.entities.router_models import UserBase

auth_controller = APIRouter()


@auth_controller.post("/signup", response_model=dict)
async def register(
    user: UserBase, auth_service: AuthService = Depends(get_auth_service)
):
    try:
        response = auth_service.signup(user.username, user.email, user.password)
        if response is None:
            return {"error": "Some error occured."}
        return {"message": "User registered successfully."}
    except Exception:
        return {"error": "Some error occured."}


@auth_controller.post("/login", response_model=dict)
async def login(user: UserBase, auth_service: AuthService = Depends(get_auth_service)):
    try:
        response = auth_service.login(user.username, user.password)
        return {"access_token": response, "token_type": "bearer"}

    except Exception:
        return {"error": "Some error occured."}


@auth_controller.post("/user", response_model=dict)
async def get_user(
    token: str = Header(..., alias="Authorization"),
    auth_service: AuthService = Depends(get_auth_service),
):
    try:
        token = token.split(" ")[1]
        response = auth_service.user_info(token)
        return response

    except Exception:
        return {"error": "Some error occured."}
