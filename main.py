from neo4j import GraphDatabase


class DDLRepo:
    def __init__(self):
        pass

    @classmethod
    def neo4j_ddl(cls, connecting_string: str) -> list[str]:
        # Extract credentials from the connection string manually
        uri = "neo4j+s://8cbcaf0e.databases.neo4j.io"
        username = "neo4j"
        password = "gn1pvhJFWsYNV79ZUK1rzyIQbd-P0gmuk0xVMcVjT1U"

        # Create Neo4j driver with authentication
        driver = GraphDatabase.driver(uri, auth=(username, password))

        results: list[str] = []

        with driver.session() as session:
            # Get all labels (similar to tables in RDBMS)
            result = session.run("CALL db.labels()")
            labels = [record[0] for record in result]

            for label in labels:
                print(f"Fetching schema for label: {label}")

                # Fetch node property schema
                schema_result = session.run(
                    """
                    CALL db.schema.nodeTypeProperties()
                    YIELD nodeType, propertyName, propertyTypes
                    WITH *
                    WHERE nodeType = $label
                    RETURN propertyName, propertyTypes
                    """,
                    {"label": label},
                )

                schema_properties = []
                for record in schema_result:
                    property_name = record["propertyName"]
                    property_type = ", ".join(
                        record["propertyTypes"]
                    )  # Convert list to string
                    schema_properties.append(f"{property_name}: {property_type}")

                # Construct the DDL statement
                ddl_statement = (
                    f"CREATE (: {label} {{{', '.join(schema_properties)}}});"
                )
                results.append(ddl_statement)

        driver.close()
        return results


# Run the function and print the DDL statements
ddl_statements = DDLRepo.neo4j_ddl(
    "neo4j+s://neo4j:gn1pvhJFWsYNV79ZUK1rzyIQbd-P0gmuk0xVMcVjT1U@8cbcaf0e.databases.neo4j.io"
)
for ddl in ddl_statements:
    print(ddl)
