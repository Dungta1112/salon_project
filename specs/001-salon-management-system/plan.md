# Implementation Plan: Salon Management System Backend

**Branch**: `001-salon-management-system` | **Date**: 2026-06-02 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-salon-management-system/spec.md`

## Summary

Build a Django REST Framework backend for a salon management system with four
roles: Customer, Receptionist, Staff, and Manager. The backend will expose REST
APIs for account and role management, customers, employees, services,
appointments, service execution, invoices, payments, feedback, complaints,
promotions, vouchers, reward points, notifications, and reports.

The design uses one Django project with several focused Django apps. SQLite is
used for the project database. Complex business rules are kept in service
classes so views remain thin, permissions remain centralized, and workflows are
easy to test.

## Technical Context

**Language/Version**: Python 3.11+

**Primary Dependencies**: Django 5.x, Django REST Framework, djangorestframework-simplejwt, django-filter

**Storage**: SQLite

**Testing**: pytest, pytest-django, DRF APIClient

**Target Platform**: Local development and classroom/demo deployment

**Project Type**: Backend web service

**Performance Goals**: Support classroom/demo usage with predictable responses
for common CRUD, appointment search, invoicing, and report views over moderate
salon-sized data.

**Constraints**: Use Django REST Framework and SQLite; keep architecture simple
enough for a student project while preserving authorization, auditability, data
history, and testability.

**Scale/Scope**: Single salon or small multi-branch-ready model, four initial
roles, core operational workflows, and reporting over local SQLite data.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Role Access and Data Scope**: PASS. The backend will implement role constants,
  DRF permission classes, queryset scoping, and workflow-level checks for
  Customer, Receptionist, Staff, and Manager.
- **Auditability**: PASS. Important model changes and rejected workflow actions
  will create `AuditEvent` records through shared audit helpers used by services.
- **Historical Data Preservation**: PASS. Critical records use soft-delete or
  lifecycle statuses. No normal API will permanently delete customers, employees,
  services, appointments, invoices, payments, promotions, vouchers, reward
  ledgers, feedback, complaints, or notifications.
- **Business Rule Integrity**: PASS. Appointment conflicts, appointment status
  transitions, invoice calculation, voucher usage, reward points, payment status
  history, and complaint escalation are handled in transaction-aware service
  functions.
- **Maintainability and Extensibility**: PASS. Apps are separated by business
  area and cross-cutting concerns are centralized in `core`, `accounts`, and
  workflow service modules.
- **Consistent Responses and Errors**: PASS. APIs will use DRF serializers,
  validation errors, standardized error payloads, and explicit business error
  codes for conflicts, authorization failures, and invalid state transitions.

## Project Structure

### Documentation (this feature)

```text
specs/001-salon-management-system/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── api.md
└── checklists/
    └── requirements.md
```

### Source Code (repository root)

```text
backend/
├── manage.py
├── salon_backend/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── core/                 # Base models, audit, common responses, soft delete
│   ├── accounts/             # User, roles, auth, permissions
│   ├── customers/            # Customer profiles and customer-facing history
│   ├── employees/            # Employee profiles and staff availability
│   ├── services/             # Service catalog and price/duration history
│   ├── appointments/         # Booking, conflicts, status transitions
│   ├── service_execution/    # Check-in, start, incidentals, completion results
│   ├── billing/              # Invoices and invoice line calculation
│   ├── payments/             # Payment records and status history
│   ├── promotions/           # Promotions, vouchers, reward point ledger
│   ├── feedback/             # Feedback and complaints
│   ├── notifications/        # In-app notifications
│   └── reports/              # Manager reporting endpoints
└── tests/
    ├── contract/
    ├── integration/
    └── unit/
