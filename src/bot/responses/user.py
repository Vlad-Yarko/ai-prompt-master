from src.bot.utils.response import MessageResponse, CallbackResponse
from src.bot.text.user import *
from src.services import UserService


class UserMessageResponse(MessageResponse):
    async def authorize_hand(self, service: UserService) -> None:
        self.text = s_authorize_hand_text.render()
        await self.answer()

    async def delete_command_hand(self, service: UserService) -> None:
        self.text = s_delete_command_hand_text.render()
        self.text = e_delete_command_hand_text.render()
        await self.answer()
        
    async def profile_hand(self, service: UserService) -> None:
        self.text = s_profile_hand_text.render()
        self.text = e_profile_hand_text.render()
        await self.answer()
        
        
class UserCallbackResponse(CallbackResponse):
    async def delete_hand(self) -> None:
        self.text = s_delete_hand_text.render()
        await self.answer()

