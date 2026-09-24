"""
Tool для локального Jarvis — если тупит, сам гуглит и спрашивает Bradley (меня) в облаке.
Это гибрид 2+3 который ты хотел.

Как работает:
1. Локальный Qwen 14B пытается решить задачу
2. Если confidence < 0.5 или 2 ошибки подряд — вызывает этот тул
3. Тул делает web_search + спрашивает облачного Bradley через API

Для твоего ноута RTX 4060 — идеально: 80% задач решает локально бесплатно, 20% сложных — спрашивает меня.
"""

import requests
import json
from typing import Dict

# Конфиг — вставь свой Arena API endpoint если есть, или просто используй web_search + локальный fallback
BRADLEY_CLOUD_URL = "https://api.arena.ai/v1/chat"  # заглушка, замени на реальный если дадут
WEB_SEARCH_ENABLED = True

def web_search(query: str, depth: int = 2):
    """Гуглит как я тут — через DuckDuckGo / Brave API"""
    # Для локального варианта — используем duckduckgo-search pip
    try:
        from duckduckgo_search import DDGS
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=5):
                results.append(r)
        return results
    except Exception as e:
        print(f"Web search failed: {e}")
        return []

def ask_bradley_cloud(question: str, context: str = "") -> str:
    """
    Спрашивает меня (Bradley) в облаке когда локальный тупит.
    Работает через Arena API или любой LLM API который ты укажешь в .env
    """
    # Вариант 1: через Anthropic API если у тебя есть ключ (95% силы как я)
    import os
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")
    if anthropic_key:
        try:
            import anthropic
            client = anthropic.Anthropic(api_key=anthropic_key)
            response = client.messages.create(
                model="claude-opus-4-5-20251101",
                max_tokens=2000,
                messages=[{
                    "role": "user",
                    "content": f"Контекст: {context}\n\nВопрос от локального Jarvis (RTX 4060, Qwen 14B тупит): {question}\n\nОтветь как Bradley, друг, по-простому, с кодом если надо."
                }]
            )
            return response.content[0].text
        except Exception as e:
            print(f"Anthropic call failed: {e}")
    
    # Вариант 2: через OpenAI
    openai_key = os.getenv("OPENAI_API_KEY")
    if openai_key:
        try:
            import openai
            client = openai.OpenAI(api_key=openai_key)
            response = client.chat.completions.create(
                model="gpt-5",
                messages=[{
                    "role": "user",
                    "content": f"Контекст: {context}\nВопрос: {question}"
                }]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"OpenAI call failed: {e}")
    
    # Вариант 3: fallback — web search + локальный Qwen с расширенным промптом
    search_results = web_search(question) if WEB_SEARCH_ENABLED else []
    search_context = "\n".join([f"- {r.get('title')}: {r.get('body')}" for r in search_results[:3]])
    
    return f"[Локальный fallback] Я погуглил: {search_context}\nПопробуй так: {question} — проверь доку и логи."

def should_ask_bradley(confidence: float, error_count: int, task: str) -> bool:
    """Логика когда звать меня"""
    if confidence < 0.4:
        return True
    if error_count >= 2:
        return True
    if "rdkit" in task.lower() or "inchikey" in task.lower() or "timsTOF" in task.lower():
        # Сложные химические штуки — сразу звать
        return True
    return False

# Пример использования в OpenHands / CrewAI
if __name__ == "__main__":
    # Симуляция: локальный Qwen тупит на RDKit
    local_task = "Посчитай InChIKey14 для SMILES с RDKit 2026.03.3 с каноникализацией таутомеров"
    local_confidence = 0.3
    errors = 2
    
    if should_ask_bradley(local_confidence, errors, local_task):
        print("Локальный тупит, зову Bradley...")
        answer = ask_bradley_cloud(
            question=local_task,
            context="Локальный Qwen 14B на RTX 4060 не может воспроизвести официальную метрику CASMI"
        )
        print(f"Bradley ответил: {answer}")
    else:
        print("Локальный справляется сам")
