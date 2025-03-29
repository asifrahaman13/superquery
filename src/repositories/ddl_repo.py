import sqlite3
import mysql
import psycopg2


class DDLRepo:
    def __init__(self):
        pass

    @classmethod
    def get_ddl_commands(cls, db_type: str, connecting_string: str) -> str:
        print("sdfasdfasdfasdfsda")
        print(db_type)
        print(connecting_string)
        if db_type == "postgres":
            print("Postgres on the way")
            return DDLRepo.psql_ddl(connecting_string)
        elif db_type == "sqlite":
            return DDLRepo.sqlite_ddl(connecting_string)
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
                f"""
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
