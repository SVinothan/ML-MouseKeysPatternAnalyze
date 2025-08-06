import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime
from modules.db import get_mouse_data, get_keyboard_data

def vectorize(data):
    df = pd.DataFrame(data)
    df = df.drop(columns=["_id", "user_id", "timestamp"], errors="ignore")
    return df.mean().values.reshape(1, -1) if not df.empty else None

def compare_vectors(old, current):
    if old is None or current is None:
        return 0.0
    return float(cosine_similarity(old, current)[0][0])

def verify_behavior(user_id):
    today = datetime.now().date()

    mouse_old, mouse_now = get_mouse_data(user_id, today)
    keyboard_old, keyboard_now = get_keyboard_data(user_id, today)

    mouse_score = compare_vectors(vectorize(mouse_old), vectorize(mouse_now))
    keyboard_score = compare_vectors(vectorize(keyboard_old), vectorize(keyboard_now))

    avg_score = (mouse_score + keyboard_score) / 2

    return {
        "mouse_similarity": mouse_score,
        "keyboard_similarity": keyboard_score,
        "average_score": avg_score,
        "verified": avg_score > 0.75
    }
