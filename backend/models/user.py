from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from databases.database import Base  # <-- import iz databases foldera

class Autor(Base):
    __tablename__ = "autori"

    id = Column(Integer, primary_key=True, index=True)
    ime = Column(String, index=True)
    prezime = Column(String, index=True)

    knjige = relationship("Knjiga", back_populates="autor")


class Knjiga(Base):
    __tablename__ = "knjige"

    id = Column(Integer, primary_key=True, index=True)
    naslov = Column(String, index=True)
    isbn = Column(String, unique=True, index=True)
    godina_izdanja = Column(Integer)
    dostupna = Column(Boolean, default=True)

    autor_id = Column(Integer, ForeignKey("autori.id"))
    autor = relationship("Autor", back_populates="knjige")
