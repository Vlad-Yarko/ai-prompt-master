# python -m scripts.db.progress_data

import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from src.models import Level, Achievement
from src.databases import db_session
from src.enums.level import LevelEnum


async def fill_level(session: AsyncSession) -> None:
    levels = [
        Level(title=LevelEnum.beginner, requiredScore=0, emoji="🐣"),
        Level(title=LevelEnum.novice, requiredScore=500, emoji="📗"),
        Level(title=LevelEnum.learner, requiredScore=1000, emoji="🧩"),
        Level(title=LevelEnum.junior, requiredScore=1500, emoji="🎯"),
        Level(title=LevelEnum.intermediate, requiredScore=2000, emoji="📘"),
        Level(title=LevelEnum.skilled, requiredScore=2500, emoji="🛠️"),
        Level(title=LevelEnum.advanced, requiredScore=3000, emoji="🚀"),
        Level(title=LevelEnum.proficient, requiredScore=3500, emoji="🧠"),
        Level(title=LevelEnum.expert, requiredScore=4000, emoji="🏆"),
        Level(title=LevelEnum.master, requiredScore=4500, emoji="👑"),
    ]
    session.add_all(levels)
    
    
async def fill_achievement(session: AsyncSession) -> None:
    achievements = [
        # Learn mode
        Achievement(title="Початківець оцінки", description="Зароби 50 очок у Learn Mode", emoji="🔍", conditionKey="learnMode", conditionValue=50),
        Achievement(title="Дослідник якості", description="Зароби 200 очок у Learn Mode", emoji="🧪", conditionKey="learnMode", conditionValue=200),
        Achievement(title="Аналітик промптів", description="Зароби 500 очок у Learn Mode", emoji="📊", conditionKey="learnMode", conditionValue=500),
        Achievement(title="Профі відбору", description="Зароби 1000 очок у Learn Mode", emoji="🧠", conditionKey="learnMode", conditionValue=1000),
        Achievement(title="Майстер інтуїції", description="Зароби 2000 очок у Learn Mode", emoji="👁️‍🗨️", conditionKey="learnMode", conditionValue=2000),

        # Creative mode
        Achievement(title="Маленький творець", description="Зароби 50 очок у Creative Mode", emoji="🖌️", conditionKey="creativeMode", conditionValue=50),
        Achievement(title="Ідейний шукач", description="Зароби 200 очок у Creative Mode", emoji="🎨", conditionKey="creativeMode", conditionValue=200),
        Achievement(title="Автор промптів", description="Зароби 500 очок у Creative Mode", emoji="✍️", conditionKey="creativeMode", conditionValue=500),
        Achievement(title="Креатор промптів", description="Зароби 1000 очок у Creative Mode", emoji="🌟", conditionKey="creativeMode", conditionValue=1000),
        Achievement(title="Геній натхнення", description="Зароби 2000 очок у Creative Mode", emoji="💡", conditionKey="creativeMode", conditionValue=2000),

        # Code mode
        Achievement(title="Новачок розробник", description="Зароби 50 очок у Code Mode", emoji="💻", conditionKey="codeMode", conditionValue=50),
        Achievement(title="Початківець GPT Dev", description="Зароби 200 очок у Code Mode", emoji="🧑‍💻", conditionKey="codeMode", conditionValue=200),
        Achievement(title="Інженер слів", description="Зароби 500 очок у Code Mode", emoji="🛠️", conditionKey="codeMode", conditionValue=500),
        Achievement(title="AI девелопер", description="Зароби 1000 очок у Code Mode", emoji="🤖", conditionKey="codeMode", conditionValue=1000),
        Achievement(title="Машинний промптер", description="Зароби 2000 очок у Code Mode", emoji="📟", conditionKey="codeMode", conditionValue=2000),

        # Anti-prompt mode
        Achievement(title="Початківець редактор", description="Зароби 50 очок у Anti-prompt Mode", emoji="📝", conditionKey="antiPromptMode", conditionValue=50),
        Achievement(title="Покращувач GPT", description="Зароби 200 очок у Anti-prompt Mode", emoji="🔧", conditionKey="antiPromptMode", conditionValue=200),
        Achievement(title="Редактор рівняння", description="Зароби 500 очок у Anti-prompt Mode", emoji="✂️", conditionKey="antiPromptMode", conditionValue=500),
        Achievement(title="Архітектор слів", description="Зароби 1000 очок у Anti-prompt Mode", emoji="🏗️", conditionKey="antiPromptMode", conditionValue=1000),
        Achievement(title="Реформатор ІІ", description="Зароби 2000 очок у Anti-prompt Mode", emoji="🧠✏️", conditionKey="antiPromptMode", conditionValue=2000),

        # Prompt puzzles
        Achievement(title="Збирач слів", description="Зароби 50 очок у Prompt Puzzles", emoji="🧩", conditionKey="promptPuzzlesMode", conditionValue=50),
        Achievement(title="Розумник GPT", description="Зароби 200 очок у Prompt Puzzles", emoji="🪄", conditionKey="promptPuzzlesMode", conditionValue=200),
        Achievement(title="Комбінатор промптів", description="Зароби 500 очок у Prompt Puzzles", emoji="🔀", conditionKey="promptPuzzlesMode", conditionValue=500),
        Achievement(title="Алхімік підказок", description="Зароби 1000 очок у Prompt Puzzles", emoji="⚗️", conditionKey="promptPuzzlesMode", conditionValue=1000),
        Achievement(title="Майстер синтезу", description="Зароби 2000 очок у Prompt Puzzles", emoji="🧬", conditionKey="promptPuzzlesMode", conditionValue=2000),
    ]
    session.add_all(achievements)


async def main() -> None:
    async for session in db_session():
        tasks = asyncio.gather(
            fill_level(session),
            fill_achievement(session)
        )
        await tasks
        await session.commit()
    
    
asyncio.run(main())
