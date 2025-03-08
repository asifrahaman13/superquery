from infastructure.repositories.database_repo import MongodbRepo
from typing import Any, Dict


class DataService:
    def __init__(self, data_repository: MongodbRepo = MongodbRepo) -> None:
        self.data_repository = data_repository

    def query_sql(self, query: str) -> Dict[str, Any]:
        return self.data_repository.query_on_mysql_db(query)
