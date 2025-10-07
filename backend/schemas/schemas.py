from pydantic import BaseModel
from typing import Optional

class AutorBase(BaseModel):
    ime: str
    prezime: str

class AutorCreate(AutorBase):
    pass

class Autor(AutorBase):
    id: int

    model_config = {"from_attributes": True}  # <--- Pydantic V2

class KnjigaBase(BaseModel):
    naslov: str
    isbn: str
    godina_izdanja: int
    dostupna: Optional[bool] = True

class KnjigaCreate(KnjigaBase):
    autor_id: int

class Knjiga(KnjigaBase):
    id: int
    autor: Autor

    model_config = {"from_attributes": True}  # <--- Pydantic V2
