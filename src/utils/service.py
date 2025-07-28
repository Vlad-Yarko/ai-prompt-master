from typing import Optional, Union
import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src.models import Base
from src.databases import redis_manager


class Service:
    def __init__(
        self, 
        session: Optional[AsyncSession] = None
        ):
        self.session = session
        self.repo = None
        self.user_repo = None
        self.redis_manager = redis_manager
    
    async def get(self, page: Optional[int] = None, **kwargs) -> dict:
        full_data = await self.repo(self.session).get(page, **kwargs)
        data, total, offset = full_data
        count = len(data)
        has_next = False
        if page is not None:
            has_next = (page * offset) < total
        res = {
            "data": data,
            "page": page,
            "count": count,
            "total": total,
            "hasNext": has_next
        }
        return res
    
    async def get_one(self, id: Union[int, uuid.UUID]) -> Union[Base, str]:
        data = await self.repo(self.session).get_one_by_id(id)
        if not data:
            data = ""
        return data
    
    async def create_one(self, data: dict) -> Base:
        obj = await self.repo(self.session).create_one(**data)
        return obj
    
    async def update_one(self, id: Union[int, uuid.UUID], data: dict) -> Union[Base, str]:
        obj = await self.get_one(id)
        if isinstance(obj, str):
            return obj
        obj = await self.repo(self.session).update_one(id, **data)
        return obj
    
    async def delete_one(self, id: Union[int, uuid.UUID]) -> Union[Base, str]:
        obj = await self.get_one(id)
        if isinstance(obj, str):
            return obj
        obj = await self.repo(self.session).delete_one(id)
        return obj
    
    async def get_user_one(self, telegram_id: int) -> Optional[Base]:
        user = await self.user_repo(self.session).get_one_by_telegram_id(telegram_id) 
        return user
