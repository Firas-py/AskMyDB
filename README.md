📊 AskMyDB

AI-powered question answering for your MySQL database using natural language.

🌐 LIVE DEMO: (Optional: Add your Streamlit app link here)

🚀 Quick Start

Install dependencies
pip install -r requirements.txt

Configure
Create a .env file in the project root with your settings:
DB_USER=your_db_user
DB_PASS=your_db_password
DB_HOST=your_db_host
DB_PORT=3306
DB_NAME=your_db_name
OPENROUTER_API_KEY=your_api_key_here
DEEPSEEK_MODEL=deepseek/deepseek-chat-v3.1:free

Run the app
streamlit run app.py

📖 How to Use

Open the app in your browser.

Optional: Check Show Database Schema to see tables and columns.

Type a question about your data in natural language.

Click Get Answer.

View the generated SQL query, query results, and AI explanation.

✨ Features

Natural language questions → SQL queries

Executes queries safely against your MySQL database

Shows query results in a table

Explains results in plain English

Optional database schema preview

⚙️ .ENV Configuration
Variable	Description
DB_USER	Database username
DB_PASS	Database password
DB_HOST	Database host (with port if needed)
DB_PORT	Database port (default 3306)
DB_NAME	Database name
OPENROUTER_API_KEY	OpenRouter API key for AI SQL generation
DEEPSEEK_MODEL	DeepSeek model (default: deepseek/deepseek-chat-v3.1:free)
🔧 Troubleshooting

No results returned: Check your SQL permissions and database connection.

Invalid DB connection: Verify .env credentials and host/port.

API errors: Verify OpenRouter API key in .env.

SQL errors: Ensure the generated SQL matches your database schema.
