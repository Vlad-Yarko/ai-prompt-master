from sqlalchemy import BigInteger, Enum as SQLEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base, BaseFields


class User(Base, BaseFields):
    __tablename__ = "users"
    
    telegramId: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    chatId: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    levelId: Mapped[int] = mapped_column(ForeignKey("levels.id"), nullable=False)
    # statsId: Mapped[int] = mapped_column(ForeignKey("user_stats.id"))
    
    level: Mapped["Level"] = relationship("Level", back_populates="users", uselist=False)
    stats: Mapped["UserStats"] = relationship("UserStats", back_populates="user", uselist=False)
    achievements: Mapped[list["Achievement"]] = relationship("Achievement", back_populates="users", secondary="user_achievements")
