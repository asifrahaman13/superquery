from src.repositories.database_repo import MongodbRepo
from typing import Any


class DataService:
    def __init__(self, data_repository: MongodbRepo = MongodbRepo) -> None:
        self.data_repository = data_repository

    def query_sql(self, query: str) -> dict[str, Any]:
        return self.data_repository.query_on_mysql_db(query)
