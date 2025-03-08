import asyncio
from neo4j import GraphDatabase
from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain_openai import ChatOpenAI
from src.internal.entities.router_models import QueryResponse


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
        print("Querying Neo4j:", query, parameters)
        with self.session.begin_transaction() as tx:
            result = tx.run(query, parameters)
            return result.data()


class Neo4jQueryRepository:
    @staticmethod
    async def query_database(query: str, *args, **kwargs):
        username = kwargs.get("username")
        password = kwargs.get("neo4j_password")
        connection_string = kwargs.get("api_endpoint")
        graph = Neo4jGraph(
            url=connection_string,
            username=username,
            password=password,
        )

        await asyncio.sleep(0)
        yield QueryResponse(
            message="Querying Neo4j", status=True, answer_type="plain_answer"
        )
        await asyncio.sleep(0)

        chain = GraphCypherQAChain.from_llm(
            ChatOpenAI(temperature=0, model="gpt-4o"), graph=graph, verbose=True
        )

        response = chain.invoke({"query": query})
        await asyncio.sleep(0)
        yield QueryResponse(
            message=response["result"], status=False, answer_type="plain_answer"
        )
        await asyncio.sleep(0)

    @staticmethod
    def general_raw_query(query: str, *args, **kwargs):
        auth = (kwargs.get("username"), kwargs.get("neo4j_password"))
        connection_string = kwargs.get("api_endpoint")
        with Neo4jDriver(connection_string, auth) as driver:
            result = driver.query(query)
            return result
