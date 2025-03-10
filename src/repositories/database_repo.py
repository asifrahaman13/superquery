import logging
from typing import Any, Awaitable, Optional

from motor.motor_asyncio import AsyncIOMotorClient


class MongodbRepo:
    def __init__(
        self, mongodb_client: AsyncIOMotorClient, mongodb_database: str
    ) -> None:
        self.client = mongodb_client
        self.database = self.client[mongodb_database]

    async def find_single_entity_by_field_name(
        self, collection_name: str, field_name: str, field_value: str
    ) -> Awaitable[Optional[dict]]:
        try:
            collection = self.database[collection_name]
            result = await collection.find_one({field_name: field_value})
            if result:
                result["_id"] = str(result["_id"])
            return result
        except Exception:
            return None

    async def find_all_model_by_field_name(
        self, collection_name: str, field_name: str, field_value: str
    ) -> Awaitable[Optional[list[dict]]]:
        try:
            collection = self.database[collection_name]
            cursor = collection.find({field_name: field_value})
            all_documents = []
            async for item in cursor:
                item["_id"] = str(item["_id"])
                all_documents.append(item)
            return all_documents
        except Exception:
            return None

    async def save_entity(
        self, collection_name: str, entity: dict[str, Any]
    ) -> Awaitable[Optional[str]]:
        try:
            collection = self.database[collection_name]
            result = await collection.insert_one(entity)
            return str(result.inserted_id)
        except Exception:
            return None

    async def update_entity(
        self,
        filter_key: str,
        filter_value: str,
        update_data: dict[str, Any],
        collection_name: str,
    ) -> Awaitable[Optional[dict[str, Any]]]:
        try:
            collection = self.database[collection_name]
            await collection.update_one(
                {filter_key: filter_value}, {"$set": update_data}
            )
            return update_data
        except Exception as e:
            logging.error(f"Failed to update data: {e}")
            return None
