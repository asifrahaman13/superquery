import json
import logging
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from config.config import OPEN_AI_API_KEY
from src.internal.entities.router_models import AnswerFormat
from langchain_openai import ChatOpenAI


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
                    3. line_chart.
                    4. pie_chart.

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
