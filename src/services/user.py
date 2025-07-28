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
        user_achievement_repo: Repository,
        level_repo: Repository,
        achievement_repo: Repository
    ):
        super().__init__(session)
        self.repo = user_repo
        self.user_repo = user_repo
        self.user_stats_repo = user_stats_repo
        self.user_achievement_repo = user_achievement_repo
        self.level_repo = level_repo
        self.achievement_repo = achievement_repo
    
    async def get_one_with_data(self, telegram_id: int) -> Optional[dict]:
        # Here could be join
        user = await self.user_repo(self.session).get_one_by_telegram_id(telegram_id) 
        if user:
            user_statistics = await self.user_stats_repo(self.session).get_one_by_user_id(user.id)
            user_level = await self.level_repo(self.session).get_one_by_id(user.levelId)
            user_achievements = await self.user_achievement_repo(self.session).get_by_user_id(user.id)
            achievements = []
            if user_achievements:
                for user_achievement in user_achievements:
                    achievement = await self.achievement_repo(self.session).get_one_by_id(user_achievement.achievementId)
                    achievements.append(achievement)
            data = {
                "user": user,
                "statistics": user_statistics,
                "achievements": achievements,
                "level": user_level
            }
            return data
        return user
        
    @transaction
    async def create_one(self, data: dict) -> Optional[Base]:
        user = await self.get_user_one(telegram_id=data.get("telegramId"))
        if user:
            return None
        level = await self.level_repo(self.session).get_one_by_title(LevelEnum.beginner.value)
        data["levelId"] = level.id
        user = await super().create_one(data)
        await self.user_stats_repo(self.session).create_one(userId=user.id)
        return user
    
    @transaction
    async def delete_one(self, telegram_id: int) -> Optional[Base]:
        user = await self.get_user_one(telegram_id=telegram_id)
        if not user:
            print("BOBA")
            return None
        user = await self.user_repo(self.session).delete_one(user.id)
        return user
