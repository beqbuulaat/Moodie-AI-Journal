from flask import Flask, request
import requests
from mood_analyzer import analyze_mood
from mood_storage import save_entry
from mood_plotter import create_mood_graph
import os

app = Flask(__name__)

# Твой Telegram Bot Token (устанавливается в переменных окружения на Render)
TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}"

@app.route('/')
def home():
    return 'Moodie is alive!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')

        if text == "/start":
            send_message(chat_id, "Привет! Я — Moodie 😊 Напиши, как ты себя чувствуешь сегодня.")
        elif text == "/graph":
            path = create_mood_graph(chat_id)
            if path:
                send_photo(chat_id, path)
            else:
                send_message(chat_id, "У тебя пока нет записей.")
        else:
            mood = analyze_mood(text)
            save_entry(chat_id, text, mood)
            response = f"Я чувствую, что твоё настроение — {mood}. Спасибо за доверие ❤️"
            send_message(chat_id, response)

    return {'ok': True}

def send_message(chat_id, text):
    requests.post(f"{TELEGRAM_API_URL}/sendMessage", json={
        "chat_id": chat_id,
        "text": text
    })

def send_photo(chat_id, file_path):
    with open(file_path, 'rb') as photo:
        requests.post(f"{TELEGRAM_API_URL}/sendPhoto", data={"chat_id": chat_id}, files={"photo": photo})
      
