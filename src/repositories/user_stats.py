from src.utils.repository import SQLAlchemyRepository
from src.models import UserStats


class UserStatsRepository(SQLAlchemyRepository):
    model = UserStats

