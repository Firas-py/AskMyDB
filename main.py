import os
import streamlit as st
import requests
import json
import re
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from langchain_community.utilities import SQLDatabase

# ================= CONFIG =================
# Load .env locally
if os.path.exists(".env"):
    load_dotenv()

# Read secrets (Streamlit Cloud uses st.secrets)
DB_USER = os.getenv("DB_USER") or st.secrets.get("DB_USER")
DB_PASS = os.getenv("DB_PASS") or st.secrets.get("DB_PASS")
DB_HOST = os.getenv("DB_HOST") or st.secrets.get("DB_HOST")
DB_PORT = os.getenv("DB_PORT") or st.secrets.get("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME") or st.secrets.get("DB_NAME")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY") or st.secrets.get("OPENROUTER_API_KEY")
DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL") or st.secrets.get("DEEPSEEK_MODEL", "deepseek/deepseek-chat-v3.1:free")

# Build DB URI
db_uri = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
db = SQLDatabase.from_uri(db_uri)

# ================= STREAMLIT UI =================
st.set_page_config(page_title="AskMyDB", page_icon="📊")
st.title("📊 AskMyDB")
st.write("Ask questions in natural language, get answers from your MySQL database.")

# Show schema
if st.checkbox("Show Database Schema"):
    schema = db.get_table_info()
    st.code(schema, language="sql")

# ================= HELPERS =================
def query_deepseek(prompt):
    """Send prompt to DeepSeek and return content"""
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": DEEPSEEK_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
        "max_tokens": 500
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()["choices"][0]["message"]["content"]

def clean_sql_query(sql):
    """Extract clean SQL statement from LLM output"""
    sql = re.sub(r"```(?:sql)?\n([\s\S]*?)```", r"\1", sql)
    match = re.search(r"(SELECT[\s\S]*?;)", sql, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    match = re.search(r"([\s\S]*?;)", sql)
    if match:
        return match.group(1).strip()
    return sql.strip()

# ================= USER INPUT =================
question = st.text_input("Ask a question about your data:")

if st.button("Get Answer") and question:
    schema = db.get_table_info()
    prompt = f"""
You are a SQL assistant. You ONLY return SQL queries.
Do NOT include any explanation, comments, or extra text.

Here is the database schema:
{schema}

User question: {question}

SQL QUERY:
"""
    sql_query = query_deepseek(prompt)
    sql_query = clean_sql_query(sql_query)
    st.subheader("📝 Generated SQL Query")
    st.code(sql_query, language="sql")

    try:
        engine = create_engine(db_uri)
        with engine.connect() as conn:
            result = conn.execute(text(sql_query))
            rows = result.fetchall()

        st.subheader("📊 Query Results")
        if rows:
            columns = result.keys()
            data = [dict(zip(columns, row)) for row in rows]
            st.table(data)
        else:
            st.write("No results returned.")

        answer_prompt = f"""
The following SQL query was executed:

{sql_query}

It returned these results:
{rows}

Explain the answer in plain English.
"""
        answer = query_deepseek(answer_prompt)
        st.subheader("💡 Final Answer")
        st.write(answer)

    except Exception as e:
        st.error(f"❌ Error executing SQL: {e}")
