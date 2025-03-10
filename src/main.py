import logging
import os
from math import ceil

from contextlib import asynccontextmanager
import redis.asyncio as redis
import uvicorn
from fastapi.responses import JSONResponse
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from starlette.middleware.cors import CORSMiddleware
from src.middleware.logging_middleware import PrefixMiddleware
from fastapi import Depends, FastAPI, HTTPException, Request, Response, status

from src.application.web.controllers import (
    auth_controller,
    query_controller,
    raw_query_controller,
    upload_controller,
    configuration_controller,
)
from src.repositories import (
    SemanticEmbeddingService,
    SemanticQdrantService,
    SemanticSearchRepo,
)
from src.exports import config

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
    semantic_embedding_service = SemanticEmbeddingService()
    semantic_qdrant_service = SemanticQdrantService(
        url=config.qdrant_api_endpoint, api_key=config.qdrant_api_key
    )
    semantic_search_repo = SemanticSearchRepo(
        embedding_service=semantic_embedding_service,
        qdrant_service=semantic_qdrant_service,
    )
    await semantic_search_repo.create_collection("superquery")

    redis_connection = redis.from_url(config.redis_url, encoding="utf8")
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
