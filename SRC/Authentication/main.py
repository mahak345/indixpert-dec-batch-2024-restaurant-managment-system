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

def sign_up():
    print("== Sign Up ==")
    email = input("Enter email: ")
    password = input("Enter password: ")
    role = input("enter role (user/admin/staff): ").lower() 

    if role not in ['user', 'admin', 'staff']:
        print("Invalid role. Please choose from user/admin/staff.")
        return

    users = load_users()  
    for user in users:
        if user['email'] == email:
            print("Email already exists. Please try again.")
            return

    users.append({
        'email': email,
        'password': password,
        'role': role
    })

    save_users(users) 
    print("User registered successfully!")

def sign_in():
    print("== Sign In ==")
    email = input("Enter email: ")
    password = input("Enter password: ")

    users = load_users()

    for user in users:
        if user['email'] == email and user['password'] == password:
            print(f"Login successful!  {user['role'].capitalize()}")
            return

    print("Invalid email or password.")

def main():
    init_user_file()

    while True:
        print("\n1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        choice = input("Choose a option: ")

        if choice == '1':
            sign_up()
        elif choice == '2':
            sign_in()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()
