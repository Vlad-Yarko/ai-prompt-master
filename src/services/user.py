from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.service import Service
from src.utils.repository import Repository, transaction
from src.models import Base
from src.enums.level import LevelEnum


class UserService(Service):
    def __init__(
        self,
        session: AsyncSession,
        user_repo: Repository,
        user_stats_repo: Repository,
        level_repo: Repository
    ):
        super().__init__(session)
        self.repo = user_repo
        self.user_repo = user_repo
        self.user_stats_repo = user_stats_repo
        self.level_repo = level_repo
        
    async def get_one(self, telegram_id: int) -> Optional[Base]:
        user = await self.user_repo(self.session).get_one_by_telegram_id(telegram_id)
        return user
    
    @transaction
    async def create_one(self, data: dict) -> Optional[Base]:
        user = await self.get_one(telegram_id=data.get("telegramId"))
        if user:
            return None
        level = await self.level_repo(self.session).get_one_by_title(LevelEnum.beginner.value)
        data["levelId"] = level.id
        return await super().create_one(data)
    
    @transaction
    async def delete_one(self, telegram_id: int) -> Optional[Base]:
        user = await self.get_one(telegram_id=telegram_id)
        if not user:
            return None
        return await super().delete_one(user.id)
