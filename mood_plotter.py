import matplotlib.pyplot as plt
from datetime import datetime
from mood_storage import load_entries

def create_mood_graph(user_id):
    data = load_entries()
    user_data = [d for d in data if d['user_id'] == user_id]

    if not user_data:
        return None

    user_data.sort(key=lambda x: x['timestamp'])
    dates = [datetime.fromisoformat(d['timestamp']) for d in user_data]
    moods = [mood_to_num(d['mood']) for d in user_data]

    plt.figure(figsize=(10, 4))
    plt.plot(dates, moods, marker='o')
    plt.ylim(-1.1, 1.1)
    plt.yticks([-1, 0, 1], ['Негативное', 'Нейтральное', 'Позитивное'])
    plt.title("Настроение с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Настроение")
    plt.grid(True)
    path = f"mood_plot_{user_id}.png"
    plt.savefig(path)
    plt.close()
    return path

def mood_to_num(mood):
    return {"негативное": -1, "нейтральное": 0, "позитивное": 1}[mood]
