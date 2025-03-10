import yaml
import os
import logging
from dotenv import load_dotenv
from dataclasses import dataclass
from functools import lru_cache
from pydantic import BaseModel

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
    vector_db: VectorizerConfig
    email_service: EmailConfig


@dataclass
class ConfigData:
    config: dict
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    anthropic_api_key: str
    mongo_db_uri: str
    redis_url: str
    redis_port: str
    redis_host: str
    redis_password: str
    aws_bucket_name: str
    aws_access_key_id: str
    aws_secret_access_key: str
    embedding_model: str
    qdrant_api_key: str
    qdrant_api_endpoint: str
    anthropic_model: str


class ConfigManager:
    def __init__(self, config_path: str):
        self.config = self.load_config(config_path)
        self.load_env_variables()

    def load_config(self, file_path: str) -> Config:
        with open(file_path, "r") as file:
            config_dict = yaml.safe_load(file)
        return Config(**config_dict)

    def load_env_variables(self):
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        assert self.SECRET_KEY, "Secret key is not set"

        self.ALGORITHM = self.config.security.algorithm
        assert self.ALGORITHM, "Algorithm is not set"

        self.ACCESS_TOKEN_EXPIRE_MINUTES = (
            self.config.security.access_token_expire_minutes
        )
        assert (
            self.ACCESS_TOKEN_EXPIRE_MINUTES
        ), "Access token expire minutes is not set"

        self.ANTHROPIC_API_KEY = os.getenv("OPENAI_API_KEY")
        assert self.ANTHROPIC_API_KEY, "OpenAI client is not set"

        self.MONGO_DB_URI = os.getenv("MONGO_DB_URI")
        assert self.MONGO_DB_URI, "Mongo URI is not set"

        self.REDIS_URL = os.getenv("REDIS_URL") 
        assert self.REDIS_URL, "Redis URL is not set."

        self.REDIS_PORT = os.getenv("REDIS_PORT")
        assert self.REDIS_PORT, "Redis port is not set."

        self.REDIS_HOST = os.getenv("REDIS_HOST")
        assert self.REDIS_HOST, "Redis host is not set."

        self.REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
        assert self.REDIS_PASSWORD, "Redis password is not set."

        self.AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
        assert self.AWS_BUCKET_NAME, "AWS bucket name is not set."

        self.AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY")
        assert self.AWS_ACCESS_KEY_ID, "AWS access key is not set."

        self.AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS")
        assert self.AWS_SECRET_ACCESS_KEY, "AWS secret access key is not set."

        self.EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
        assert self.EMBEDDING_MODEL, "Embedding model is not set"

        self.QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
        assert self.QDRANT_API_KEY, "Qdrant API key not set"

        self.QDRANT_API_ENDPOINT = os.getenv("QDRANT_API_ENDPOINT")
        assert self.QDRANT_API_ENDPOINT, "Qdrant api endpoint not set"

        self.ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL")
        assert self.ANTHROPIC_MODEL, "Anthropic model is not set"

    def to_config_data(self) -> ConfigData:
        return ConfigData(
            config=self.config.model_dump(),
            secret_key=self.SECRET_KEY,
            algorithm=self.ALGORITHM,
            access_token_expire_minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES,
            anthropic_api_key=self.ANTHROPIC_API_KEY,
            mongo_db_uri=self.MONGO_DB_URI,
            redis_url=self.REDIS_URL,
            redis_port=self.REDIS_PORT,
            redis_host=self.REDIS_HOST,
            redis_password=self.REDIS_PASSWORD,
            aws_bucket_name=self.AWS_BUCKET_NAME,
            aws_access_key_id=self.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=self.AWS_SECRET_ACCESS_KEY,
            embedding_model=self.EMBEDDING_MODEL,
            qdrant_api_key=self.QDRANT_API_KEY,
            qdrant_api_endpoint=self.QDRANT_API_ENDPOINT,
            anthropic_model=self.ANTHROPIC_MODEL,
        )


@lru_cache()
def get_config():
    config_manager = ConfigManager("config.yaml")
    return config_manager.to_config_data()


config = get_config()
