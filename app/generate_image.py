import google.generativeai as genai
import psycopg2
import json
import os
from dotenv import load_dotenv
from services.leonardo_ai import get_headers 

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

connection = psycopg2.connect(
    database="vulpix",
    host="localhost",
    user="postgres",
    password="30112004",
    port="5432"
)

cursor = connection.cursor()

cursor.execute("SELECT user_prompt FROM informacoes WHERE id = 4;")

prompt_user = cursor.fetchone()

