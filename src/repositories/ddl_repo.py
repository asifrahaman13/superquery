import sqlite3
import mysql
from neo4j import GraphDatabase
import psycopg2

from ..model.products import Databases


class DDLRepo:
    def __init__(self):
        pass

    @classmethod
    def get_ddl_commands(cls, db_type: str, connecting_string: str) -> str:
        if db_type == Databases.POSTGRES.value:
            return DDLRepo.psql_ddl(connecting_string)
        if db_type == Databases.MYSQL.value:
            return DDLRepo.mysql_ddl(connecting_string)
        elif db_type == Databases.SQLITE.value:
            return DDLRepo.sqlite_ddl(connecting_string)
        elif db_type == Databases.NEO4J.value:
            return DDLRepo.neo4j_ddl(connecting_string)
        else:
            raise ValueError(f"Unsupported database type: {db_type}")

    @classmethod
    def psql_ddl(cls, connecting_string: str) -> str:
        conn = psycopg2.connect(connecting_string)
        cur = conn.cursor()

        # Get all user-defined tables in public schema
        cur.execute("""
                SELECT tablename FROM pg_catalog.pg_tables
                WHERE schemaname = 'public';
            """)
        tables = cur.fetchall()

        results: list[str] = []

        for table in tables:
            table_name = table[0]
            print(f"DDL for table: {table_name}")

            # Construct DDL statement
            cur.execute(
                """
                    SELECT 'CREATE TABLE ' || quote_ident(schemaname) || '.' || quote_ident(tablename) || ' (' ||
                    array_to_string(
                        ARRAY(
                            SELECT quote_ident(attname) || ' ' || format_type(atttypid, atttypmod)
                            FROM pg_attribute
                            WHERE attrelid = (schemaname || '.' || tablename)::regclass
                            AND attnum > 0
                            ORDER BY attnum
                        ), ', '
                    ) || ');'
                    FROM pg_tables
                    WHERE tablename = %s;
                """,
                (table_name,),
            )

            ddl = cur.fetchone()

            # Store the DDL in the results list
            results.append(ddl[0] if ddl and ddl[0] else None)

        cur.close()
        conn.close()

        return results

    @classmethod
    def sqlite_ddl(cls, connecting_string: str) -> str:
        # Connect to the SQLite database
        conn = sqlite3.connect(connecting_string)
        cur = conn.cursor()

        # Query to get all table names
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cur.fetchall()

        results: list[str] = []

        for table in tables:
            table_name = table[0]
            print(f"DDL for table: {table_name}")

            # Fetch DDL (schema) for the table
            cur.execute(
                "SELECT sql FROM sqlite_master WHERE type='table' AND name=?;",
                (table_name,),
            )
            ddl = cur.fetchone()

            # Store the DDL in the results list
            results.append(ddl[0] if ddl and ddl[0] else None)

        # Close connection
        cur.close()
        conn.close()

        return results

    @classmethod
    def mysql_ddl(cls, connecting_string: str) -> str:
        user, rest = connecting_string.split(":", 1)
        password, rest = rest.split("@", 1)
        host, database = rest.split("/")

        conn = mysql.connector.connect(
            user=user, password=password, host=host, database=database
        )
        cur = conn.cursor()

        cur.execute("SHOW TABLES;")
        tables = cur.fetchall()

        results: list[str] = []

        for table in tables:
            table_name = table[0]
            print(f"DDL for table: {table_name}")

            cur.execute(f"SHOW CREATE TABLE `{table_name}`;")
            ddl = cur.fetchone()
            results.append(ddl[1] if ddl and ddl[1] else None)

        cur.close()
        conn.close()

        return results

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
                print(f"Schema for label: {label}")

                # Fetch schema constraints and indexes
                schema_result = session.run(
                    f"CALL db.schema.nodeTypeProperties() YIELD nodeType, propertyName, propertyTypes WHERE nodeType = '{label}'"
                )

                schema = [
                    f"{record['propertyName']} {record['propertyTypes']}"
                    for record in schema_result
                ]
                ddl_statement = f"CREATE (: {label} {{{', '.join(schema)}}});"
                results.append(ddl_statement)

        driver.close()
        return results
