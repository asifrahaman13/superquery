import pytest

from unittest.mock import MagicMock, patch
from src.helper.handle_answer_types import HandleAnswerTypes


@pytest.mark.asyncio
async def test_handle_sqlite_query():
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [(1, "Alice"), (2, "Bob")]
    mock_cursor.description = [("id",), ("name",)]
    mock_conn = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    with patch("sqlite3.connect", return_value=mock_conn):
        handler = HandleAnswerTypes()
        responses = []
        async for response in handler.handle_sqlite_query(
            "SELECT * FROM users;", "mock_connection_string"
        ):
            responses.append(response)

    assert len(responses) == 3
    assert responses[0].message == "Querying the database"
    assert responses[1].answer_type == "table_response"
    assert responses[2].answer_type == "sql_query"


@pytest.mark.asyncio
async def test_handle_postgres_query():
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [(1, "Alice"), (2, "Bob")]
    mock_cursor.description = [("id",), ("name",)]
    mock_conn = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    with patch("psycopg2.connect", return_value=mock_conn):
        handler = HandleAnswerTypes()
        responses = []
        async for response in handler.handle_postgres_query(
            "SELECT * FROM users;", "mock_connection_string"
        ):
            responses.append(response)

    assert len(responses) == 3
    assert responses[0].message == "Querying the database"
    assert responses[1].answer_type == "table_response"
    assert responses[2].answer_type == "sql_query"


@pytest.mark.asyncio
async def test_handle_mysql_query():
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [(1, "Alice"), (2, "Bob")]
    mock_cursor.description = [("id",), ("name",)]
    mock_conn = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    with patch("mysql.connector.connect", return_value=mock_conn):
        handler = HandleAnswerTypes()
        responses = []
        async for response in handler.handle_mysql_query(
            "SELECT * FROM users;", "mock_connection_string"
        ):
            responses.append(response)

    assert len(responses) == 3
    assert responses[0].message == "Querying the database"
    assert responses[1].answer_type == "table_response"
    assert responses[2].answer_type == "sql_query"
