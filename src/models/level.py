from sqlalchemy import Enum as SQLEnum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base
from src.enums.level import LevelEnum


class Level(Base):
    __tablename__ = "levels"
    
    # title: Mapped[LevelEnum] = mapped_column(SQLEnum(LevelEnum, name='level_title'), default=LevelEnum.beginner)
    title: Mapped[str] = mapped_column(String(50), default="beginner")
    requiredScore: Mapped[int] = mapped_column(nullable=False)
    emoji: Mapped[str] = mapped_column(String(50), nullable=False)
    
    # Users with defined level
    users: Mapped[list["User"]] = relationship("User", back_populates="level", uselist=True)
    