```

**Structure Decision**: Use a single Django project under `backend/` with focused
apps grouped by salon business capability. This is simpler than a microservice or
multi-project design and fits SQLite/classroom constraints while remaining easy
to extend.

## Backend Architecture

- **Views/ViewSets**: DRF viewsets expose CRUD and workflow actions. Views call
  service functions for state-changing business operations.
- **Serializers**: Serializers validate request shape and simple field rules.
  Cross-entity rules are delegated to services.
- **Services**: Appointment, invoice, payment, voucher, reward, complaint, and
  notification services own business rules and use database transactions.
- **Permissions**: Shared DRF permissions check role. Queryset scoping limits
  records to the actor's responsibility scope.
- **Audit**: Services call a shared audit helper after accepted changes and for
  rejected important workflow attempts.
- **Soft Delete**: Critical models inherit from a base soft-delete/lifecycle mixin
  and expose archive/deactivate actions instead of destructive deletes.
- **Reports**: Reports are read-only manager endpoints that aggregate from
  authoritative invoices, payments, appointments, service execution, and staff data.

## Module Responsibilities

- `core`: base timestamped model, soft-delete mixin, status choices, audit model,
  common exceptions, response helpers.
- `accounts`: custom user or profile-linked user, role choices, authentication,
  role permissions, account status.
- `customers`: customer profile, customer history views, customer-facing dashboard.
- `employees`: employee profile, availability blocks, staff schedule scope.
- `services`: service catalog, service categories, price/duration change history.
- `appointments`: appointment model, appointment services, conflict checks,
  booking/cancel/confirm/reschedule APIs.
- `service_execution`: customer arrival, service start, incidentals, result notes,
  completion confirmation.
- `billing`: invoice, invoice items, invoice calculation and adjustment services.
- `payments`: payment transaction, payment status history, refund/adjustment records.
- `promotions`: promotion rules, voucher lifecycle, voucher redemption, reward
  point ledger and reward policy.
- `feedback`: feedback intake, complaint assignment, escalation, status workflow.
- `notifications`: in-app notification creation and read tracking.
- `reports`: revenue, appointment, service, customer, and staff performance summaries.

## API Surface

Detailed contracts are in [contracts/api.md](./contracts/api.md). Main endpoint
groups:

- `/api/auth/*`
- `/api/customers/*`
- `/api/employees/*`
- `/api/services/*`
- `/api/appointments/*`
- `/api/service-executions/*`
- `/api/invoices/*`
- `/api/payments/*`
- `/api/promotions/*`
- `/api/vouchers/*`
- `/api/reward-ledger/*`
- `/api/feedback/*`
- `/api/complaints/*`
- `/api/notifications/*`
- `/api/reports/*`

## Complex Workflow Strategy

- **Appointment conflict check**: Reject confirmation or reschedule when the
  assigned staff has another active appointment overlapping the requested time
  range. Exclude cancelled/rejected/completed states. Validate service duration,
  staff active status, and appointment state before saving.
- **Appointment status updates**: Use explicit transitions such as requested,
  confirmed, arrived, in_service, completed, invoiced, closed, cancelled, and
  no_show. Each transition is performed through a service and audited.
- **Invoice calculation**: Build invoice lines from completed services and
  incidentals, then apply eligible promotions, voucher discount, reward usage,
  taxes/fees if configured, and compute total due.
- **Voucher application**: Validate active state, expiration, customer ownership
  or campaign eligibility, usage limits, service eligibility, minimum invoice
  amount, and incompatible promotions before marking redemption.
- **Reward points**: Record point changes as ledger entries. Award points only
  after successful payment, reverse or adjust on refund, and never update point
  totals without a ledger record.
- **Complaint handling**: Use status workflow: received, assigned, in_review,
  escalated, resolved, closed, rejected. Receptionists can intake and handle
  permitted issues; managers handle escalations and final outcomes.

## Complexity Tracking

> No constitution violations identified. The service layer adds structure, but it
> is justified by the number of workflow rules and keeps views/test cases simpler.

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |

## Post-Design Constitution Check

- **Role Access and Data Scope**: PASS. Contracts define role restrictions and
  data scoping per endpoint group.
- **Auditability**: PASS. Data model includes `AuditEvent` and workflow histories.
- **Historical Data Preservation**: PASS. Data model documents soft delete and
  lifecycle status for critical records.
- **Business Rule Integrity**: PASS. Research, data model, and contracts define
  state transitions and validation services.
- **Maintainability and Extensibility**: PASS. Django apps are capability-based
  and future roles/payment methods/promotions can be added through choices,
  policies, and service modules.
- **Consistent Responses and Errors**: PASS. API contract defines a common error
  response format.
