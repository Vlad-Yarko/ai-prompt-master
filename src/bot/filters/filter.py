from aiogram.filters import Filter
from aiogram.types import CallbackQuery, TelegramObject
from aiogram.fsm.context import FSMContext


class CallDataIn(Filter):
    def __init__(self, data: list[str]):
        self.data = data

    async def __call__(self, callback: CallbackQuery):
        result = callback.data in self.data
        return result


class CallDataEq(Filter):
    def __init__(self, data: str):
        self.data = data

    async def __call__(self, callback: CallbackQuery):
        result = self.data == callback.data
        return result


class StateIn(Filter):
    def __init__(self, states: list[FSMContext]):
        self.states = states

    async def __call__(self, obj: TelegramObject, state: FSMContext):
        current_state = await state.get_state()
        result = current_state in self.states
        return result
