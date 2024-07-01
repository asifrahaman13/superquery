class MongodbQueryRepository():
    def __init__(self, client, database) -> None:
        self.__client=client
        self.__database=database

    def query_database(self, query):
        return {"message":"Mongodb" + query}