from src.infastructure.repositories.mongodb_query_repository import (
    MongodbQueryRepository,
)
from src.infastructure.repositories.mysql_query_repository import MySqlQueryRepository
from src.internal.use_cases.query_service import QueryService
from src.internal.use_cases.data_service import DataService
from src.ConnectionManager.ConnectionManager import ConnectionManager
from src.infastructure.repositories.database_repository import (
    DatabaseRepository,
)
from pymongo import MongoClient
from typing import Any, Dict
import logging
from config.config import MONGO_DB_URI


class DIContainer:
    def __init__(self):
        self.__instances = {}

    def get_mysql_query_repository(self):
        if "mysql_query_repository" not in self.__instances:
            self.__instances["mysql_query_repository"] = MySqlQueryRepository()
        return self.__instances["mysql_query_repository"]

    def get_mongodb_query_repository(self):
        if "mongodb_query_repository" not in self.__instances:
            self.__instances["mongodb_query_repository"] = MongodbQueryRepository(
                MongoClient(MONGO_DB_URI), "test"
            )
        return self.__instances["mongodb_query_repository"]

    def get_mysql_query_database_service(self):
        if "mysql_query_service" not in self.__instances:

            self.__instances["mysql_query_service"] = QueryService(
                self.get_mysql_query_repository()
            )
        return self.__instances["mysql_query_service"]

    def get_mongodb_query_database_service(self):
        if "mongodb_query_service" not in self.__instances:
            self.__instances["mongodb_query_service"] = QueryService(
                self.get_mongodb_query_repository()
            )
        return self.__instances["mongodb_query_service"]


container = DIContainer()


def get_mysql_query_database_service():
    return container.get_mysql_query_database_service()

def get_mongodb_query_database_service():
    return container.get_mongodb_query_database_service()
