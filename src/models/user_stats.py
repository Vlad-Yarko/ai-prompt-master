from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base


class UserStats(Base):
    __tablename__ = "user_stats"
    
    userId: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
    totalScore: Mapped[int] = mapped_column(default=0)
    totalGamesPlayed: Mapped[int] = mapped_column(default=0)
    learnMode: Mapped[int] = mapped_column(default=0)
    creativeMode: Mapped[int] = mapped_column(default=0)
    codeMode: Mapped[int] = mapped_column(default=0)
    antiPromptMode: Mapped[int] = mapped_column(default=0)
    promptPuzzlesMode: Mapped[int] = mapped_column(default=0)
    
    user: Mapped["User"] = relationship("User", back_populates="stats", uselist=False)
