from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import anthropic
import pymssql

load_dotenv()

app = Flask(__name__)

# Configure Anthropic API client
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Client(api_key=anthropic_api_key)
MODEL_NAME = "claude-3-opus-20240229"

# Configure database connection
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

# Define a function to get the database schema
def get_schema():
    try:
        conn = pymssql.connect(server=db_host, user=db_user, password=db_password, database=db_name)
        print("Verbindung erfolgreich hergestellt")
    except pymssql.Error as e:
        print(f"Fehler bei der Verbindungsherstellung: {e}")
        return None

    cursor = conn.cursor(as_dict=True)

    # Get a list of all tables in the database
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'dbo'")
    tables = cursor.fetchall()

    # Iterate through each table to get its schema
    schema_str = ""
    for table in tables:
        table_name = table['table_name']
        cursor.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}'")
        columns = cursor.fetchall()

        # Construct the CREATE TABLE statement for each table
        table_schema_str = f"CREATE TABLE {table_name} (\n"
        table_schema_str += ",\n".join([f"{col['column_name']} {col['data_type']}" for col in columns])
        table_schema_str += "\n);"

        schema_str += table_schema_str + "\n\n"  # Concatenate all table schemas

    conn.close()
    return schema_str

# Define a function to send a query to Claude and get the response
def ask_claude(query, schema_str):
    prompt = f"""Here are the schemas for the database tables:

{schema_str}

Given these schemas, can you output a SQL query to answer the following question? Only output the SQL query and nothing else.

Hinweis:
Falls du gefragt wirst alle Tabellen anzuzeigen, kannst du folgende SQL-Abfrage verwenden: SELECT name FROM sys.tables;
"SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'; hat nicht funktioniert. Ich möchte alle Tabellen sehen, die in dieser Datenbank vorhanden sind." funktioniert nicht!

Question: {query}
"""

    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2048,
        messages=[{
            "role": 'user', "content":  prompt
        }]
    )
    return response.content[0].text

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        question = request.form["question"]
        schema_str = get_schema()
        if schema_str:
            sql_query = ask_claude(question, schema_str)
            try:
                conn = pymssql.connect(server=db_host, user=db_user, password=db_password, database=db_name)
                cursor = conn.cursor(as_dict=True)
                cursor.execute(sql_query)
                results = cursor.fetchall()
                conn.close()
            except Exception as e:
                results = [{"error": str(e)}]
            return render_template("home.html", question=question, sql_query=sql_query, results=results)
        else:
            return render_template("home.html", error="Fehler bei der Verbindungsherstellung zur Datenbank")

    return render_template("home.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
