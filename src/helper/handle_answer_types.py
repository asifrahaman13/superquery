import asyncio
import json
import sqlite3
from typing import AsyncGenerator, Callable, Any
import psycopg2
import mysql.connector
from src.entities.router_models import QueryResponse
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


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
