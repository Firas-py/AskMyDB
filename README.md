📊 ASKMYDB  
=======================

AI-powered question answering for your MySQL database using natural language.

🌐 LIVE DEMO: askmydb.streamlit.app

🚀 QUICK START
--------------
1. Install: pip install -r requirements.txt  
2. Configure: Update your `.env` file with settings below  
3. Run: streamlit run app.py

📖 HOW TO USE
-------------
1. Optional: Check "Show Database Schema" to see tables and columns  
2. Type a question about your data in natural language  
3. Click "Get Answer"  
4. View the generated SQL query, query results, and AI explanation

✨ FEATURES
-----------
- Natural language questions → SQL queries  
- Executes queries safely against your MySQL database  
- Shows query results in a table  
- Explains results in plain English  
- Optional database schema preview

⚙️ .ENV CONFIGURATION
---------------------
- DB_USER=your_db_user  
- DB_PASS=your_db_password  
- DB_HOST=your_db_host  
- DB_PORT=3306  
- DB_NAME=your_db_name  
- OPENROUTER_API_KEY=your_api_key_here  
- DEEPSEEK_MODEL=deepseek/deepseek-chat-v3.1:free

🔧 TROUBLESHOOTING
------------------
- No results returned: Check your SQL permissions and database connection  
- Invalid DB connection: Verify `.env` credentials and host/port  
- API errors: Verify OpenRouter API key in `.env`  
- SQL errors: Ensure the generated SQL matches your database schema
