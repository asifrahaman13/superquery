from typing import Annotated, Any, Optional
from pydantic import BaseModel, Field


class Query(BaseModel):
    query: Annotated[str, "The query to be executed"]


class UserBase(BaseModel):
    email: Annotated[Optional[str], "The email of the user"] = None
    username: Annotated[str, "The username of the user"]
    password: Annotated[str, "The password of the user"]


class AnswerFormat(BaseModel):
    answer_type: str


class QueryResponse(BaseModel):
    json_message: Any = Field(None, description="The json message")
    message: Any = None
    status: Annotated[Optional[bool], "The status of the response"]
    answer_type: Annotated[Optional[str], "The type of the answer"] = None
    sql_query: Annotated[Optional[str], "The sql query"] = None


class ConfigurationBase(BaseModel):
    db_type: Annotated[str, "Database type"] = None


class QueryBase(BaseModel):
    raw_query: Annotated[str, "Raw query to execute"]
    db_type: Annotated[str, "Database type"]


class UpdateConfig(BaseModel):
    class ConfigDict:
        extra = "allow"


class Files(BaseModel):
    file_name: Annotated[str, "File name"]


class TrainData(BaseModel):
    user_query: Annotated[str, "Training data of user query"]
    sql_query: Annotated[str, "Training data of sql query"]
    metadata: list[dict[str, str]]
