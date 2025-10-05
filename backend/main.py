import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from databases.database import Base, engine
from routers import library
from core.config import FRONTEND_URL

# Kreiraj tabele u bazi
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Biblioteka API")

# CORS - dozvoljava frontend da poziva API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registracija routera
app.include_router(library.router, prefix="/biblioteka", tags=["biblioteka"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
