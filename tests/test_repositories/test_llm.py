import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from src.repositories.llm_response import LlmResponse
from src.model import AIResponse, Databases


@pytest.mark.asyncio
@patch("src.repositories.llm_response.Utils.format_ddl_and_examples")
@patch("src.repositories.llm_response.instructor.from_anthropic")
async def test_bulk_llm_response_mysql(mock_from_anthropic, mock_format):
    mock_client = MagicMock()
    mock_create = AsyncMock()
    mock_response = AIResponse(
        sql_query="```sql\nSELECT * FROM users;```", raw_response="Raw LLM Response"
    )
    mock_create.messages.create = AsyncMock(return_value=mock_response)
    mock_client.messages = mock_create
    mock_from_anthropic.return_value = mock_client

    mock_format.return_value = ("DDL", "Examples")

    llm = LlmResponse(anthropic_client="dummy_client", model="claude-3-opus")

    messages = [{"role": "user", "content": "Get all users"}]
    ddl_commands = ["CREATE TABLE users (id INT);"]
    examples = [{"input": "get users", "output": "SELECT * FROM users"}]
    db_type = Databases.MYSQL.value

    raw_response, sql_query = await llm.bulk_llm_response(
        messages, ddl_commands, examples, db_type
    )

    mock_format.assert_called_once()
    mock_create.create.assert_awaited_once()
    assert raw_response == "Raw LLM Response"
    assert sql_query == "SELECT * FROM users;"


@pytest.mark.asyncio
@patch("src.repositories.llm_response.Utils.format_ddl_and_examples")
@patch("src.repositories.llm_response.instructor.from_anthropic")
async def test_bulk_llm_response_unknown_db(mock_from_anthropic, mock_format):
    llm = LlmResponse(anthropic_client="dummy_client", model="claude-3-opus")
    response = await llm.bulk_llm_response([], [], [], "UNKNOWN_DB")
    assert response == "No response"


@pytest.mark.asyncio
@patch("src.repositories.llm_response.Utils.format_ddl_and_examples")
@patch("src.repositories.llm_response.instructor.from_anthropic")
async def test_bulk_llm_response_mysql(mock_from_anthropic, mock_format):
    # Arrange
    mock_messages = MagicMock()
    mock_response = AIResponse(
        sql_query="```sql\nSELECT * FROM users;```", raw_response="Raw LLM Response"
    )
    mock_messages.create = AsyncMock(return_value=mock_response)

    mock_client = MagicMock()
    mock_client.messages = mock_messages
    mock_from_anthropic.return_value = mock_client

    mock_format.return_value = ("DDL", "Examples")

    llm = LlmResponse(anthropic_client="dummy_client", model="claude-3-opus")

    messages = [{"role": "user", "content": "Get all users"}]
    ddl_commands = ["CREATE TABLE users (id INT);"]
    examples = [{"input": "get users", "output": "SELECT * FROM users"}]
    db_type = Databases.MYSQL.value

    raw_response, sql_query = await llm.bulk_llm_response(
        messages, ddl_commands, examples, db_type
    )

    mock_format.assert_called_once()
    mock_messages.create.assert_awaited_once()
    assert raw_response == "Raw LLM Response"
    assert sql_query == "SELECT * FROM users;"
