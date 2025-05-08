import json
import os
USER_FILE = 'users.json'

def init_user_file():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, 'w') as f:
            json.dump([], f)

def load_users():
    try:
        with open(USER_FILE, 'r') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except json.JSONDecodeError:
        return []

def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f, indent=4)
