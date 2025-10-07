
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from databases.database import Base, engine
from routers import knjige, autori  # <- dodaj sve rutere
from core.config import FRONTEND_URL


# ==========================================
# 🚀 FastAPI inicijalizacija
# ==========================================

app = FastAPI(
    title="📚 Biblioteka API",
    version="1.0.0",
    description="REST API za upravljanje knjigama i autorima"
)


# ==========================================
# 🌐 CORS konfiguracija
# ==========================================

origins = [FRONTEND_URL] if FRONTEND_URL else ["http://localhost:5173", "http://127.0.0.1:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================
# 🧱 Kreiranje tabela prilikom pokretanja
# ==========================================

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)
    print("✅ Tabele su uspešno kreirane (ako već ne postoje).")


# ==========================================
# 🔌 Registracija API ruta
# ==========================================

app.include_router(knjige.router, prefix="/knjige", tags=["Knjige"])
app.include_router(autori.router, prefix="/autori", tags=["Autori"])


# ==========================================
# ❤️ Health check ruta
# ==========================================

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Biblioteka API radi!"}


# ==========================================
# 🏁 Pokretanje servera
# ==========================================

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )

