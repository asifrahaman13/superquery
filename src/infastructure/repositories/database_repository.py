"""
Database repository is used to interact with the MongoDB database.
It is separate entity from the rest of the program.
"""


class DatabaseRepository:
    def __init__(self, client, db_name):
        self.__client =client
        self.__db = db_name

    def query_database(self, query):
        print(self.__client, self.__db)
        return {"message":"Hello from MySQL DB" + query}