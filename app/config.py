import os
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

class Settings:
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")

settings = Settings()
