import logging
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from src.use_cases.auth_service import AuthService
from starlette.middleware.base import BaseHTTPMiddleware
from src.exports.index import get_auth_service


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class PrefixMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, prefix=""):
        super().__init__(app)
        self.app = app
        self.prefix = prefix
        self.protected_routes = ["raw-query", "config"]

    async def authenticate(self, request):
        auth_interface: AuthService = get_auth_service()
        logging.info(f"Authenticating")
        try:
            logging.info(f"Method: {request.method}")
            if request.method == "POST":
                token = request.headers.get("Authorization").split(" ")[1]
                logging.info(f"Token: {token}")
            elif request.method == "GET":
                token = request.url.path.split("/")[-1]
                logging.info(f"The token is: {token}")
            elif request.method == "PUT":
                token = request.headers.get("Authorization").split(" ")[1]

            logging.info(f"Token: {token}")
            if not token:
                raise HTTPException(status_code=401, detail="Unauthorized")

            result = auth_interface.user_info(token)
            logging.info(result)
            if "error" in result:
                raise HTTPException(status_code=401, detail="Unauthorized")
        except Exception:
            raise HTTPException(status_code=401, detail="Unauthorized")

    async def dispatch(self, request, call_next):
        self.prefix = request.url.path.split("/")[1]
        logging.info(f"Request with prefix {self.prefix}")
        if request.method == "OPTIONS":
            response = await call_next(request)
            return response
        if self.prefix in self.protected_routes:
            logging.info(f"Protected route {self.protected_routes}")
            try:
                await self.authenticate(request)
                response = await call_next(request)
                return response
            except HTTPException as e:
                return JSONResponse(
                    status_code=e.status_code, content={"message": str(e)}
                )
        else:
            response = await call_next(request)
            return response
