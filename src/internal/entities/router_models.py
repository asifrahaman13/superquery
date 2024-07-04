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


class QueryBase(BaseModel):
    raw_query: Annotated[str, "Raw query to execute"]
    db_type: Annotated[str, "Database type"]


class UpdateConfig(BaseModel):
    db_type: Annotated[str, "Database type"]
    projectName: Annotated[str, "The name of the project"]
    username: Annotated[str, "The username of the MySQL database"]
    description: str = Annotated[Optional[str], "The description of the MySQL database"]
    mysqlConnectionString: Annotated[str, "The connection string of the MySQL database"]
