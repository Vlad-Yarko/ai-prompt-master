from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from src.bot.responses.base import BaseMessageResponse
from src.services import ProgressDataService
from src.bot.middlewares import BaseMiddleware


router = Router()
router.message.filter(StateFilter(None))
router.message.middleware(BaseMiddleware())


@router.message(Command('start'))
async def start_hand(message: Message, state: FSMContext):
    await BaseMessageResponse(
        message=message,
        state=state
    ).start_hand()


@router.message(Command('help'))
async def help_hand(message: Message, state: FSMContext):
    await BaseMessageResponse(
        message=message,
        state=state
    ).help_hand()
    
    
@router.message(Command("levels"))
async def levels_hand(message: Message, state: FSMContext, service: ProgressDataService):
    await BaseMessageResponse(
        message=message,
        state=state
    ).levels_hand(service)
    
    
@router.message(Command("achievements"))
async def achievement_hand(message: Message, state: FSMContext, service: ProgressDataService):
    await BaseMessageResponse(
        message=message,
        state=state
    ).achievement_hand(service)
