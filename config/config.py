import yaml
from pydantic import BaseModel
import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up logging configuration
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


# Load the configuration
config = load_config("config.yaml")


# Retrieve environment variables and ensure they are set
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
assert GOOGLE_CLIENT_ID, "Google client ID is not set"
logging.info("Google client ID is set")

SECRET_KEY = os.getenv("SECRET_KEY")
assert SECRET_KEY, "Secret key is not set"
logging.info("Secret key is set")

ALGORITHM = config.security.algorithm
assert ALGORITHM, "Algorithm is not set"
logging.info("Algorithm is set")

ACCESS_TOKEN_EXPIRE_MINUTES = config.security.access_token_expire_minutes
assert ACCESS_TOKEN_EXPIRE_MINUTES, "Access token expire minutes is not set"
logging.info("Access token expire minutes is set")


OPEN_AI_API_KEY = os.getenv("OPENAI_API_KEY")
assert OPEN_AI_API_KEY, "OpenAI client is not set"
logging.info("OpenAI client is set")

MONGO_DB_URI = os.getenv("MONGO_DB_URI")
assert MONGO_DB_URI, "Mongo URI is not set"
logging.info("Mongo URI is set")


AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
assert AWS_ACCESS_KEY, "AWS access key is not set"
logging.info("AWS access key is set")

AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
assert AWS_SECRET_KEY, "AWS secret key is not set"
logging.info("AWS secret key is set")

AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
assert AWS_BUCKET_NAME, "AWS bucket name is not set"
logging.info("AWS bucket name is set")

REDIS_URL = config.redis.url
assert REDIS_URL, "Redis URL is not set."
logging.info("Redis URL is set")


DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
assert DEEPGRAM_API_KEY, "Deepgram API key is not set"
logging.info("Deepgram API key is set")


EMBEDDING_MODEL = config.vector_db.embedding_model
assert EMBEDDING_MODEL, "Embedding model is not set"
logging.info("Embedding model is set")

EMAIL_HOST = config.email_service.host
assert EMAIL_HOST, "Email host is not set"
logging.info("Email host is set")

EMAIL_PORT = config.email_service.port
assert EMAIL_PORT, "Email port is not set"
logging.info("Email port is set")

EMAIL_USERNAME = config.email_service.username
assert EMAIL_USERNAME, "Email username is not set"
logging.info("Email username is set")

EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
assert EMAIL_PASSWORD, "Email password is not set"
logging.info("Email password is set")
