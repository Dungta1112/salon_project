# Research: Salon Management System Backend

## Decision: Use Django REST Framework with capability-based Django apps

**Rationale**: The requested backend is a DRF project with many business domains.
Capability-based apps keep models, serializers, views, permissions, and tests
close to the business area while avoiding one large monolithic app.

**Alternatives considered**:
- Single app: simpler startup, but quickly becomes hard to navigate and test.
- Microservices: too complex for SQLite and a classroom/demo project.

## Decision: Use SQLite for storage

**Rationale**: SQLite is required and is appropriate for local development,
learning, and demo data. Workflow services will use database transactions for
multi-step operations.

**Alternatives considered**:
- PostgreSQL: stronger concurrency and reporting support, but outside the user's
  required stack.
- In-memory storage: unsuitable because audit, history, and reporting need
  persistent records.

## Decision: Keep business workflows in service classes/functions

**Rationale**: Appointment conflicts, status transitions, invoicing, voucher
validation, reward points, payment histories, and complaint escalation require
cross-model rules. Services make these rules reusable from APIs and tests.

**Alternatives considered**:
- Put rules in views: easy initially, but leads to duplicated logic.
- Put all rules in model `save()`: hides request actor and role context needed
  for permissions and audit.

## Decision: Use role permissions plus queryset scoping

**Rationale**: Role checks answer "may this actor perform the action"; queryset
scoping answers "which records may this actor see or change." Both are required
by the constitution.

**Alternatives considered**:
- Role checks only: risks exposing records through list/detail endpoints.
- Queryset filters only: insufficient for workflow actions such as confirm,
  start service, escalate complaint, or refund.

## Decision: Use soft delete and lifecycle states

**Rationale**: Customer, employee, service, appointment, invoice, payment,
promotion, voucher, reward, feedback, complaint, and notification records must
remain available for audit and history. Soft delete and explicit statuses preserve
historical context.

**Alternatives considered**:
- Physical delete: violates constitution and breaks reporting.
- Immutable-only records: useful for payments and reward ledgers, but too rigid
  for all profile/catalog records.

## Decision: Use explicit status history for financial and complaint workflows

**Rationale**: Payments and complaints need traceable state changes. Separate
history tables preserve the timeline even when the current status changes.

**Alternatives considered**:
- Store only current status: insufficient for audit and dispute handling.
- Store status history only in audit logs: audit is generic; domain histories
  make business queries easier.

## Decision: Use in-app notifications first

**Rationale**: The spec requires notifications but not an external delivery
channel. In-app notifications are testable and sufficient for the initial backend.

**Alternatives considered**:
- Email/SMS/push: valuable future extensions, but add integration complexity not
  needed for the required backend plan.
