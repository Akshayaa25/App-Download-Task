# Project Overview

The Django project facilitates interaction between an admin user and regular users. It consists of an Admin Facing section for managing Android apps and points, and a User Facing section for users to view app listings, track points, and submit task completion evidence through screenshots.

## Prerequisites

Before running the project, ensure you have the following prerequisites installed:

- Python (3.6 or higher)
- Django
- Django REST Framework
- Pillow
- MySQL

## Installation

Follow these steps to set up and run the project:

1. Clone the repository or download the project files.

2. Configure the MySQL Database:
   - Install and configure MySQL on your system.
   - Create a new MySQL database named "webapp".
   - Open the project's settings file (`settings.py`) and update the `DATABASES` configuration with your MySQL database details.

3. Apply Migrations:
   ```
   python manage.py migrate
   ```
4. Run the Development Server:
   ```
   python manage.py runserver
   ```
5. Open a web browser and navigate to `http://127.0.0.1:8000/` to access the project.

**API Endpoints:**
- GET /api/list/admin/ - Retrieve a list of all admin users.
- GET /api/list/user/ - Retrieve a list of all regular users.
- POST /api/create/admin/ - Create a new admin user.
- POST /api/create/user/ - Create a new regular user.
- POST /api/create/app/ - Create a new Android app.
- GET /api/list/app/ - Retrieve a list of all Android apps.
- GET /api/tasks/completed/<str:username>/ - Retrieve a list of completed tasks by a specific user.
- GET /api/task/details/<int:id>/ - Retrieve details of a specific task (Android app).
