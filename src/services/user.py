from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.service import Service
from src.utils.repository import Repository, transaction
from src.utils.logger import logger


class UserService(Service):
    def __init__(
        self,
        session: AsyncSession,
        user_repo: Repository,
        user_stats_repo: Repository
    ):
        super().__init__(session)
        self.repo = user_repo
        self.user_repo = user_repo
        self.user_stats_repo = user_stats_repo
    
    @transaction
    async def create_one(self, data: dict) -> dict:
        
        return await super().create_one(data)
    
    @transaction
    async def delete_one(self) -> dict:
        pass
