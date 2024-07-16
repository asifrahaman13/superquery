class LlmResponse:
    def __init__(self, open_ai_client) -> None:
        self.client = open_ai_client

    def embed_text(self, text, model_name):
        response = self.client.embeddings.create(model=model_name, input=text)
        return response.data[0].embedding

    def bulk_llm_response(self, query: str, db_type: str):

        if db_type == "sqlite":
            completion = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": """You are a master in sqlite query. You are going to help me with generating sqlite query from the natural langauge. I will provide you the natural language query and you will convert it into sqlite query. Take care of all the details of the user query. Each small information of the user query matters. Depending upon that generate accurate sql query for sqlite.\n
             
    We have three tables. They are created with the following SQL commands:\n

    CREATE TABLE companies (id INTEGER NOT NULL PRIMARY KEY,company_logo_url TEXT,company_logo_text TEXT,company_name TEXT,relation_to_event TEXT,event_url TEXT,company_revenue TEXT,n_employees TEXT,company_phone TEXT,company_founding_year TEXT,company_address TEXT,company_industry TEXT,company_overview TEXT,homepage_url TEXT,linkedin_company_url TEXT,homepage_base_url TEXT,company_logo_url_on_event_page TEXT,company_logo_match_flag TEXT);\n
             
    CREATE TABLE events (id INTEGER NOT NULL PRIMARY KEY,event_logo_url TEXT,event_name TEXT,event_start_date TEXT,event_end_date TEXT,event_venue TEXT,event_country TEXT,event_description TEXT,event_url TEXT);\n
             
    CREATE TABLE people (id INTEGER NOT NULL PRIMARY KEY,first_name TEXT, middle_name TEXT,last_name TEXT,job_title TEXT,person_city TEXT,person_state TEXT,person_country TEXT,email_pattern TEXT,homepage_base_url TEXT,duration_in_current_job TEXT,duration_in_current_company TEXT);\n
             
    Give me the SQL query corresonspoing to the user prompt. Example.
             
    1. 
    User prompt: Find me events that companies in Pharmaceuticals sector are attending
    SQL query: ```sql
                SELECT e.*
                FROM events e
                INNER JOIN companies c ON e.event_url = c.event_url
                WHERE LOWER(c.company_industry) LIKE '%pharmaceutical%';```\n
             
    2. User prompt: Find me companies that are attending Oil & Gas related events over the next 12 months
    SQL query:  ```sql
                SELECT DISTINCT c.company_name
                FROM companies c
                INNER JOIN events e ON c.event_url = e.event_url
                WHERE LOWER(c.company_industry) LIKE '%oil%' AND LOWER(c.company_industry) LIKE '%gas%'
                AND (e.event_start_date >= DATE('now') AND e.event_start_date <= DATE('now', '+5 months'));```\n
    3. User prompt: Find sales people for companies that are attending events in Singapore over the next 9 months.
    SQL query:  ```sql
                SELECT DISTINCT p.*
                FROM people p
                INNER JOIN companies c ON p.homepage_base_url = c.homepage_base_url
                INNER JOIN events e ON c.event_url = e.event_url
                WHERE LOWER(c.company_address) LIKE '%singapore%'
                AND (e.event_start_date >= DATE('now') AND e.event_start_date <= DATE('now', '+6 months'))
                AND LOWER(p.job_title) LIKE '%sales%';```\n
    4. User prompt: I need the email addresses of people working for companies that are attending finance and banking events
    SQL query:  ```sql
                SELECT first_name
                FROM people p
                INNER JOIN companies c ON p.homepage_base_url = c.homepage_base_url
                INNER JOIN events e ON c.event_url = e.event_url
                WHERE LOWER(c.company_industry) LIKE '%finance%' OR LOWER(c.company_industry) LIKE '%banking%';```\n
    5. User prompt: Find first 10 entries for first name and profession of the people for companies that are attending events in Singapore over the next 12 months and who are Engineer by job title
    SQL query: ```sql
              SELECT p.first_name, p.job_title
              FROM people p
              INNER JOIN companies c ON p.homepage_base_url = c.homepage_base_url
              INNER JOIN events e ON c.event_url = e.event_url
              WHERE e.event_country = 'Singapore'
              AND (e.event_start_date >= DATE('now') AND e.event_start_date <= DATE('now', '+12 months'))
              AND LOWER(p.job_title) LIKE '%engineer%'
              LIMIT 10;```\n

             Give only the sql command. Do not give any other text or information. Remember to take care of all the details of the user query. Each small information of the user query matters. Depending upon that generate accurate sql query for sqlite.
             """,
                    },
                    {"role": "user", "content": query},
                ],
            )
            return completion.choices[0].message.content.strip("```sql\n").strip("```")

        if db_type == "pinecone":
            completion = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": f"""You are a helpful assistant who is pro at pinecone vector semantic search. You have been asked to provide a response. You have the semantic search result from the source. You need to to check the result from the semantic search of the pinecone and give the result as per the query of the user in a natural language. The data source from which you need to answer is: \n
                       
                      """,
                    },
                    {"role": "user", "content": query},
                ],
            )
            return completion.choices[0].message.content
        elif db_type == "qdrant":
            completion = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": f"""You are a helpful assistant who is pro at qdrant vector semantic search. You have been asked to provide a response. You have the semantic search result from the source. You need to to check the result from the semantic search of the qdrant and give the result as per the query of the user in a natural language. The data source from which you need to answer is: \n
                
                      """,
                    },
                    {"role": "user", "content": query},
                ],
            )
            return completion.choices[0].message.content
        else:
            return "No response"
