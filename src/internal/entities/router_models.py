from typing import Annotated, Optional
from pydantic import BaseModel


class Query(BaseModel):
    query: Annotated[str, "The query to be executed"]


class UserBase(BaseModel):
    email: Annotated[Optional[str], "The email of the user"] = None
    username: Annotated[str, "The username of the user"]
    password: Annotated[str, "The password of the user"]


class AnswerFormat(BaseModel):
    answer_type: str


class QueryResponse(BaseModel):
    message: Annotated[str, "The response message"]
    status: Annotated[Optional[bool], "The status of the response"]
    answer_type: Annotated[Optional[str], "The type of the answer"] = None


class ConfigurationBase(BaseModel):
    db_type: Annotated[str, "Database type"] = None
