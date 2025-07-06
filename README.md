# crowdfunding_app
# Crowd-Funding Console App

This is a simple **console-based crowdfunding application** written in Python.  
It allows users to register, login, and manage fundraising projects through a command-line interface.

---

## Features

### Authentication System:
- User Registration:
  - First name, Last name
  - Email (must be unique)
  - Password + Confirm password
  - Egyptian phone number validation (e.g., 01012345678)
- User Login using email and password

### Project Management:
- Create a project (title, details, target amount, start & end date)
- View all available projects
- Edit your own projects
- Delete your own projects
- Search for projects by date (`YYYY-MM-DD`)

---

## Data Storage
- All users are stored in `users.json`
- All projects are stored in `projects.json`
- No external database required

---

## How to Run

1. Make sure you have **Python 3** installed.
2. Open terminal and go to the project directory:

```bash
cd crowdfunding_app  # or crowdfunding_app_simple
