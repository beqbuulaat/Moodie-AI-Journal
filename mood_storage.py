import json
import os
from datetime import datetime

FILE_PATH = "mood_data.json"

def save_entry(user_id, text, mood):
    data = load_entries()
    entry = {
        "user_id": user_id,
        "text": text,
        "mood": mood,
        "timestamp": datetime.now().isoformat()
    }
    data.append(entry)
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=2)

def load_entries():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)
