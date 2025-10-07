from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from models.models import Autor as AutorModel
from schemas.schemas import AutorRead, AutorCreate
from databases.database import get_db

router = APIRouter(prefix="/autori", tags=["Autori"])

@router.post("/", response_model=AutorRead)
def create_autor(autor: AutorCreate, db: Session = Depends(get_db)):
    novi_autor = AutorModel(**autor.dict())
    db.add(novi_autor)
    db.commit()
    db.refresh(novi_autor)
    return novi_autor

@router.get("/", response_model=List[AutorRead])
def get_autori(db: Session = Depends(get_db)):
    return db.query(AutorModel).all()
