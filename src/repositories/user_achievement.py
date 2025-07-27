from src.utils.repository import SQLAlchemyRepository
from src.models import user_achievement


class UserAchievementRepository(SQLAlchemyRepository):
    model = user_achievement

