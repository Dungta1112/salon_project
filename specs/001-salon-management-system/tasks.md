---
description: "Task list for Salon Management System backend implementation"
---

# Tasks: Salon Management System Backend

**Input**: Design documents from `/specs/001-salon-management-system/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/api.md, quickstart.md

**Tests**: No separate test-first tasks are generated because the feature spec does not request TDD. Verification tasks are included in the final phase.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each workflow.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel because it touches different files and has no dependency on incomplete tasks
- **[Story]**: Maps a task to a user story phase only
- Every task includes a concrete file path

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the Django REST Framework project skeleton and baseline development configuration.

- [X] T001 Create Django project directory structure in backend/
- [X] T002 Create Django project package in backend/salon_backend/
- [X] T003 Create apps package directories in backend/apps/
- [X] T004 Create dependency manifest in backend/requirements.txt
- [X] T005 Configure Django settings for DRF, Simple JWT, django-filter, SQLite, installed apps, and custom user model in backend/salon_backend/settings.py
- [X] T006 Configure root URL routing and API router include points in backend/salon_backend/urls.py
- [X] T007 Create pytest and pytest-django configuration in backend/pytest.ini
- [X] T008 Create developer README with setup commands in backend/README.md

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Implement cross-cutting models, permissions, audit, errors, and app wiring required before user story work begins.

**CRITICAL**: No user story work can begin until this phase is complete.

- [X] T009 Create Django app configs in backend/apps/core/apps.py, backend/apps/accounts/apps.py, backend/apps/customers/apps.py, backend/apps/employees/apps.py, backend/apps/services/apps.py, backend/apps/appointments/apps.py, backend/apps/service_execution/apps.py, backend/apps/billing/apps.py, backend/apps/payments/apps.py, backend/apps/promotions/apps.py, backend/apps/feedback/apps.py, backend/apps/notifications/apps.py, and backend/apps/reports/apps.py
- [X] T010 Create shared timestamp, soft-delete, lifecycle, and active manager base classes in backend/apps/core/models.py
- [X] T011 Create shared business exception classes and error code constants in backend/apps/core/exceptions.py
- [X] T012 Create standardized DRF exception handler and response helpers in backend/apps/core/responses.py
- [X] T013 Create AuditEvent model and audit helper service in backend/apps/core/audit.py
- [X] T014 Create role constants and role utility functions in backend/apps/accounts/roles.py
- [X] T015 Create custom User model with role and account lifecycle fields in backend/apps/accounts/models.py
- [X] T016 Create shared role-based DRF permission classes in backend/apps/accounts/permissions.py
- [X] T017 Create queryset scoping helpers for Customer, Receptionist, Staff, and Manager roles in backend/apps/accounts/scopes.py
- [X] T018 Create authentication serializers for registration, login, and current user profile in backend/apps/accounts/serializers.py
- [X] T019 Create authentication and account viewsets for auth endpoints in backend/apps/accounts/views.py
- [X] T020 Register account and auth URLs in backend/apps/accounts/urls.py
- [X] T021 Add app URL includes for all modules in backend/salon_backend/urls.py
- [X] T022 Create initial migrations for core and accounts apps in backend/apps/core/migrations/ and backend/apps/accounts/migrations/
- [X] T023 Configure admin registration for User and AuditEvent in backend/apps/accounts/admin.py and backend/apps/core/admin.py

**Checkpoint**: Shared backend foundation is ready for story implementation.

---

## Phase 3: User Story 1 - Customer Self-Service Experience (Priority: P1)

**Goal**: Customers can register, update profile, view services, book/change/cancel appointments, track status/history, receive notifications, and submit feedback or complaints.

**Independent Test**: Create a customer account, list services, submit an appointment request, reschedule/cancel it when allowed, view own history, receive a notification, and submit feedback/complaint without manager-only workflows.

### Implementation for User Story 1

- [X] T024 [P] [US1] Create CustomerProfile model in backend/apps/customers/models.py
- [X] T025 [P] [US1] Create Service and ServicePriceHistory models in backend/apps/services/models.py
- [X] T026 [P] [US1] Create Appointment and AppointmentService models in backend/apps/appointments/models.py
- [X] T027 [P] [US1] Create Notification model in backend/apps/notifications/models.py
- [X] T028 [P] [US1] Create Feedback and Complaint models with initial customer-facing statuses in backend/apps/feedback/models.py
- [X] T029 [US1] Create customer profile serializers in backend/apps/customers/serializers.py
- [X] T030 [US1] Create service list/detail serializers for customer-visible service data in backend/apps/services/serializers.py
- [X] T031 [US1] Create appointment serializers for customer create, reschedule, cancel, and detail flows in backend/apps/appointments/serializers.py
- [X] T032 [US1] Create notification serializers in backend/apps/notifications/serializers.py
- [X] T033 [US1] Create feedback and complaint submission serializers in backend/apps/feedback/serializers.py
- [X] T034 [US1] Implement customer registration profile creation in backend/apps/accounts/services.py
- [X] T035 [US1] Implement appointment availability and conflict check service in backend/apps/appointments/services.py
- [X] T036 [US1] Implement customer appointment create, reschedule, cancel, and status transition service methods in backend/apps/appointments/services.py
- [X] T037 [US1] Implement customer history aggregation service for appointments, invoices, payments, feedback, complaints, rewards, and notifications in backend/apps/customers/services.py
- [X] T038 [US1] Implement notification creation helper for appointment and complaint events in backend/apps/notifications/services.py
- [X] T039 [US1] Implement customer profile and history API views in backend/apps/customers/views.py
- [X] T040 [US1] Implement service catalog API views for active services in backend/apps/services/views.py
- [X] T041 [US1] Implement customer appointment API actions for create, reschedule, cancel, and detail in backend/apps/appointments/views.py
- [X] T042 [US1] Implement customer notification API views and mark-read action in backend/apps/notifications/views.py
- [X] T043 [US1] Implement customer feedback and complaint submission API views in backend/apps/feedback/views.py
- [X] T044 [US1] Register customer, service, appointment, notification, feedback, and complaint routes in backend/apps/customers/urls.py, backend/apps/services/urls.py, backend/apps/appointments/urls.py, backend/apps/notifications/urls.py, and backend/apps/feedback/urls.py
- [X] T045 [US1] Create migrations for customer, service, appointment, notification, feedback, and complaint models in backend/apps/customers/migrations/, backend/apps/services/migrations/, backend/apps/appointments/migrations/, backend/apps/notifications/migrations/, and backend/apps/feedback/migrations/
- [X] T046 [US1] Enforce customer role permissions and own-record queryset scoping in backend/apps/customers/views.py, backend/apps/appointments/views.py, backend/apps/notifications/views.py, and backend/apps/feedback/views.py
- [X] T047 [US1] Add audit events for customer profile updates, appointment requests, reschedules, cancellations, feedback, and complaints in backend/apps/core/audit.py

**Checkpoint**: Customer self-service workflow is functional and independently demonstrable.

---

## Phase 4: User Story 2 - Receptionist Appointment and Complaint Coordination (Priority: P1)

**Goal**: Receptionists manage customers, create and confirm appointments, inspect staff availability, receive feedback/complaints, and escalate issues to managers.

**Independent Test**: A receptionist creates a customer, creates and confirms a non-conflicting appointment, sees rejection for a conflicting appointment, and escalates a complaint.

### Implementation for User Story 2

- [X] T048 [P] [US2] Create EmployeeProfile and StaffAvailability models in backend/apps/employees/models.py
- [X] T049 [US2] Create employee availability serializers in backend/apps/employees/serializers.py
- [X] T050 [US2] Extend customer serializers for receptionist-managed customer create/update in backend/apps/customers/serializers.py
- [X] T051 [US2] Extend appointment serializers for receptionist booking, confirmation, arrival, and no-show actions in backend/apps/appointments/serializers.py
- [X] T052 [US2] Extend complaint serializers for assignment and escalation in backend/apps/feedback/serializers.py
- [X] T053 [US2] Implement staff availability lookup service in backend/apps/employees/services.py
- [X] T054 [US2] Extend appointment service with receptionist create, confirm, arrive, no-show, and conflict rejection logic in backend/apps/appointments/services.py
- [X] T055 [US2] Implement receptionist complaint intake, assignment, and escalation service methods in backend/apps/feedback/services.py
- [X] T056 [US2] Implement receptionist customer management API views in backend/apps/customers/views.py
- [X] T057 [US2] Implement employee availability API views for receptionist scheduling in backend/apps/employees/views.py
- [X] T058 [US2] Extend appointment API views with confirm, arrive, no-show, and availability actions in backend/apps/appointments/views.py
- [X] T059 [US2] Extend feedback and complaint API views with receptionist response, assign, escalate, and close actions in backend/apps/feedback/views.py
- [X] T060 [US2] Register employee and receptionist workflow routes in backend/apps/employees/urls.py, backend/apps/appointments/urls.py, and backend/apps/feedback/urls.py
- [X] T061 [US2] Create migrations for employee and availability models in backend/apps/employees/migrations/
- [X] T062 [US2] Enforce receptionist role permissions and front-desk queryset scoping in backend/apps/customers/views.py, backend/apps/employees/views.py, backend/apps/appointments/views.py, and backend/apps/feedback/views.py
- [X] T063 [US2] Add audit events for receptionist customer updates, appointment confirmation, conflict rejection, arrival/no-show, complaint assignment, and escalation in backend/apps/core/audit.py

**Checkpoint**: Receptionist workflow is functional and independently demonstrable.

---

## Phase 5: User Story 3 - Staff Service Execution (Priority: P2)

**Goal**: Staff can view assigned schedules, start service, add incidentals, record results, and complete service.

**Independent Test**: A staff user sees only assigned appointments, starts service, adds an incidental item, completes service, and produces billable execution data.

### Implementation for User Story 3

- [X] T064 [P] [US3] Create ServiceExecution and ServiceIncidental models in backend/apps/service_execution/models.py
- [X] T065 [US3] Create service execution and incidental serializers in backend/apps/service_execution/serializers.py
- [X] T066 [US3] Implement assigned staff schedule query service in backend/apps/service_execution/services.py
- [X] T067 [US3] Implement service start, incidental add, result record, and completion transition service methods in backend/apps/service_execution/services.py
- [X] T068 [US3] Implement staff schedule and service execution API views in backend/apps/service_execution/views.py
- [X] T069 [US3] Register service execution routes in backend/apps/service_execution/urls.py
- [X] T070 [US3] Create migrations for service execution models in backend/apps/service_execution/migrations/
- [X] T071 [US3] Enforce staff role permissions and assigned-appointment queryset scoping in backend/apps/service_execution/views.py
- [X] T072 [US3] Add audit events for service start, incidental additions, result updates, and completion in backend/apps/core/audit.py
- [X] T073 [US3] Trigger appointment status updates from service execution transitions in backend/apps/appointments/services.py

**Checkpoint**: Staff service execution workflow is functional and independently demonstrable.

---

## Phase 6: User Story 4 - Manager Catalog, Employee, Promotion, Reward, and Escalation Management (Priority: P2)

**Goal**: Managers manage employee accounts, service catalog, prices, promotions, vouchers, reward points, and escalated complaints.

**Independent Test**: A manager creates staff accounts, changes service price/duration with history, creates a promotion/voucher, adjusts reward points, and resolves an escalated complaint.

### Implementation for User Story 4

- [X] T074 [P] [US4] Create Promotion, Voucher, VoucherRedemption, and RewardPointLedger models in backend/apps/promotions/models.py
- [X] T075 [US4] Create manager employee account serializers in backend/apps/accounts/serializers.py and backend/apps/employees/serializers.py
- [X] T076 [US4] Create manager service catalog and price history serializers in backend/apps/services/serializers.py
- [X] T077 [US4] Create promotion, voucher, and reward ledger serializers in backend/apps/promotions/serializers.py
- [X] T078 [US4] Extend complaint serializers for manager resolution and closure in backend/apps/feedback/serializers.py
- [X] T079 [US4] Implement manager account and employee lifecycle service methods in backend/apps/accounts/services.py and backend/apps/employees/services.py
- [X] T080 [US4] Implement service catalog update and ServicePriceHistory creation service in backend/apps/services/services.py
- [X] T081 [US4] Implement promotion and voucher lifecycle service methods in backend/apps/promotions/services.py
- [X] T082 [US4] Implement reward point adjustment service using ledger entries in backend/apps/promotions/reward_services.py
- [X] T083 [US4] Implement manager complaint resolution and closure service methods in backend/apps/feedback/services.py
- [X] T084 [US4] Implement manager account and employee API views in backend/apps/accounts/views.py and backend/apps/employees/views.py
- [X] T085 [US4] Implement manager service catalog API views in backend/apps/services/views.py
- [X] T086 [US4] Implement promotion, voucher, and reward ledger API views in backend/apps/promotions/views.py
- [X] T087 [US4] Extend complaint API views for manager resolution and closure in backend/apps/feedback/views.py
- [X] T088 [US4] Register promotion, voucher, reward, manager employee, and manager complaint routes in backend/apps/promotions/urls.py, backend/apps/employees/urls.py, and backend/apps/feedback/urls.py
- [X] T089 [US4] Create migrations for promotion, voucher, redemption, and reward ledger models in backend/apps/promotions/migrations/
- [X] T090 [US4] Enforce manager-only permissions for employee, service catalog, promotion, voucher, reward, and escalated complaint actions in backend/apps/accounts/views.py, backend/apps/employees/views.py, backend/apps/services/views.py, backend/apps/promotions/views.py, and backend/apps/feedback/views.py
- [X] T091 [US4] Add audit events for employee account changes, service price changes, promotion/voucher lifecycle changes, reward adjustments, and complaint resolution in backend/apps/core/audit.py

**Checkpoint**: Manager catalog, staff, promotion, reward, and escalation workflows are functional and independently demonstrable.

---

## Phase 7: User Story 5 - Billing, Payments, Notifications, and Reports (Priority: P3)

**Goal**: The system creates invoices, applies discounts/vouchers/rewards, records payment status history, sends notifications, and provides manager reports.

**Independent Test**: Complete an appointment, create an invoice, apply a voucher and reward points, record payment success, verify transaction history, receive notifications, and view manager reports.

### Implementation for User Story 5

- [X] T092 [P] [US5] Create Invoice and InvoiceItem models in backend/apps/billing/models.py
- [X] T093 [P] [US5] Create PaymentTransaction and PaymentStatusHistory models in backend/apps/payments/models.py
- [X] T094 [US5] Create invoice and invoice item serializers in backend/apps/billing/serializers.py
- [X] T095 [US5] Create payment transaction and payment history serializers in backend/apps/payments/serializers.py
- [X] T096 [US5] Create report serializers for revenue, appointments, services, customers, and staff performance in backend/apps/reports/serializers.py
- [X] T097 [US5] Implement invoice calculation service from completed service execution and incidentals in backend/apps/billing/services.py
- [X] T098 [US5] Implement voucher and reward application integration in backend/apps/billing/discount_services.py
- [X] T099 [US5] Implement payment status transition and PaymentStatusHistory service methods in backend/apps/payments/services.py
- [X] T100 [US5] Implement reward point earning and reversal after payment success/refund in backend/apps/promotions/reward_services.py
- [X] T101 [US5] Implement notification triggers for invoice issue, payment result, reward movement, and complaint changes in backend/apps/notifications/services.py
- [X] T102 [US5] Implement manager reporting aggregation service in backend/apps/reports/services.py
- [X] T103 [US5] Implement invoice API views for create-from-appointment, apply-voucher, use-reward-points, issue, detail, and adjustment in backend/apps/billing/views.py
- [X] T104 [US5] Implement payment API views for create, mark-success, mark-failed, refund, and history in backend/apps/payments/views.py
- [X] T105 [US5] Implement manager report API views in backend/apps/reports/views.py
- [X] T106 [US5] Register invoice, payment, and report routes in backend/apps/billing/urls.py, backend/apps/payments/urls.py, and backend/apps/reports/urls.py
- [X] T107 [US5] Create migrations for billing and payment models in backend/apps/billing/migrations/ and backend/apps/payments/migrations/
- [X] T108 [US5] Enforce scoped invoice/payment visibility for customers, receptionists, staff, and managers in backend/apps/billing/views.py and backend/apps/payments/views.py
- [X] T109 [US5] Enforce manager-only report permissions and report audit logging in backend/apps/reports/views.py and backend/apps/core/audit.py
- [X] T110 [US5] Add audit events for invoice creation, invoice adjustment, voucher application, reward redemption, payment status changes, refunds, and report access in backend/apps/core/audit.py

**Checkpoint**: Billing, payment, notification, and reporting workflow is functional and independently demonstrable.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Validate the end-to-end backend, harden business rules, and prepare the project for demo/use.

- [X] T111 Create seed data command for manager, receptionist, staff, customers, services, availability, promotion, and voucher in backend/apps/core/management/commands/seed_demo_data.py
- [X] T112 Verify role access and data-scope behavior for all endpoint groups documented in specs/001-salon-management-system/contracts/api.md
- [X] T113 Verify appointment conflict, appointment status transition, and stale state error behavior in backend/apps/appointments/services.py
- [X] T114 Verify invoice total reconciliation, voucher eligibility, reward ledger movement, and payment status history behavior in backend/apps/billing/services.py, backend/apps/payments/services.py, and backend/apps/promotions/reward_services.py
- [X] T115 Verify complaint assignment, escalation, resolution, closure, and status history behavior in backend/apps/feedback/services.py
- [X] T116 Verify all critical records use archive, deactivate, lifecycle status, or soft delete instead of physical delete in backend/apps/customers/models.py, backend/apps/employees/models.py, backend/apps/services/models.py, backend/apps/appointments/models.py, backend/apps/service_execution/models.py, backend/apps/billing/models.py, backend/apps/payments/models.py, backend/apps/promotions/models.py, backend/apps/feedback/models.py, backend/apps/notifications/models.py, backend/apps/customers/views.py, backend/apps/employees/views.py, backend/apps/services/views.py, backend/apps/appointments/views.py, backend/apps/service_execution/views.py, backend/apps/billing/views.py, backend/apps/payments/views.py, backend/apps/promotions/views.py, backend/apps/feedback/views.py, and backend/apps/notifications/views.py
- [X] T117 Verify standardized response and error payloads for validation, authorization, conflict, payment, voucher, reward, and complaint errors in backend/apps/core/responses.py
- [X] T118 Update quickstart execution notes after implementation in specs/001-salon-management-system/quickstart.md
- [X] T119 Run migrations and smoke-test flow from quickstart in backend/manage.py
- [X] T120 Review admin registrations for all core models in backend/apps/core/admin.py, backend/apps/accounts/admin.py, backend/apps/customers/admin.py, backend/apps/employees/admin.py, backend/apps/services/admin.py, backend/apps/appointments/admin.py, backend/apps/service_execution/admin.py, backend/apps/billing/admin.py, backend/apps/payments/admin.py, backend/apps/promotions/admin.py, backend/apps/feedback/admin.py, backend/apps/notifications/admin.py, and backend/apps/reports/admin.py

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies; starts immediately.
- **Foundational (Phase 2)**: Depends on Setup; blocks all user story phases.
- **US1 Customer Self-Service (Phase 3)**: Depends on Foundational.
- **US2 Receptionist Coordination (Phase 4)**: Depends on Foundational and shares appointment/customer models from US1.
- **US3 Staff Service Execution (Phase 5)**: Depends on Foundational and appointment models.
- **US4 Manager Management (Phase 6)**: Depends on Foundational; can proceed after employee/service base models exist.
- **US5 Billing, Payments, Notifications, Reports (Phase 7)**: Depends on service execution, promotions/rewards, and appointment completion workflows.
- **Polish (Phase 8)**: Depends on desired user stories being complete.

### User Story Dependencies

- **US1 (P1)**: MVP customer booking and history foundation.
- **US2 (P1)**: Can proceed after foundational appointment/customer models are available; complements US1.
- **US3 (P2)**: Requires assigned appointments and staff profile data.
- **US4 (P2)**: Requires account, employee, service, and complaint base workflows.
- **US5 (P3)**: Requires completed appointment/service execution and promotion/reward concepts.

### Within Each User Story

- Models before serializers.
- Serializers before views.
- Services before workflow view actions.
- URL registration after views exist.
- Migrations after models are defined.
- Role permissions and audit events before story checkpoint validation.

---

## Parallel Opportunities

- Setup directories and configuration tasks T001-T008 can be split by file.
- Foundational core, account, permissions, audit, and response helper tasks T010-T018 can proceed in parallel after app skeletons exist.
- US1 model tasks T024-T028 can run in parallel.
- US2 employee model/serializer tasks T048-T052 can run in parallel.
- US3 service execution model and serializer tasks T064-T065 can run after appointment models exist.
- US4 promotion model and serializer tasks T074-T078 can run in parallel.
- US5 billing and payment model tasks T092-T096 can run in parallel.

## Parallel Example: User Story 1

```text
Task: "T024 [P] [US1] Create CustomerProfile model in backend/apps/customers/models.py"
Task: "T025 [P] [US1] Create Service and ServicePriceHistory models in backend/apps/services/models.py"
Task: "T026 [P] [US1] Create Appointment and AppointmentService models in backend/apps/appointments/models.py"
Task: "T027 [P] [US1] Create Notification model in backend/apps/notifications/models.py"
Task: "T028 [P] [US1] Create Feedback and Complaint models with initial customer-facing statuses in backend/apps/feedback/models.py"
```

## Parallel Example: User Story 4

```text
Task: "T074 [P] [US4] Create Promotion, Voucher, VoucherRedemption, and RewardPointLedger models in backend/apps/promotions/models.py"
Task: "T075 [US4] Create manager employee account serializers in backend/apps/accounts/serializers.py and backend/apps/employees/serializers.py"
Task: "T076 [US4] Create manager service catalog and price history serializers in backend/apps/services/serializers.py"
Task: "T077 [US4] Create promotion, voucher, and reward ledger serializers in backend/apps/promotions/serializers.py"
```

## Implementation Strategy

### MVP First

1. Complete Phase 1 and Phase 2.
2. Complete Phase 3 for customer self-service booking and history.
3. Complete enough of Phase 4 to allow receptionist confirmation and conflict rejection.
4. Validate customer booking, receptionist confirmation, conflict rejection, and audit records.

### Incremental Delivery

1. Deliver US1 + US2 as the scheduling MVP.
2. Add US3 to make appointments produce service execution data.
3. Add US4 to support manager-maintained employees, services, promotions, rewards, and escalations.
4. Add US5 to support billing, payments, notifications, and reports.
5. Run Phase 8 checks after each delivered increment.

### Format Validation

- All implementation tasks use the required checkbox, task ID, optional `[P]`, story label where applicable, and concrete file paths.
- Setup, foundational, and polish tasks intentionally omit story labels.
- User story phase tasks include `[US1]`, `[US2]`, `[US3]`, `[US4]`, or `[US5]`.
