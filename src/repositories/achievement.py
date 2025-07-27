from src.utils.repository import SQLAlchemyRepository
from src.models import Achievement


class AchievementRepository(SQLAlchemyRepository):
    model = Achievement

