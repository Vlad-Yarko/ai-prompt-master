from src.utils.repository import SQLAlchemyRepository
from src.models import Level


class LevelRepository(SQLAlchemyRepository):
    model = Level
