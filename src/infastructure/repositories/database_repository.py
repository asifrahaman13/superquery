"""
Database repository is used to interact with the MongoDB database.
It is separate entity from the rest of the program.
"""


class MongodbRepository:
    def __init__(self, mongodb_client, mongodb_database) -> None:
        self.__client = mongodb_client
        self.__database = self.__client[mongodb_database]

    def find_single_entity_by_field_name(
        self, collection_name, field_name, field_value
    ):
        try:
            collection = self.__database[collection_name]
            result = collection.find_one({field_name: field_value})
            result["_id"] = str(result["_id"])
            return result
        except Exception as e:
            return None
        finally:
            self.__client.close()

    def find_all_entities_by_field_name(self, collection_name):
        try:
            collection = self.__database[collection_name]
            return collection.find()
        except Exception as e:
            return None
        finally:
            self.__client.close()
