from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from src.bot.responses.game import GameMessageResponse, GameCallbackResponse
from src.bot.middlewares import GameMiddleware
from src.bot.fsm import GameState
from src.bot.filters import CallDataStarts, StateIn
from src.services import GameService


router = Router()
router.message.middleware(GameMiddleware())
router.callback_query.middleware(GameMiddleware())


@router.message(StateIn(None, GameState.active), Command("games"))
async def games_hand(message: Message, state: FSMContext, service: GameService):
    await GameMessageResponse(
        message=message,
        state=state
    ).games_hand(service)
    
    
@router.callback_query(StateFilter(GameState.active), CallDataStarts("description_game_"))
async def game_info_hand(callback: CallbackQuery, state: FSMContext, service: GameService):
    await GameCallbackResponse(
        callback=callback,
        state=state
    ).game_info_hand(service)
