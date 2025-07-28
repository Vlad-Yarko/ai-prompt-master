from src.bot.utils.keyboard import InlineKeyboard
from src.bot.utils.button import CallbackButton


def games_hand_keyboard(game_title: str) -> InlineKeyboard:
    keyboard = InlineKeyboard(
        [
            [
                CallbackButton(text="Грати 🎮", callback=f"start_game_{game_title}").button
            ],
            [
                CallbackButton(text="Опис 📝", callback=f"description_game_{game_title}").button,
                CallbackButton(text="Меню 🏠", callback="quit").button
            ]
        ]
    ).keyboard()
    return keyboard


def game_info_hand_keyboard(game_title: str) -> InlineKeyboard:
    keyboard = InlineKeyboard(
        [
            [
                CallbackButton(text="Грати 🎮", callback=f"start_game_{game_title}").button
            ],
            [
                CallbackButton(text="Меню 🏠", callback="quit").button
            ]
        ]
    ).keyboard()
    return keyboard
