# config.py
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
LEONARDO_API_KEY = os.getenv("LEONARDO_API_KEY")
AMBIENTE = os.getenv("AMBIENTE")

