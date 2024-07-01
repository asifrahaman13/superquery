from src.internal.interfaces.services.query_interface import QueryInterface


class QueryService(QueryInterface):

    def __init__(self, query_database, database) -> None:
        self.query_database = query_database
        self.database = database

    def query_db(self, user: str, query: str, db: str) -> dict:
        if db == "mysql":
            available_mysql_client = self.database.find_single_entity_by_field_name(
                "configurations", "username", user
            )
            if available_mysql_client:
                return self.query_database.query_database(
                    query, str(available_mysql_client["mysql"]["mysqlConnectionString"])
                )

        return None
