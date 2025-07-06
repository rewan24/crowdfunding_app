import json
import os
from datetime import datetime

PROJECTS_FILE = 'projects.json'

if not os.path.exists(PROJECTS_FILE):
    with open(PROJECTS_FILE, 'w') as f:
        json.dump([], f)

def is_valid_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def create_project(user):
    print("\n=== Create Project ===")
    title = input("Enter project title: ")
    details = input("Enter project details: ")
    total_target = input("Enter total target (e.g., 250000): ")

    if not total_target.isdigit():
        print("Target must be a number.")
        return

    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    if not is_valid_date(start_date) or not is_valid_date(end_date):
        print("Invalid date format.")
        return

    if datetime.strptime(start_date, '%Y-%m-%d') >= datetime.strptime(end_date, '%Y-%m-%d'):
        print("Start date must be before end date.")
        return

    with open(PROJECTS_FILE, 'r') as f:
        projects = json.load(f)

    new_project = {
        'id': len(projects) + 1,
        'owner': user['email'],
        'title': title,
        'details': details,
        'total_target': total_target,
        'start_date': start_date,
        'end_date': end_date
    }

    projects.append(new_project)

    with open(PROJECTS_FILE, 'w') as f:
        json.dump(projects, f, indent=4)

    print("Project created successfully!")

def view_projects():
    print("\n=== All Projects ===")
    with open(PROJECTS_FILE, 'r') as f:
        projects = json.load(f)

    if not projects:
        print("No projects found.")
        return

    for project in projects:
        print(f"\n🔹 Project ID: {project['id']}")
        print(f"Title: {project['title']}")
        print(f"Details: {project['details']}")
        print(f"Target: {project['total_target']} EGP")
        print(f"Start Date: {project['start_date']}")
        print(f"End Date: {project['end_date']}")
        print(f"Owner: {project['owner']}")

def edit_project(user):
    print("\n=== Edit Your Project ===")
    view_projects()
    project_id = input("Enter project ID to edit: ")

    with open(PROJECTS_FILE, 'r') as f:
        projects = json.load(f)

    for project in projects:
        if str(project['id']) == project_id:
            if project['owner'] != user['email']:
                print("You can only edit your own projects.")
                return

            print("Leave blank to keep the old value.")
            title = input(f"New title (old: {project['title']}): ") or project['title']
            details = input(f"New details (old: {project['details']}): ") or project['details']
            total_target = input(f"New target (old: {project['total_target']}): ") or project['total_target']
            start_date = input(f"New start date (old: {project['start_date']}): ") or project['start_date']
            end_date = input(f"New end date (old: {project['end_date']}): ") or project['end_date']

            if not is_valid_date(start_date) or not is_valid_date(end_date):
                print("Invalid date.")
                return

            if datetime.strptime(start_date, '%Y-%m-%d') >= datetime.strptime(end_date, '%Y-%m-%d'):
                print("Start date must be before end date.")
                return

            if not total_target.isdigit():
                print("Target must be a number.")
                return

            project['title'] = title
            project['details'] = details
            project['total_target'] = total_target
            project['start_date'] = start_date
            project['end_date'] = end_date

            with open(PROJECTS_FILE, 'w') as f:
                json.dump(projects, f, indent=4)

            print("Project updated successfully.")
            return

    print("Project not found.")

def delete_project(user):
    print("\n=== Delete Your Project ===")
    view_projects()
    project_id = input("Enter project ID to delete: ")

    with open(PROJECTS_FILE, 'r') as f:
        projects = json.load(f)

    for i, project in enumerate(projects):
        if str(project['id']) == project_id:
            if project['owner'] != user['email']:
                print("You can only delete your own projects.")
                return

            projects.pop(i)

            with open(PROJECTS_FILE, 'w') as f:
                json.dump(projects, f, indent=4)

            print("Project deleted.")
            return

    print("Project not found.")

def search_projects_by_date():
    print("\n=== Search Projects by Date ===")
    search_date = input("Enter date (YYYY-MM-DD): ")

    if not is_valid_date(search_date):
        print("Invalid date format.")
        return

    with open(PROJECTS_FILE, 'r') as f:
        projects = json.load(f)

    found = False
    for project in projects:
        if project['start_date'] <= search_date <= project['end_date']:
            found = True
            print(f"\n🔍 Found Project ID: {project['id']}")
            print(f"Title: {project['title']}")
            print(f"Details: {project['details']}")
            print(f"Target: {project['total_target']} EGP")
            print(f"Start: {project['start_date']}")
            print(f"End: {project['end_date']}")
            print(f"Owner: {project['owner']}")

    if not found:
        print("No projects found for that date.")
