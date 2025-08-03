# 🤖 Moodie — AI Mood Journal Telegram Bot

Moodie is a smart AI-powered Telegram bot that helps users reflect on their emotions and track their mood over time. Built with Flask and deployed on Render, Moodie uses the **Gemini 2.5 Flash Lite** model via OpenRouter API to analyze emotions in real time.

---

## 🌟 Features

- 🧠 **AI-Powered Mood Analysis** — understands your emotions through natural language input  
- 📈 **Mood Graph** — (optional) tracks your mood history and visualizes it as a graph  
- 🔁 **Real-time Interaction** — responses are instant via Telegram webhook  
- ☁️ **No Server Setup** — fully deployed on [Render](https://render.com)  

---

## 💬 How it works

1. Send a message to [@MoodieFixerBot](https://t.me/MoodieFixerBot)
2. Moodie analyzes your message using Gemini 2.5
3. You receive a personalized emotional response
4. (Optional) Send `/graph` to view your weekly mood graph

---

## 🛠️ Tech Stack

- Python 3.10  
- Flask  
- Telegram Bot API  
- OpenRouter API (Gemini 2.5 Flash Lite)  
- Render (Deployment)  

---

## 🚀 Commands

| Command   | Description                        |
|-----------|------------------------------------|
| `/start`  | Start conversation with Moodie     |
| *(text)*  | AI will analyze your mood          |
| `/graph`  | View a mood graph (if enabled)     |

---

## 🔐 Environment Variables

Set these on Render:

- `BOT_TOKEN` — Your Telegram Bot Token  
- `OPENROUTER_API_KEY` — Your OpenRouter API Key  

---

## 📸 Preview

![Moodie Preview](preview-image.png)

---

## 💡 Inspiration

Moodie was built to help users develop emotional self-awareness by simply chatting. It's an ideal side project for students, aspiring AI developers, or anyone interested in mental wellness tech.

---

## 📩 Contact

Created by [beqbuulaat](https://github.com/beqbuulaat) — feel free to fork, clone, or contribute!
