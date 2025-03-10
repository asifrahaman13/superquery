import json
import asyncio
import sqlite3
import psycopg2
import logging
import mysql.connector
from neo4j import GraphDatabase
from typing import AsyncGenerator, Callable, Any
from src.entities.router_models import QueryResponse


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class Neo4jDriver:
    def __init__(self, connection_string: str, auth: tuple):
        self.driver = GraphDatabase.driver(connection_string, auth=auth)

    def __enter__(self):
        self.session = self.driver.session()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()
        self.driver.close()

    def query(self, query: str, parameters=None):
        if parameters is None:
            parameters = {}
        with self.session.begin_transaction() as tx:
            result = tx.run(query, parameters)
            return result.data()


class HandleAnswerTypes:
    async def handle_query(
        self,
        user_query: str,
        connection_string: str,
        connect_func: Callable[[str], Any],
    ) -> AsyncGenerator[QueryResponse, None]:
        await asyncio.sleep(0)
        yield QueryResponse(message="Querying the database", status=True)
        logging.info(f"The connecting string is....{connection_string}")
        conn = connect_func(connection_string)
        cursor = conn.cursor()
        cursor.execute(user_query)
        results = cursor.fetchall()
        headers = [desc[0] for desc in cursor.description] if cursor.description else []
        data = [dict(zip(headers, row)) for row in results]
        json_data = json.dumps(data)
        if results:
            await asyncio.sleep(0)
            yield QueryResponse(
                message=json_data,
                answer_type="table_response",
                status=False,
            )
            await asyncio.sleep(0)
            yield QueryResponse(
                sql_query=user_query, answer_type="sql_query", status=False
            )
        cursor.close()
        conn.close()

    async def handle_sqlite_query(
        self, user_query: str, connection_string: str
    ) -> AsyncGenerator[QueryResponse, None]:
        async for response in self.handle_query(
            user_query, connection_string, sqlite3.connect
        ):
            await asyncio.sleep(0)
            yield response

    async def handle_postgres_query(
        self, user_query: str, connection_string: str
    ) -> AsyncGenerator[QueryResponse, None]:
        async for response in self.handle_query(
            user_query, connection_string, psycopg2.connect
        ):
            await asyncio.sleep(0)
            yield response

    async def handle_mysql_query(
        self, user_query: str, connection_string: str
    ) -> AsyncGenerator[QueryResponse, None]:
        async for response in self.handle_query(
            user_query, connection_string, mysql.connector.connect
        ):
            await asyncio.sleep(0)
            yield response

    async def handle_neo4j_query(
        self, user_query: str, *args, **kwargs
    ) -> AsyncGenerator[QueryResponse, None]:
        await asyncio.sleep(0)
        yield QueryResponse(message="Querying the database", status=True)
        logging.info(f"The connecting string is....{kwargs}")

        api_endpoint: str = kwargs.get("api_endpoint")
        username: str = kwargs.get("username")
        neo4j_password: str = kwargs.get("neo4j_password")

        with Neo4jDriver(api_endpoint, (username, neo4j_password)) as driver:
            result = driver.query(user_query)
            json_data = json.dumps(result)
            await asyncio.sleep(0)
            yield QueryResponse(
                message=json_data,
                answer_type="table_response",
                status=False,
            )
            await asyncio.sleep(0)
            yield QueryResponse(
                sql_query=user_query, answer_type="sql_query", status=False
            )
