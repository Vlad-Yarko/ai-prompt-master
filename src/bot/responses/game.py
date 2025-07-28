from src.bot.utils.response import MessageResponse, CallbackResponse
from src.bot.text.game import *
from src.bot.fsm.game import GameState
from src.bot.keyboards.inline.game import games_hand_keyboard, game_info_hand_keyboard
from src.services import GameService


class GameMessageResponse(MessageResponse):
    async def games_hand(self, service: GameService) -> None:
        user = await service.get_user_one(self.message.from_user.id)
        if not user:
            self.text = e_games_hand_text.render()
            await self.answer()
            return 
        games = await service.get()
        await self.state.set_state(GameState.active)
        self.text = s_games_hand_text.render()
        await self.answer()
        for game in games:
            self.text = s_games_hand_text_game.render(**game.to_dict())
            self.keyboard = games_hand_keyboard(game.title)
            await self.answer()
        
        
class GameCallbackResponse(CallbackResponse):
    async def game_info_hand(self, service: GameService) -> None:
        title = self.callback.data.split("_")[-1]
        game = await service.get_one(title)
        self.text = s_game_info_hand_text.render(**game.to_dict())
        self.keyboard = game_info_hand_keyboard(title)
        self.click_text = title
        await self.answer()
