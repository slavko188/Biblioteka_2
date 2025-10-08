from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    # 🔹 Osnovne postavke
    APP_NAME: str = "📚 Biblioteka API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # 🔹 URL baze (npr. SQLite lokalno)
    DATABASE_URL: str = "sqlite:///./biblioteka.db"

    # 🔹 Dozvoljeni frontend URL-ovi (CORS)
    FRONTEND_URLS: List[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]

    # Ako hoćeš samo jedan URL, koristi ovo:
    FRONTEND_URL: str = "http://localhost:5173"

    # 🔹 Port i host za Uvicorn (možeš koristiti u main.py)
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


# 🧩 Instanca konfiguracije
settings = Settings()

# Ako želiš brzi pristup iz drugih modula:
FRONTEND_URL = settings.FRONTEND_URL
