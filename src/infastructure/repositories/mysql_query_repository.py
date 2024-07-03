from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
import json
import logging
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from config.config import OPEN_AI_API_KEY
from pydantic import BaseModel


class AnswerFormat(BaseModel):
    answer_type: str


class FormatAssistant:
    def __init__(self):
        self.__model = "gpt-4o"
        self.__openai_api_key = OPEN_AI_API_KEY
        self.__max_tokens = 300
        self.__chat_model = ChatOpenAI(
            model=self.__model,
            openai_api_key=self.__openai_api_key,
            max_tokens=self.__max_tokens,
        )

    def process_output(self, output):

        # Extract the JSON content
        json_content = output.content.strip("```json\n").strip("```")
        try:
            return json.loads(json_content)
        except json.JSONDecodeError as e:
            logging.error(f"Failed to parse JSON: {e}")
            return None

    def format_input(self, user_query):

        # Create a prompt
        parser = PydanticOutputParser(pydantic_object=AnswerFormat)

        # Create a prompt
        prompt = ChatPromptTemplate(
            messages=[
                HumanMessagePromptTemplate.from_template(
                    """You have the user query. Your task is to analyze the user queery and decide what kind of answer would fit the result. You have the following choices:
                    Your answer should be in the form of json. Key should be answer_type. The possible values are as follows:
                    1. plain_answer.
                    2. bar_chart.
                    3. pie_chart.

                    Only give the JSON response and you are not supposed to give any other answer.

                    The user query is: {question}
                                                                     
                   """
                )
            ],
            # Define the input variables
            input_variables=["question"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        return prompt.format_prompt(question=user_query)

    def run_answer_type_assistant(self, user_query):

        # Format the input
        input_prompt = self.format_input(user_query)

        print("#################", input_prompt)

        # Invoke the model
        output = self.__chat_model.invoke(input_prompt.to_messages())

        print("#################", output)

        # Process the output
        return self.process_output(output)


class MySqlQueryRepository:
    def __init__(self) -> None:
        pass

    def query_database(self, user_query: str, connection_string: str):

        answer_type = FormatAssistant().run_answer_type_assistant(user_query)

        print("#################", answer_type)

        if answer_type["answer_type"] == "plain_answer":
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

            return {"message": response, "answer_type": "plain_answer"}
        if answer_type["answer_type"] == "bar_chart":
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

            return {"message": response, "answer_type": "bar_chart"}
