import os
import json
from Sign_up import Sign_up
from Sign_in import Sign_in

USER_FILE = 'users.json'

def init_user_file():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, 'w') as f:
            json.dump([], f)

def main():
    init_user_file()

    while True:
        print("\n1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            Sign_up()
        elif choice == '2':
            Sign_in()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
