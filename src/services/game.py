from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.service import Service
from src.utils.repository import Repository, transaction
from src.models import Base


class GameService(Service):
    def __init__(
        self,
        session: AsyncSession,
        game_repo: Repository,
        user_repo: Repository
    ):
        super().__init__(session)
        self.repo = game_repo
        self.game_repo = game_repo
        self.user_repo = user_repo
        
    async def get(self) -> list[Base]:
        data = await super().get()
        return data.get("data")

    async def get_one(self, title: str) -> Optional[Base]:
        data = await self.game_repo(self.session).get_one_by_title(title)
        return data
