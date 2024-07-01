from src.internal.interfaces.services.database_interface import DatabaseInterface
from src.infastructure.repositories.database_repository import (
    DatabaseRepository,
)


class DatabaseService(DatabaseInterface):

    def __init__(
        self, database_repository: DatabaseRepository = DatabaseRepository
    ) -> None:
        self.database_repository = database_repository

    def find_one(self, field: str, field_value: str, collection_name: str) -> dict:
        return self.database_repository.find_single_document(
            field, field_value, collection_name
        )

    def insert_one(self, data: dict, collection_name: str) -> None:
        return self.database_repository.insert_single_document(data, collection_name)

    def find_all(self, collection_name: str) -> list:
        return self.database_repository.find_all(collection_name)

    def find_all_documents_from_field(
        self, field: str, field_value: str, collection_name: str
    ) -> list:
        return self.database_repository.find_all_documents_from_field(
            field, field_value, collection_name
        )
