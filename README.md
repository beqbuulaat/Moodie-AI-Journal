# Moodie — AI Mood Journal 🤖🧠

**Moodie** — это Telegram-бот, который помогает пользователю отслеживать своё настроение и визуализировать эмоциональные состояния.  
Он использует NLP-анализ текста (TextBlob), сохраняет историю и строит графики на основе ваших сообщений.

---

## 📦 Структура проекта

```
Moodie-AI-Journal/
├── app.py              # Flask-приложение и Telegram Webhook
├── mood_analyzer.py    # Анализ настроения текста
├── mood_storage.py     # Хранение данных в JSON
├── mood_plotter.py     # Построение графиков с matplotlib
├── requirements.txt    # Зависимости проекта
└── .env.example        # Пример .env файла с BOT_TOKEN
```

---

## 🚀 Как развернуть на Render

1. Создай Web Service на [render.com](https://render.com)
2. Подключи этот репозиторий
3. Укажи:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
   - Region: Singapore (если ты из Казахстана)
4. Добавь переменную окружения:  
   `BOT_TOKEN=твой_токен_бота`
5. Установи webhook:
   ```
   https://api.telegram.org/bot<твой_токен>/setWebhook?url=https://<твой-проект>.onrender.com/webhook
   ```

---

## ✨ Возможности

- Анализирует настроение сообщений
- Визуализирует настроение в виде графика
- Хранит историю сообщений
- Отвечает добрыми словами 😊

---

## 🔮 Будущее

Хочешь — можно добавить:
- GPT-анализ (через OpenRouter API)
- Личный дневник с поиском
- Категории эмоций (радость, грусть, тревога и т.д.)

---

👤 Автор: @beqbuulaat  
📅 Год: 2025
