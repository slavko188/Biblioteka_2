from pydantic import BaseModel, Field
from typing import Optional


# ============================
# 🔹 AUTOR ŠEME
# ============================

class AutorBase(BaseModel):
    ime: str = Field(..., min_length=2, max_length=50)
    prezime: str = Field(..., min_length=2, max_length=50)


class AutorCreate(AutorBase):
    """Šema za kreiranje novog autora."""
    pass


class AutorRead(AutorBase):
    """Šema za čitanje autora iz baze."""
    id: int

    model_config = {
        "from_attributes": True
    }


# ============================
# 🔹 KNJIGA ŠEME
# ============================

class KnjigaBase(BaseModel):
    naslov: str = Field(..., min_length=1, max_length=100)
    isbn: str = Field(..., min_length=5, max_length=30)
    godina_izdanja: int = Field(..., ge=1000, le=2100)
    dostupna: bool = True


class KnjigaCreate(KnjigaBase):
    """Šema za kreiranje knjige (koristi autor_id)."""
    autor_id: int


class KnjigaRead(KnjigaBase):
    """Šema za prikaz knjige zajedno sa autorom."""
    id: int
    autor: Optional[AutorRead] = None

    model_config = {
        "from_attributes": True
    }
