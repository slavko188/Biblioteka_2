from __future__ import annotations
from typing import List, Optional
from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from databases.database import Base


class Autor(Base):
    __tablename__ = "autori"

    # --- Kolone ---
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    ime: Mapped[str] = mapped_column(String(50), index=True, nullable=False)
    prezime: Mapped[str] = mapped_column(String(50), index=True, nullable=False)

    # --- Relacije ---
    knjige: Mapped[List[Knjiga]] = relationship(
        back_populates="autor",
        cascade="all, delete-orphan",
        lazy="joined"
    )

    def __repr__(self) -> str:
        return f"<Autor(id={self.id}, ime='{self.ime}', prezime='{self.prezime}')>"


class Knjiga(Base):
    __tablename__ = "knjige"

    # --- Kolone ---
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    naslov: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    isbn: Mapped[str] = mapped_column(String(30), unique=True, index=True, nullable=False)
    godina_izdanja: Mapped[int] = mapped_column(Integer, nullable=False)
    dostupna: Mapped[bool] = mapped_column(Boolean, default=True)

    # --- Relacija ka autoru ---
    autor_id: Mapped[int] = mapped_column(ForeignKey("autori.id", ondelete="CASCADE"))
    autor: Mapped[Optional[Autor]] = relationship(back_populates="knjige", lazy="joined")

    def __repr__(self) -> str:
        return f"<Knjiga(id={self.id}, naslov='{self.naslov}', isbn='{self.isbn}')>"
