from sqlalchemy.orm import Session
from models.user import Autor, Knjiga
from schemas.library import AutorCreate, KnjigaCreate

def napravi_autora(db: Session, autor: AutorCreate):
    db_autor = Autor(**autor.dict())
    db.add(db_autor)
    db.commit()
    db.refresh(db_autor)
    return db_autor

def svi_autori(db: Session):
    return db.query(Autor).all()

def napravi_knjigu(db: Session, knjiga: KnjigaCreate):
    db_knjiga = Knjiga(**knjiga.dict())
    db.add(db_knjiga)
    db.commit()
    db.refresh(db_knjiga)
    return db_knjiga

def sve_knjige(db: Session):
    return db.query(Knjiga).all()
