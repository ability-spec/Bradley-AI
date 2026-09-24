# Добавь этот файл в OpenHands как custom tool — чтобы он сам меня звал

from typing import Annotated

def ask_bradley_when_stuck(
    question: Annotated[str, "Вопрос который не можешь решить локально"],
    context: Annotated[str, "Что ты уже пробовал и какие ошибки"] = "",
    search_web: Annotated[bool, "Нужно ли погуглить перед вопросом"] = True
) -> str:
    """
    Используй этот тул когда:
    - confidence < 0.5
    - 2 ошибки подряд
    - задача про RDKit, InChIKey14, timsTOF, DreaMS, MIST, DiffMS, ICEBERG
    - не знаешь как посчитать нейтральную массу с аддуктом
    
    Я (Bradley) в облаке отвечу и дам код.
    """
    from .ask_bradley import ask_bradley_cloud, web_search
    
    search_ctx = ""
    if search_web:
        results = web_search(question)
        search_ctx = "\n".join([r.get('body','')[:200] for r in results[:3]])
    
    full_context = f"{context}\n\nWeb search: {search_ctx}"
    answer = ask_bradley_cloud(question, full_context)
    return answer

# В OpenHands config.yaml добавь:
# tools:
#   - name: ask_bradley_when_stuck
#     description: "Зовет облачного Bradley когда локальный Qwen тупит"
#     function: tools.openhands_tool.ask_bradley_when_stuck
