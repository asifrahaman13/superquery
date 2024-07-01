
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
        self.__instances={}

    def get_mysql_query_repository(self):
        if "mysql_query_repository" not in self.__instances:
            self.__instances["mysql_query_repository"]=DatabaseRepository(MongoClient(MONGO_DB_URI), "octo")
        return self.__instances["mysql_query_repository"]

    def get_mysql_query_service(self):
        if "mysql_query_repository" not in self.__instances:
            
            self.__instances["mysql_query_repository"]=DataService(self.get_mysql_query_repository())
        return self.__instances["mysql_query_repository"]


container = DIContainer()

def get_database_service():
    return container.get_mysql_query_service()