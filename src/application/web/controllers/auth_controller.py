from fastapi import APIRouter, Depends, HTTPException, Header
from src.exports.index import get_auth_service
from src.use_cases.auth_service import AuthService
from src.entities.router_models import UserBase

auth_controller = APIRouter()


@auth_controller.post("/signup", response_model=dict)
async def register(
    user: UserBase, auth_service: AuthService = Depends(get_auth_service)
):
    try:
        response = await auth_service.signup(user.username, user.email, user.password)
        if response is None:
            return HTTPException(status_code=400, detail="User already exists.")
        return {"message": "User registered successfully."}
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))


@auth_controller.post("/login", response_model=dict)
async def login(user: UserBase, auth_service: AuthService = Depends(get_auth_service)):
    try:
        response = await auth_service.login(user.username, user.password)
        return {"access_token": response, "token_type": "bearer"}

    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))


@auth_controller.post("/user", response_model=dict)
async def get_user(
    token: str = Header(..., alias="Authorization"),
    auth_service: AuthService = Depends(get_auth_service),
):
    try:
        token = token.split(" ")[1]
        response = auth_service.user_info(token)
        return response

    except Exception as e:
        return HTTPException(status_code=400, detail="Invalid token")
