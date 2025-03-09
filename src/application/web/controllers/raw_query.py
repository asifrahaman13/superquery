from fastapi import APIRouter, Depends, HTTPException, Header
from src.constants.databases.database_service_mapping import QueryServiceMapping
from src.exports.index import (
    get_auth_service,
    get_mysql_query_database_service,
    get_neo4j_query_database_service,
    get_pinecone_query_database_service,
    get_postgres_query_database_service,
    get_qdrant_query_database_service,
    get_sqlite_query_database_service,
)
from src.entities.router_models import QueryBase
from src.use_cases.auth_service import AuthService
from src.use_cases.query_service import QueryService

raw_query_controller = APIRouter()


@raw_query_controller.post("/raw-query")
async def raw_query(
    query: QueryBase,
    token: str = Header(..., alias="Authorization"),
    auth_service: AuthService = Depends(get_auth_service),
    mysql_query_service: QueryService = Depends(get_mysql_query_database_service),
    postgres_query_service: QueryService = Depends(get_postgres_query_database_service),
    sqlite_query_service: QueryService = Depends(get_sqlite_query_database_service),
    pinecone_query_service: QueryService = Depends(get_pinecone_query_database_service),
    qdrant_query_service: QueryService = Depends(get_qdrant_query_database_service),
    neo4j_query_service: QueryService = Depends(get_neo4j_query_database_service),
):
    db_service_mapping = QueryServiceMapping.get_mapping(
        mysql_query_service,
        postgres_query_service,
        sqlite_query_service,
        pinecone_query_service,
        qdrant_query_service,
        neo4j_query_service,
    )

    try:
        user = auth_service.user_info(token.split(" ")[1])
        if user is None:
            raise HTTPException(status_code=401, detail="Authentication failed")

        service, response_type = db_service_mapping.get(query.db_type, (None, None))
        if not service:
            raise HTTPException(
                status_code=400, detail=f"Unsupported database type: {query.db_type}"
            )

        response = await service.general_raw_query(
            user["sub"], query.raw_query, query.db_type
        )
        return {"response": response, "response_type": response_type}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
