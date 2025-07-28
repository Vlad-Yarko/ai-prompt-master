from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from src.databases import db_session
from src.services import GameService
from src.repositories import GameRepository, UserRepository


class GameMiddleware(BaseMiddleware):
    def __init__(self):
        pass

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ):
        async for session in db_session():
            data['session'] = session
            data['service'] = GameService(
                session=session,
                game_repo=GameRepository,
                user_repo=UserRepository
            ) 
            result = await handler(event, data)
            return result
