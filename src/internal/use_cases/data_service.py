from src.internal.interfaces.services.data_interface import DataInterface
from src.infastructure.repositories.database_repository import MongodbRepository
from typing import Any, Dict


class DataService(DataInterface):

    def __init__(self, data_repository: MongodbRepository = MongodbRepository) -> None:
        self.data_repository = data_repository

    def query_sql(self, query: str) -> Dict[str, Any]:
        return self.data_repository.query_on_mysql_db(query)
