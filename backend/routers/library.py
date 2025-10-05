from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud.library import napravi_autora, svi_autori, napravi_knjigu, sve_knjige
from schemas.library import AutorCreate, Autor, KnjigaCreate, Knjiga
from databases.database import SessionLocal

router = APIRouter()

# Dependency za DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# AUTORI
@router.post("/autori/", response_model=Autor)
def dodaj_autora(autor: AutorCreate, db: Session = Depends(get_db)):
    return napravi_autora(db, autor)


@router.get("/autori/", response_model=list[Autor])
def svi_autori_endpoint(db: Session = Depends(get_db)):
    return svi_autori(db)


# KNJIGE
@router.post("/knjige/", response_model=Knjiga)
def dodaj_knjigu(knjiga: KnjigaCreate, db: Session = Depends(get_db)):
    return napravi_knjigu(db, knjiga)


@router.get("/knjige/", response_model=Knjiga)
def sve_knjige(db: Session = Depends(get_db)):
    return sve_knjige(db)
