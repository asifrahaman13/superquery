import yaml
from pydantic import BaseModel
import os
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class AppConfig(BaseModel):
    title: str
    version: str
    description: str


class ServerConfig(BaseModel):
    host: str
    port: int


class DatabaseConfig(BaseModel):
    # url: str
    pool_size: int


class SecurityConfig(BaseModel):
    algorithm: str
    access_token_expire_minutes: int


class RedisConfig(BaseModel):
    url: str


class VectorizerConfig(BaseModel):
    embedding_model: str


class EmailConfig(BaseModel):
    host: str
    port: int
    username: str


class Config(BaseModel):
    app: AppConfig
    server: ServerConfig
    database: DatabaseConfig
    security: SecurityConfig
    redis: RedisConfig
    vector_db: VectorizerConfig
    email_service: EmailConfig


def load_config(file_path: str) -> Config:
    with open(file_path, "r") as file:
        config_dict = yaml.safe_load(file)
    return Config(**config_dict)


config = load_config("config.yaml")

SECRET_KEY = os.getenv("SECRET_KEY")
assert SECRET_KEY, "Secret key is not set"

ALGORITHM = config.security.algorithm
assert ALGORITHM, "Algorithm is not set"

ACCESS_TOKEN_EXPIRE_MINUTES = config.security.access_token_expire_minutes
assert ACCESS_TOKEN_EXPIRE_MINUTES, "Access token expire minutes is not set"

anthropic_API_KEY = os.getenv("OPENAI_API_KEY")
assert anthropic_API_KEY, "OpenAI client is not set"

MONGO_DB_URI = os.getenv("MONGO_DB_URI")
assert MONGO_DB_URI, "Mongo URI is not set"

REDIS_URL = config.redis.url
assert REDIS_URL, "Redis URL is not set."

REDIS_PORT = os.getenv("REDIS_PORT")
assert REDIS_PORT, "Redis port is not set."

REDIS_HOST = os.getenv("REDIS_HOST")
assert REDIS_HOST, "Redis host is not set."

REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
assert REDIS_PASSWORD, "Redis password is not set."

AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
assert AWS_BUCKET_NAME, "AWS bucket name is not set."

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY")
assert AWS_ACCESS_KEY_ID, "AWS access key is not set."

AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS")
assert AWS_SECRET_ACCESS_KEY, "AWS secret access key is not set."


EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
assert EMBEDDING_MODEL, "Embedding model is not set"


QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
assert QDRANT_API_KEY, "Qdrant API key not set"

QDRANT_API_ENDPOINT = os.getenv("QDRANT_API_ENDPOINT")
assert QDRANT_API_ENDPOINT, "Qdrant api endpoint not set"


ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL")
assert ANTHROPIC_MODEL, "Anthropic model is not set"
