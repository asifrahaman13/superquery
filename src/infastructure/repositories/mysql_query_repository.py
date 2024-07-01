from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool


class MySqlQueryRepository:
    def __init__(self) -> None:
        pass

    def query_database(self, user_query):

        db = SQLDatabase.from_uri(
            ""
        )
        llm = ChatOpenAI(model="gpt-4", temperature=0)

        execute_query = QuerySQLDataBaseTool(db=db)

        write_query = create_sql_query_chain(llm, db)
        response = write_query.invoke(
            {"question": "How many users are there in users table"}
        )

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

        return {"message": response}
