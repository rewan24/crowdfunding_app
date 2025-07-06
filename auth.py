import re
import json
import os

USERS_FILE = 'users.json'

if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, 'w') as file:
        json.dump([], file)

def is_valid_egyptian_phone(phone):
    return re.fullmatch(r'01[0125][0-9]{8}', phone)

def register():
    print("\n=== Register ===")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    confirm = input("Confirm password: ")
    phone = input("Enter Egyptian phone number (ex: 01012345678): ")
    if password != confirm:
        print("Passwords do not match.")
        return
    if not is_valid_egyptian_phone(phone):
        print("Invalid Egyptian phone number.")
        return
    with open(USERS_FILE, 'r') as file:
        users = json.load(file)
    for user in users:
        if user['email'] == email:
            print("Email already registered.")
            return
    new_user = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'phone': phone
    }
    users.append(new_user)
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=4)
    print("Registration successful!")

def login():
    print("\n=== Login ===")
    email = input("Enter email: ")
    password = input("Enter password: ")
    with open(USERS_FILE, 'r') as file:
        users = json.load(file)
    for user in users:
        if user['email'] == email and user['password'] == password:
            print(f"Welcome back, {user['first_name']}!")
            return user
    print("Invalid email or password.")
    return None