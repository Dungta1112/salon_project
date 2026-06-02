# Quickstart: Salon Management System Backend

## Goal

Set up and run the Django REST Framework backend for local development and
classroom/demo testing with SQLite.

## Prerequisites

- Python 3.11 or newer.
- A virtual environment tool.
- Project source created under `backend/` according to `plan.md`.

## Setup

```powershell
cd D:\project\salon_project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r backend\requirements.txt
cd backend
python manage.py migrate
python manage.py seed_demo_data
python manage.py createsuperuser
python manage.py runserver
```

## Suggested Seed Data

Create sample records for:

- One manager account.
- One receptionist account.
- Two staff accounts with availability blocks.
- Two customer accounts.
- Three active salon services.
- One active promotion and one voucher.

## Smoke Test Flow

1. Customer registers and logs in.
2. Customer lists active services.
3. Customer requests an appointment for an available staff member and service.
4. Receptionist confirms the appointment.
5. Staff views assigned schedule and starts service.
6. Staff adds an incidental item and completes service.
7. Receptionist creates an invoice from the completed appointment.
8. Receptionist applies an eligible voucher and records payment success.
9. Customer views service, invoice, payment, reward, and notification history.
10. Customer submits a complaint.
11. Receptionist escalates the complaint to manager.
12. Manager resolves the complaint and views reports.

## Verification Checklist

- Role-scoped users cannot access records outside their responsibility scope.
- Appointment conflict attempts return `appointment_conflict`.
- Payment status history is visible for authorized users.
- Voucher redemption cannot be reused after successful redemption.
- Reward points are recorded through ledger rows.
- Complaint status history is recorded for assignment, escalation, resolution,
  and closure.
- Critical records are archived or soft-deleted rather than physically deleted.
