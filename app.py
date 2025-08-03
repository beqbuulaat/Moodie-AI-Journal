from flask import Flask, request
import requests
import os
from mood_analyzer import analyze_mood
from mood_plotter import create_mood_graph

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route("/")
def index():
    return "Moodie is alive!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("📩 Получено сообщение:", data)

    if not data or "message" not in data:
        return {"ok": False}, 400

    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    if text == "/start":
        send_message(chat_id, "Привет! Я — Moodie 😊 Напиши, как ты себя чувствуешь сегодня.")

    elif text == "/graph":
        path = create_mood_graph(chat_id)
        if path:
            send_photo(chat_id, path)
        else:
            send_message(chat_id, "У тебя пока нет записей 😔")

    else:
        mood = analyze_mood(text)
        send_message(chat_id, f"Я чувствую, что твоё настроение — {mood}.")

    return {"ok": True}

def send_message(chat_id, text):
    try:
        resp = requests.post(
            f"{TELEGRAM_API_URL}/sendMessage",
            json={"chat_id": chat_id, "text": text}
        )
        print("📤 Ответ отправлен:", resp.text)
    except Exception as e:
        print("❌ Ошибка отправки сообщения:", e)

def send_photo(chat_id, file_path):
    try:
        with open(file_path, 'rb') as photo:
            resp = requests.post(
                f"{TELEGRAM_API_URL}/sendPhoto",
                data={"chat_id": chat_id},
                files={"photo": photo}
            )
            print("📷 Фото отправлено:", resp.text)
    except Exception as e:
        print("❌ Ошибка отправки фото:", e)
