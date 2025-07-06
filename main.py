from auth import register, login
from projects import *

def main_menu():
    print("\n=== Crowd-Funding App ===")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        register()
    elif choice == '2':
        user = login()
        if user:
            project_menu(user)
    elif choice == '3':
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice.")

def project_menu(user):
    while True:
        print("\n=== Project Menu ===")
        print("1. Create project")
        print("2. View all projects")
        print("3. Edit your project")
        print("4. Delete your project")
        print("5. Search by date")
        print("6. Logout")
        choice = input("Choose an option: ")
        if choice == '1':
            create_project(user)
        elif choice == '2':
            view_projects()
        elif choice == '3':
            edit_project(user)
        elif choice == '4':
            delete_project(user)
        elif choice == '5':
            search_projects_by_date()
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

while True:
    main_menu()