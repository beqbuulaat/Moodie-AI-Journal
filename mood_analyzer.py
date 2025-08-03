import os
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "mistralai/mythomax"  # или "openai/gpt-3.5-turbo"

def analyze_mood(text):
    if not OPENROUTER_API_KEY:
        return "🤖 (Нет API ключа OpenRouter)"

    prompt = f"""
Ты — AI-бот, который анализирует настроение по сообщению пользователя.
Определи, какое настроение в следующем тексте:

"{text}"

Ответь только одним словом: радостное, грустное, тревожное, злое, нейтральное или вдохновлённое.
"""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://moodie-ai-journal.onrender.com",  # укажи сюда свой домен
        "X-Title": "Moodie AI Journal"
    }

    body = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    try:
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)
    data = response.json()
    print("🔎 Ответ от OpenRouter:", data)  # ← ПОКАЖЕТ тебе, что реально пришло

    if "choices" in data:
        mood = data["choices"][0]["message"]["content"].strip().lower()
        return mood
    else:
        print("⚠️ В ответе нет поля 'choices'")
        return "неизвестно"
except Exception as e:
    print("❌ Ошибка AI запроса:", e)
    return "неизвестно"
