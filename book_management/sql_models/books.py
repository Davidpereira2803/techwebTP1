from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, ForeignKey, Integer

from book_management.database import Base

class Book(Base):
    __tablename__ = "books"

    name = mapped_column(String(72))
    id = mapped_column(String(72), primary_key=True)
    author = mapped_column(String(72))
    editor : Mapped[Optional[str]] = mapped_column(String(2048), nullable=True)
    price = mapped_column(String(72))
   
    owner_email : Mapped[String(72)]= mapped_column(ForeignKey("users.email"))
    owner: Mapped["User"] = relationship()

    status = mapped_column(String(72))