import os
from pymongo import MongoClient
# from .env import load_dotenv
from datetime import datetime

# load_dotenv()
# client = MongoClient(os.getenv("MONGO_URI"))
# db = client[os.getenv("MONGO_DB")]

client = MongoClient('mongodb+srv://svinothand:11Xowxj5mzHFHWNs@clusterml.aujznm6.mongodb.net?ssl=true&authSource=admin')
db = client['sample_mflix']

def get_mouse_data(user_id, today):
    all_data = list(db.mouse_positions.find({"user_id": user_id}))
    current = [d for d in all_data if d['timestamp'].date() == today]
    old = [d for d in all_data if d['timestamp'].date() < today]
    return old, current

def get_keyboard_data(user_id, today):
    all_data = list(db.keyboard_inputs.find({"user_id": user_id}))
    current = [d for d in all_data if d['timestamp'].date() == today]
    old = [d for d in all_data if d['timestamp'].date() < today]
    return old, current
