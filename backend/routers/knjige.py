from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from models.models import Knjiga as KnjigaModel
from schemas.schemas import KnjigaRead, KnjigaCreate
from databases.database import get_db

# router = APIRouter(prefix="/knjige", tags=["Knjige"])
router = APIRouter(tags=["Knjige"])


# 🟢 1. Dohvati sve knjige
@router.get("/", response_model=List[KnjigaRead])
def get_knjige(db: Session = Depends(get_db)):
    knjige = db.query(KnjigaModel).all()
    return knjige


# 🟢 2. Dohvati jednu knjigu po ID-u
@router.get("/{knjiga_id}", response_model=KnjigaRead)
def get_knjiga(knjiga_id: int, db: Session = Depends(get_db)):
    knjiga = db.query(KnjigaModel).filter(KnjigaModel.id == knjiga_id).first()
    if not knjiga:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Knjiga nije pronađena")
    return knjiga


# 🟢 3. Dodaj novu knjigu
@router.post("/", response_model=KnjigaRead, status_code=status.HTTP_201_CREATED)
def create_knjiga(knjiga: KnjigaCreate, db: Session = Depends(get_db)):
    print("Payload iz frontenda:", knjiga) 
    nova_knjiga = KnjigaModel(**knjiga.model_dump())
    db.add(nova_knjiga)
    db.commit()
    db.refresh(nova_knjiga)
    return nova_knjiga


# 🟢 4. Ažuriraj postojeću knjigu
@router.put("/{knjiga_id}", response_model=KnjigaRead)
def update_knjiga(knjiga_id: int, knjiga_data: KnjigaCreate, db: Session = Depends(get_db)):
    knjiga = db.query(KnjigaModel).filter(KnjigaModel.id == knjiga_id).first()
    if not knjiga:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Knjiga nije pronađena")

    for key, value in knjiga_data.model_dump().items():
        setattr(knjiga, key, value)

    db.commit()
    db.refresh(knjiga)
    return knjiga


# 🟢 5. Obriši knjigu
@router.delete("/{knjiga_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_knjiga(knjiga_id: int, db: Session = Depends(get_db)):
    knjiga = db.query(KnjigaModel).filter(KnjigaModel.id == knjiga_id).first()
    if not knjiga:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Knjiga nije pronađena")

    db.delete(knjiga)
    db.commit()
    return None
