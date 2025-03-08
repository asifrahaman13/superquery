import asyncio
import json
import sqlite3
from src.internal.entities.router_models import QueryResponse


class HandleAnswerTypes:
    async def handle_plain_answer(self, user_query: str, connection_string: str):
        await asyncio.sleep(0)
        yield QueryResponse(message="Querying the database", status=True)
        await asyncio.sleep(0)
        print(f"The connecting string is....{ connection_string}")
        conn = sqlite3.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute(user_query)
        results = cursor.fetchall()
        headers = (
            [description[0] for description in cursor.description]
            if cursor.description
            else []
        )
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

            await asyncio.sleep(0)
            yield QueryResponse(
                sql_query=user_query, answer_type="sql_query", status=False
            )
            await asyncio.sleep(0)
