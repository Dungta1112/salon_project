# Salon Management Backend

Django REST Framework backend for the Salon Management System feature.

## Setup

```powershell
cd D:\project\salon_project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r backend\requirements.txt
cd backend
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Smoke Flow

Seed demo data with `python manage.py seed_demo_data`, then exercise the flows
from `specs/001-salon-management-system/quickstart.md`.
