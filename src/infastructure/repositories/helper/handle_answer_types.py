import asyncio
from src.internal.entities.router_models import QueryResponse
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain.chains import create_sql_query_chain
from operator import itemgetter


class HandleAnswerTypes:
    async def _handle_plain_answer(self, user_query: str, connection_string: str):
        await asyncio.sleep(0)
        yield QueryResponse(message="Querying the database", status=True)
        await asyncio.sleep(0)
        db = SQLDatabase.from_uri(connection_string)
        llm = ChatOpenAI(model="gpt-4", temperature=0)

        execute_query = QuerySQLDataBaseTool(db=db)
        write_query = create_sql_query_chain(llm, db)

        answer_prompt = PromptTemplate.from_template(
            """Given the following user question, corresponding SQL query, and SQL result, answer the user question.

            Question: {question}
            SQL Query: {query}
            SQL Result: {result}
            Answer: """
        )

        answer = answer_prompt | llm | StrOutputParser()
        chain = (
            RunnablePassthrough.assign(query=write_query).assign(
                result=itemgetter("query") | execute_query
            )
            | answer
        )

        response = chain.invoke({"question": user_query})
        print(response)
        await asyncio.sleep(0)
        yield QueryResponse(message=response, answer_type="plain_answer", status=False)
        await asyncio.sleep(0)

    async def _handle_bar_chart(self, user_query: str, connection_string: str):
        await asyncio.sleep(0)
        yield QueryResponse(message="Querying the database", status=True)
        await asyncio.sleep(0)
        db = SQLDatabase.from_uri(connection_string)
        llm = ChatOpenAI(model="gpt-4", temperature=0)

        execute_query = QuerySQLDataBaseTool(db=db)
        write_query = create_sql_query_chain(llm, db)

        answer_prompt = PromptTemplate.from_template(
            """Given the following user question, corresponding SQL query, and SQL result. Frame the answer in the form of a bar chart. Your response should be the following format:

                List of dictionaries where each dictionary has the x and y values as keys. The x value should be the primary key/unique key in the form of string and the y value should be the value of the column.

                Frame your answer from the sql result only and your output should be only in the above JSON format.

                Question: {question}
                SQL Query: {query}
                SQL Result: {result}
                Answer: """
        )

        answer = answer_prompt | llm | StrOutputParser()
        chain = (
            RunnablePassthrough.assign(query=write_query).assign(
                result=itemgetter("query") | execute_query
            )
            | answer
        )

        response = chain.invoke({"question": user_query})
        print("############################# The final response", response)
        await asyncio.sleep(0)
        yield QueryResponse(message=response, answer_type="bar_chart", status=False)
        await asyncio.sleep(0)

    async def _handle_line_chart(self, user_query: str, connection_string: str):
        await asyncio.sleep(0)
        yield QueryResponse(message="Querying the database", status=True)
        await asyncio.sleep(0)
        db = SQLDatabase.from_uri(connection_string)
        llm = ChatOpenAI(model="gpt-4", temperature=0)

        execute_query = QuerySQLDataBaseTool(db=db)
        write_query = create_sql_query_chain(llm, db)

        answer_prompt = PromptTemplate.from_template(
            """Given the following user question, corresponding SQL query, and SQL result. Frame the answer in the form of a line chart. Your response should be the following format:

                List of dictionaries where the key represents the label and the values are list of another dictionaries where they are (x, y) x and y values represents the the data points.

                Frame your answer from the sql result only and your output should be only in the above JSON format.

                Question: {question}
                SQL Query: {query}
                SQL Result: {result}
                Answer: """
        )

        answer = answer_prompt | llm | StrOutputParser()
        chain = (
            RunnablePassthrough.assign(query=write_query).assign(
                result=itemgetter("query") | execute_query
            )
            | answer
        )

        response = chain.invoke({"question": user_query})
        print("############################# The final response", response)
        await asyncio.sleep(0)
        yield QueryResponse(message=response, answer_type="line_chart", status=False)
        await asyncio.sleep(0)

    async def _handle_pie_chart(self, user_query: str, connection_string: str):
        await asyncio.sleep(0)
        yield QueryResponse(message="Querying the database", status=True)
        await asyncio.sleep(0)
        db = SQLDatabase.from_uri(connection_string)
        llm = ChatOpenAI(model="gpt-4", temperature=0)

        execute_query = QuerySQLDataBaseTool(db=db)
        write_query = create_sql_query_chain(llm, db)

        answer_prompt = PromptTemplate.from_template(
            """Given the following user question, corresponding SQL query, and SQL result. Frame the answer in the form of a pie chart. Your response should be the following format:

                List of dictionaries where the key represents the label and the value is the percent share of the label data points. they label should be the key and the value of the key should be the percentage share of the data points.

                Frame your answer from the sql result only and your output should be only in the above JSON format.

                Question: {question}
                SQL Query: {query}
                SQL Result: {result}
                Answer: """
        )

        answer = answer_prompt | llm | StrOutputParser()
        chain = (
            RunnablePassthrough.assign(query=write_query).assign(
                result=itemgetter("query") | execute_query
            )
            | answer
        )

        response = chain.invoke({"question": user_query})
        print("############################# The final response", response)
        await asyncio.sleep(0)
        yield QueryResponse(message=response, answer_type="pie_chart", status=False)
        await asyncio.sleep(0)