import os
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def analyze_mood(text):
    if not OPENROUTER_API_KEY:
        print("❌ OPENROUTER_API_KEY не установлен")
        return "неизвестно"

    prompt = f'Проанализируй настроение этого сообщения и ответь одним словом (радостное, грустное, тревожное, нейтральное и т.д.):\n"{text}"'

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://moodie-ai-journal.onrender.com",  # укажи здесь свой URL
        "X-Title": "Moodie AI Journal"
    }

    body = {
        "model": "google/gemini-2.5-flash-lite",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)
        data = response.json()
        print("🔎 Ответ от OpenRouter:", data)

        if "choices" in data and data["choices"]:
            mood = data["choices"][0]["message"]["content"].strip().lower()
            return mood
        else:
            print("⚠️ В ответе нет поля 'choices' или он пустой")
            return "неизвестно"
    except Exception as e:
        print("❌ Ошибка AI запроса:", e)
        return "неизвестно"
