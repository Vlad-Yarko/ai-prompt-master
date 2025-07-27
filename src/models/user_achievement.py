from sqlalchemy import Table, Column, ForeignKey
from src.models.base import Base


users_achievements = Table(
    "users_achievements",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("achievement_id", ForeignKey("achievements.id"), primary_key=True)
)
