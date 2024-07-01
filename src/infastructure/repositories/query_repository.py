

class MySqlQueryRepository:
    def __init__(self) -> None:
        pass

    def query_database(self, query):
        return {"message":"sample query mysql" + query}
        
    