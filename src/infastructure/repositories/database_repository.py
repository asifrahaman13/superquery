from pymongo import MongoClient
from typing import Any, Dict
import logging
from config.config import MONGO_DB_URI

"""
Database repository is used to interact with the MongoDB database.
It is separate entity from the rest of the program.
"""


class DatabaseRepository:
    def __init__(self):

        # Connect to the database
        self.__client = MongoClient(MONGO_DB_URI)
        self.__db = self.__client["octo"]

    def insert_single_document(self, data: str, collection_name: str):

        try:
            # Define the collection where the data will be stored
            collection = self.__db[collection_name]

            # Insert the data into the collection
            collection.insert_one(data)

            # Return the data that was stored
            return data
        except Exception as e:
            logging.error(f"Failed to insert data: {e}")
            return None

    def find_all(self, field: str, field_value: str, collection_name: str):

        # Create an empty list to store the data that will be found
        all_documents = []
        try:

            # Define the collection where the data will be stored
            collection = self.__db[collection_name]

            # Find all the data that matches the username
            data = collection.find({field: field_value})

            for item in data:
                item["_id"] = str(item["_id"])
                all_documents.append(item)

            # Return the data that was found
            return all_documents
        except Exception as e:
            logging.error(f"Failed to find data: {e}")
            return None

    def find_all_documents(self, collection_name: str):
        # Create an empty list to store the data that will be found
        all_documents = []
        try:
            # Define the collection where the data will be stored
            collection = self.__db[collection_name]

            # Find all the data that matches the username
            data = collection.find()

            for item in data:
                item["_id"] = str(item["_id"])
                all_documents.append(item)

            # Return the data that was found
            return all_documents
        except Exception as e:
            logging.error(f"Failed to find data: {e}")
            return None

    def find_single_document(self, field: str, field_value: str, collection_name: str):
        try:

            # Define the collection where the data will be stored
            collection = self.__db[collection_name]

            # Find the data that matches the username
            result = collection.find_one({field: field_value})

            if result is None:
                return None
            result["_id"] = str(result["_id"])

            # Return the data that was found
            return result
        except Exception as e:
            logging.error(f"Failed to find data: {e}")
            return None

    def delete_one(self, field: str, field_value: str, collection_name: str):
        try:
            # Define the collection where the data will be stored
            collection = self.__db[collection_name]

            # Delete the data that matches the username
            collection.delete_one({field: field_value})

            # Return the data that was found
            return True
        except Exception as e:
            logging.error(f"Failed to delete data: {e}")
            return False

    def append_entity_to_array(
        self,
        field: str,
        field_value: str,
        array_field: str,
        data: Dict[str, int],
        collection_name: str,
    ):
        try:
            # Define the collection where the data will be stored
            collection = self.__db[collection_name]

            # Append the data to the array
            collection.update_one({field: field_value}, {"$push": {array_field: data}})

            # Return the data that was stored
            return True
        except Exception as e:
            logging.error(f"Failed to append data: {e}")
            return False

    def update_single_document(
        self,
        field: str,
        field_value: str,
        data: Dict[str, Any],
        collection_name: str,
    ):
        try:
            # Define the collection where the data will be stored
            collection = self.__db[collection_name]

            # Define the filter to find the document to update
            filter = {field: field_value}

            # Define the new values for the document
            new_values = {"$set": data}

            # Update the document
            result = collection.update_one(filter, new_values)

            # Check if the document was updated
            if result.modified_count == 0:
                return False

            # Return True to indicate success
            return True
        except Exception as e:
            logging.error(f"Failed to update data: {e}")
            return False

    def update_single_document_(
        self,
        filter_key: str,
        filter_value: str,
        update_data: dict,
        collection_name: str,
    ):
        try:
            # Define the collection where the data will be updated
            collection = self.__db[collection_name]

            # Update the document in the collection
            collection.update_one({filter_key: filter_value}, {"$set": update_data})

            # Return the updated data
            return update_data
        except Exception as e:
            logging.error(f"Failed to update data: {e}")
            return None

    def find_all_documents_from_field(
        self, field: str, field_value: str, collection_name: str
    ):
        # Create an empty list to store the data that will be found
        all_pdfs_of_user = []
        try:

            # Define the collection where the data will be stored
            collection = self.__db[collection_name]

            # Find all the data that matches the username
            pdf_data = collection.find({field: field_value})

            for item in pdf_data:
                item["_id"] = str(item["_id"])
                all_pdfs_of_user.append(item)

            # Return the data that was found
            return all_pdfs_of_user
        except Exception as e:
            return None
