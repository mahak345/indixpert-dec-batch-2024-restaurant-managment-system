import json
import os

USER_FILE = 'users.json'

def load_users():
    try:
        with open(USER_FILE, 'r') as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def sign_in():
    print("== Sign In ==")
    email = input("Enter email: ")
    password = input("Enter password: ")

    users = load_users()
    for user in users:
        if user['email'] == email and user['password'] == password:
            print(f"Login successful! {user['role'].capitalize()}")
            return

    print("Invalid email or password.")