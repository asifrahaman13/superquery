import logging
import os
from contextlib import asynccontextmanager
from math import ceil

import redis.asyncio as redis
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request, Response, status
from fastapi.responses import JSONResponse
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from starlette.middleware.cors import CORSMiddleware

from src.application.web.controllers.auth_controller import auth_controller
from src.application.web.controllers.configuration_controller import (
    configuration_controller,
)
from src.application.web.controllers.file_controller import upload_controller
from src.application.web.controllers.query_controller import query_controller
from src.application.web.controllers.raw_query import raw_query_controller
from src.config.config import QDRANT_API_ENDPOINT, QDRANT_API_KEY, REDIS_URL
from src.middleware.logging_middleware import PrefixMiddleware
from src.repositories.semantic_repo import (
    SemanticEmbeddingService,
    SemanticQdrantService,
    SemanticSearchRepo,
)

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


async def client_identifier(request: Request):
    return request.client.host


async def custom_callback(request: Request, response: Response, pexpire: int):
    expire = ceil(pexpire / 1000)
    raise HTTPException(
        status.HTTP_429_TOO_MANY_REQUESTS,
        f"Too Many Requests. Retry after {expire} seconds.",
        headers={"Retry-After": str(expire)},
    )


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Initialize Qdrant

    semantic_embedding_service = SemanticEmbeddingService()
    semantic_qdrant_service = SemanticQdrantService(
        url=QDRANT_API_ENDPOINT, api_key=QDRANT_API_KEY
    )
    semantic_search_repo = SemanticSearchRepo(
        embedding_service=semantic_embedding_service,
        qdrant_service=semantic_qdrant_service,
    )
    await semantic_search_repo.create_collection("superquery")

    redis_connection = redis.from_url(REDIS_URL, encoding="utf8")
    await FastAPILimiter.init(
        redis=redis_connection,
        identifier=client_identifier,
        http_callback=custom_callback,
    )
    yield
    await FastAPILimiter.close()


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    auth_controller,
    prefix="/auth",
    tags=["Auth router"],
    dependencies=[
        Depends(RateLimiter(times=10, seconds=10, identifier=client_identifier))
    ],
)
app.include_router(
    query_controller,
    prefix="/query",
    tags=["Query router"],
)
app.include_router(
    configuration_controller,
    prefix="/config",
    tags=["Configuration router"],
    dependencies=[
        Depends(RateLimiter(times=10, seconds=10, identifier=client_identifier))
    ],
)
app.include_router(
    raw_query_controller,
    prefix="/raw-query",
    tags=["Raw Query router"],
    dependencies=[
        Depends(RateLimiter(times=10, seconds=10, identifier=client_identifier))
    ],
)
app.include_router(
    upload_controller,
    prefix="/upload",
    tags=["Upload router"],
    dependencies=[
        Depends(RateLimiter(times=10, seconds=10, identifier=client_identifier))
    ],
)
app.add_middleware(PrefixMiddleware)


@app.get(
    "/health",
    dependencies=[
        Depends(RateLimiter(times=10, seconds=10, identifier=client_identifier))
    ],
)
async def health_check(request: Request):
    ip = request.client.host
    logging.info(f"Request from IP: {ip}")
    return JSONResponse(status_code=200, content={"status": "healthy"})


@app.get("/")
async def health_check_status():
    return JSONResponse(
        status_code=200,
        content={"status": "The server is running as expected."},
    )


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))
    logging.info(f"Starting server on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
