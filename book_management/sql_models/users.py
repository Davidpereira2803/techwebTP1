from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean

from book_management.database import Base

class User(Base):
    __tablename__ = 'users'
    
    email: Mapped[str] = mapped_column(String(72), primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(String(72))
    firstname: Mapped[str] = mapped_column(String(72))
    password: Mapped[str] = mapped_column(String(72))
    role: Mapped[str] = mapped_column(String(72))
    access: Mapped[bool] = mapped_column(Boolean)
