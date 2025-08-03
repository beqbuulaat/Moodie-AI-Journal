from flask import Flask, request
import requests
import os
#from mood_analyzer import analyze_mood
#from mood_storage import save_entry
#from mood_plotter import create_mood_graph

app = Flask(__name__)
BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route("/")
def index():
    return "Moodie is alive!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    if not data:
        return {"ok": False, "error": "No data"}, 400

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            send_message(chat_id, "Привет! Я — Moodie 😊 Напиши, как ты себя чувствуешь сегодня.")
        elif text == "/graph":
            path = create_mood_graph(chat_id)
            if path:
                send_photo(chat_id, path)
            else:
                send_message(chat_id, "У тебя пока нет записей.")
        else:
            #mood = analyze_mood(text)
            #save_entry(chat_id, text, mood)
            mood = "радостное"
            response = f"Я чувствую, что твоё настроение — {mood}. Спасибо за доверие ❤️"
            send_message(chat_id, response)

    return {"ok": True}

def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print("Ошибка при отправке сообщения:", e)

def send_photo(chat_id, file_path):
    url = f"{TELEGRAM_API_URL}/sendPhoto"
    try:
        with open(file_path, 'rb') as photo:
            requests.post(
                url,
                data={"chat_id": chat_id},
                files={"photo": photo}
            )
    except Exception as e:
        print("Ошибка при отправке фото:", e)
        BOT_TOKEN = os.getenv("BOT_TOKEN")
print("DEBUG: BOT_TOKEN =", BOT_TOKEN)  # ⬅️ ДОБАВЬ
