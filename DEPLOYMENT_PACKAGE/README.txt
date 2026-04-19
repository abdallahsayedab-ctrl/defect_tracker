# Project Name: Defect Tracker Pro (Python/Postgres)

## Prerequisites
1. Python 3.10+ installed.
2. PostgreSQL 14+ database server running.
3. Gemini API Key from Google AI Studio.

## Setup Instructions:
1. Copy all files to the server.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Database Setup:
   - Create a database named `defect_db`.
   - Run the SQL code inside `schema.sql`.
4. Environment Variables:
   - Rename `config.env.example` to `.env`.
   - Fill in your DB credentials and Gemini API Key.
5. Run the Application:
   `streamlit run app.py`

## Portfolio:
- Frontend: Streamlit
- Database: PostgreSQL
- Intelligence: Google Gemini 1.5 Flash
