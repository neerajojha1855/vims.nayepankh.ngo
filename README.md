# NayePankh Foundation

**Volunteer Information Management System** for Nayepankh Foundation

This is a Djnago-based web application designed to manage volunteers, track tasks and provide an overview of operations through a centralized dashboard. It includes a REST API, export capabilities and a responsive user interface with TailwindCSS.

## Features
- **Dashboard:** A central hub to view tottal volunteers, active volunteers and task summaries.
- **Volunteer Management:** Register, track and manage volunteers including their skills, availability and active status.
- **Task Management:** Create tasks, specify required skills, duration and assign the volunteers.
- **RESTful API:** Provides API endpoints for interacting with Volunteers and Task data (powered by Django REST framework).
- **Export Data:** Export volunteer data to CSV or PDF formats.
- **Authentication:** Secure user authtentication handled by `django-allauth`.
- **Modern UI:** Styled using Tailwind CSS for a responsive and sleek desgin.

## Tech Stack

- **FrontEnd:** HTML5, Tailwind CSS
- **BackEnd:** Django, DRF
- **DataBase:** PostgreSQL
- **PDF Generation:** `xhtml2pdf`

## Setup Instructions

### 1. Prerequisites
- Python 3
- PostgreSQL DB

### 2. Clone the Repository
```
git clone https://github.com/neerajojha1855/vims.nayepankh.ngo/
cd 

python -m venv .venv
source .venv/Scripts/activate

pip install -r requirements.txt

python manage.py tailwind install

python manage.py migrate

# Terminal 1
python manage.py tailwind start

# Terminal 2
python manage.py runserver

```

<br>

## API Documentation

The API endpoints are accessible via the Django REST Framework Browsable APi.

- **API Root:** `/api/`
- **Volunteers:** `/api/volunteers/`
- **Tasks:** `/api/tasks/`

<br>
<br>

# Created by **Neeraj Ojha**
### nojha1855@gmail.com
