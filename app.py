from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    print("⚠️ BOT_TOKEN is not set!")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route("/")
def index():
    return "Moodie is alive!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("📩 Received:", data)

    if not data or "message" not in data:
        return {"ok": False}, 400

    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")
    happy_words = ["счастлив", "рад", "весело", "отлично", "норм", "кайф", "улыбка", "круто", "хорошо", "супер", "удовлетворен", "кайфую"]

    if text == "/start":
        send_message(chat_id, "Привет! Я — Moodie 😊 Напиши, как ты себя чувствуешь сегодня.")
    else:
        mood = "радостное" if "😊" in text or "счастлив" in text else "грустное"
        send_message(chat_id, f"Я чувствую, что твоё настроение — {mood}.")

    return {"ok": True}

def send_message(chat_id, text):
    try:
        resp = requests.post(
            f"{TELEGRAM_API_URL}/sendMessage",
            json={"chat_id": chat_id, "text": text}
        )
        print("📤 Sent:", resp.text)
    except Exception as e:
        print("❌ Error:", e)
