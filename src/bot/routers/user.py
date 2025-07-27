from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from src.bot.responses.user import UserMessageResponse, UserCallbackResponse
from src.bot.fsm.user import UserState
from src.bot.utils.filter import CallDataEq
from src.bot.middlewares.user import UserMiddleware
from src.services import UserService


router = Router()
router.message.middleware(UserMiddleware())
router.callback_query.middleware(UserMiddleware())


@router.message(StateFilter(None), Command('authorize'))
async def authorize_hand(message: Message, state: FSMContext):
    await UserMessageResponse(
        message=message,
        state=state
    ).authorize_hand()


@router.message(StateFilter(None), Command('delete'))
async def delete_command_hand(message: Message, state: FSMContext):
    await UserMessageResponse(
        message=message,
        state=state
    ).delete_hand()
    
    
@router.message(StateFilter(None), Command("profile"))
async def profile_hand(message: Message, state: FSMContext, service: UserService):
    await UserMessageResponse(
        message=message,
        state=state
    ).profile_hand(service)
    
    
@router.callback_query(StateFilter(UserState.delete), CallDataEq("delete"))
async def delete_hand(callback: CallbackQuery, state: FSMContext):
    await UserCallbackResponse(
        callback=callback,
        state=state
    )
