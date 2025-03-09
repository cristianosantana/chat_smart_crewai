import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    BASE_URL = os.getenv('BASE_URL')
    SMART_USER = os.getenv('SMART_USER')
    SMART_PASS = os.getenv('SMART_PASS')