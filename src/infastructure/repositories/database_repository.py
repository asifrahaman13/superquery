"""
Database repository is used to interact with the MongoDB database.
It is separate entity from the rest of the program.
"""

import logging
from typing import Any, Dict


class MongodbRepository:
    def __init__(self, mongodb_client, mongodb_database) -> None:
        self.__client = mongodb_client
        self.__database = self.__client[mongodb_database]

    def find_single_entity_by_field_name(
        self, collection_name: str, field_name: str, field_value: str
    ):
        try:
            collection = self.__database[collection_name]
            result = collection.find_one({field_name: field_value})
            result["_id"] = str(result["_id"])
            return result
        except Exception as e:
            return None

    def find_all_entities_by_field_name(
        self, collection_name: str, file_name: str, field_value: str
    ):
        try:
            collection = self.__database[collection_name]
            results = collection.find({file_name: field_value})
            all_documents = []
            for item in results:
                item["_id"] = str(item["_id"])
                all_documents.append(item)
            return all_documents
        except Exception as e:
            return None

    def save_entity(self, collection_name: str, entity: Dict[str, Any]):
        try:
            collection = self.__database[collection_name]
            result = collection.insert_one(entity).inserted_id
            return result
        except Exception as e:
            return None

    def update_entity(
        self,
        filter_key: str,
        filter_value: str,
        update_data: dict,
        collection_name: str,
    ):
        try:
            # Define the collection where the data will be updated
            collection = self.__database[collection_name]

            # Update the document in the collection
            collection.update_one({filter_key: filter_value}, {"$set": update_data})

            # Return the updated data
            return update_data
        except Exception as e:
            logging.error(f"Failed to update data: {e}")
            return None
