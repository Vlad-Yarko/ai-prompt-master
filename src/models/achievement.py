from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base


class Achievement(Base):
    __tablename__ = "achievements"
    
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    conditionKey: Mapped[str] = mapped_column(String(100), nullable=False)
    conditionValue: Mapped[int] = mapped_column(nullable=False)
    emoji: Mapped[str] = mapped_column(String(50), nullable=False)
    
    users: Mapped[list["User"]] = relationship("User", back_populates="achievements", secondary="users_achievements")
