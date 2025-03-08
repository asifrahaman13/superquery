import logging
from typing import Any, Dict


class MongodbRepo:
    def __init__(self, mongodb_client, mongodb_database) -> None:
        self.client = mongodb_client
        self.database = self.client[mongodb_database]

    def find_single_entity_by_field_name(
        self, collection_name: str, field_name: str, field_value: str
    ):
        try:
            collection = self.database[collection_name]
            result = collection.find_one({field_name: field_value})
            result["_id"] = str(result["_id"])
            return result
        except Exception:
            return None

    def find_all_entities_by_field_name(
        self, collection_name: str, file_name: str, field_value: str
    ):
        try:
            collection = self.database[collection_name]
            results = collection.find({file_name: field_value})
            all_documents = []
            for item in results:
                item["_id"] = str(item["_id"])
                all_documents.append(item)
            return all_documents
        except Exception:
            return None

    def save_entity(self, collection_name: str, entity: Dict[str, Any]):
        try:
            collection = self.database[collection_name]
            result = collection.insert_one(entity).inserted_id
            return result
        except Exception:
            return None

    def update_entity(
        self,
        filter_key: str,
        filter_value: str,
        update_data: dict,
        collection_name: str,
    ):
        try:
            collection = self.database[collection_name]
            collection.update_one({filter_key: filter_value}, {"$set": update_data})
            return update_data
        except Exception as e:
            logging.error(f"Failed to update data: {e}")
            return None
