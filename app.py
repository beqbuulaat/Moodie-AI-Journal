from flask import Flask, request
import requests
import os
from mood_analyzer import analyze_mood

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route("/")
def index():
    return "Moodie is alive!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("📩 Получены данные:", data)

    if not data or "message" not in data:
        return {"ok": False}, 400

    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    if text == "/start":
        send_message(chat_id, "Привет! Я — Moodie 😊 Напиши, как ты себя чувствуешь сегодня.")
    else:
        mood = analyze_mood(text)
        send_message(chat_id, f"Я чувствую, что твоё настроение — {mood}.")

    return {"ok": True}

def send_message(chat_id, text):
    try:
        response = requests.post(
            f"{TELEGRAM_API_URL}/sendMessage",
            json={"chat_id": chat_id, "text": text}
        )
        print("📤 Ответ отправлен:", response.text)
    except Exception as e:
        print("❌ Ошибка отправки сообщения:", e)
