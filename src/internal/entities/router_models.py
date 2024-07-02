from pydantic import BaseModel


class Query(BaseModel):
    query: str


class UserBase(BaseModel):
    email: str | None = None
    username: str | None = None
    password: str | None = None
