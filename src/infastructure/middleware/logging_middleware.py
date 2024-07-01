import logging
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from src.infastructure.repositories.auth_repository import AuthRepository
from src.internal.use_cases.auth_service import AuthService
from src.internal.interfaces.services.auth_interface import AuthInterface

auth_repository = AuthRepository()
auth_service = AuthService(auth_repository)


class PrefixMiddleware(BaseHTTPMiddleware):
    """
    Middleware to check the prefix of the request being made and authenticate the user baded on that.
    If token is not provided for protected routes then unauthorized message is sent.
    However if token is provided then decoding is attempted. If the decoding shows that the user is actually an
    authenticated user and the token is not expired yet then the user is allowed to make the request.
    """

    def __init__(self, app, prefix=""):
        super().__init__(app)
        self.app = app
        self.prefix = prefix
        self.protected_routes = ["fhir", "data"]

    async def authenticate(self, request):
        auth_interface: AuthInterface = auth_service
        logging.info("############################# authenticating")
        try:
            """
            For the post requsts the token is made in the form of authorization headers and hence we
            need to extract the data from the authorization header.
            """
            if request.method == "POST":
                token = request.headers.get("Authorization").split(" ")[1]
            else:

                """
                In the routes the token for other requests are usually taken in the form of params.
                So the token is extracted from the params.
                """
                token = request.url.path.split("/")[-1]
                logging.info("The token is: {}".format(token))

            logging.info(f"Token: {token}")
            if not token:
                raise HTTPException(status_code=401, detail="Unauthorized")

            result = auth_interface.decode_access_token(token)
            logging.info(result)
            if "error" in result:
                raise HTTPException(status_code=401, detail="Unauthorized")
        except Exception as e:
            raise HTTPException(status_code=401, detail="Unauthorized")

    async def dispatch(self, request, call_next):

        # Extract out the prefix from the URL.
        self.prefix = request.url.path.split("/")[1]

        logging.info(f"Request with prefix {self.prefix}")

        # If the prefix is among the protected routes then check the token of the routes.
        if self.prefix in self.protected_routes:
            logging.info(f"Protected route {self.protected_routes}")
            try:
                await self.authenticate(request)

                # If no exception occured then allow the further stesp.
                response = await call_next(request)
                return response
            except HTTPException as e:
                return JSONResponse(
                    status_code=e.status_code, content={"message": str(e)}
                )
        else:
            response = await call_next(request)
            return response
