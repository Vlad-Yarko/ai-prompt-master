from src.bot.utils.text import Text


s_start_hand_text = Text("""
*Привіт!*

Ти запустив 🤖 *AI Prompt Master* — тренажер, що допоможе тобі стати майстром спілкування зі штучним інтелектом.

_Напиши /help, щоб дізнатися, як користуватися ботом._
""")


s_help_hand_text = Text("""
*ℹ️ Допомога*

Цей бот навчає створювати якісні промпти для ШІ.  
Використовуй команди нижче, щоб почати:

🔹 */profile* — переглянути свій прогрес  
🔹 */achievements* — твої досягнення  
🔹 */authorize* — увійти до акаунта
🔹 */delete* — видалити акаунт (усі дані буде втрачено назавжди)
🔹 */levels* — переглянути всі рівні  
🔹 */achievements* — переглянути всі досягнення

_Чим кращий твій промпт — тим кращий результат!_
""")


s_levels_hand_text = Text("""
📶 *Усі рівні майстерності*

{% for level in levels %}
{{ loop.index }}. {{ level.emoji }} *{{ level.title }}* — {{ level.requiredScore }} XP
{% endfor %}

Набирай досвід, щоб підніматися вище!
""")


s_achievements_hand_text = Text("""
🏆 *Усі досягнення*

{% for achievement in achievements %}
{{ achievement.emoji }} *{{ achievement.title }}*:
{{ achievement.description }}
{% endfor %}

Розблокуй їх усі!
""")
