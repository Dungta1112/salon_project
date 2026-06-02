# Data Model: Salon Management System Backend

## Shared Model Patterns

- `id`: primary key.
- `created_at`, `updated_at`: timestamps for all core records.
- `created_by`, `updated_by`: actor references when available.
- `is_deleted`, `deleted_at`: soft-delete fields for critical mutable records.
- `status`: explicit lifecycle state where the record has a business workflow.
- `notes`: optional operational notes where relevant.

## Entities

### User

- Fields: username, password, email, phone, full_name, role, is_active,
  last_login_at.
- Relationships: optional one-to-one CustomerProfile or EmployeeProfile.
- Validation: role must be one of customer, receptionist, staff, manager.
- Lifecycle: active, inactive, locked.

### CustomerProfile

- Fields: user, code, full_name, phone, email, birth_date, gender, address,
  preferences, status, is_deleted.
- Relationships: appointments, invoices, payments, vouchers, reward ledger,
  feedback, complaints, notifications.
- Validation: phone or email must uniquely identify active customer records.
- Lifecycle: active, inactive, archived.

### EmployeeProfile

- Fields: user, employee_code, role_type, full_name, phone, specialties,
  employment_status, is_deleted.
- Relationships: assigned appointments, availability blocks, service execution
  records, complaint assignments.
- Validation: receptionist/staff/manager profiles must map to compatible user role.
- Lifecycle: active, inactive, archived.

### StaffAvailability

- Fields: employee, date, start_time, end_time, availability_type, reason.
- Relationships: employee.
- Validation: end_time must be after start_time; unavailable blocks affect
  appointment conflict checks.

### Service

- Fields: name, category, description, base_price, duration_minutes, active,
  is_deleted.
- Relationships: appointment services, invoice items, promotions.
- Validation: base_price must be non-negative; duration_minutes must be positive.
- Lifecycle: active, inactive, archived.

### ServicePriceHistory

- Fields: service, old_price, new_price, old_duration, new_duration, changed_by,
  changed_at, reason.
- Purpose: preserve service catalog changes without rewriting historical invoices.

### Appointment

- Fields: customer, staff, scheduled_start, scheduled_end, status, source,
  cancellation_reason, no_show_reason, is_deleted.
- Relationships: appointment services, service execution record, invoice,
  notifications, audit events.
- Validation: scheduled_end after scheduled_start; staff active; services active;
  no overlapping active appointment for staff.
- Status transitions: requested -> confirmed -> arrived -> in_service ->
  completed -> invoiced -> closed; requested/confirmed may move to cancelled;
  confirmed may move to no_show.

### AppointmentService

- Fields: appointment, service, price_at_booking, duration_at_booking, quantity.
- Purpose: snapshot selected service values at booking time.

### ServiceExecution

- Fields: appointment, staff, started_at, completed_at, result_notes, status.
- Relationships: incidentals, appointment.
- Status transitions: pending -> in_progress -> completed; pending/in_progress
  may move to cancelled when appointment is cancelled.

### ServiceIncidental

- Fields: execution, item_type, description, quantity, unit_price, added_by.
- Purpose: services or products added during service execution and billed later.

### Invoice

- Fields: customer, appointment, status, subtotal, discount_total, reward_discount,
  total_due, paid_amount, balance_due, issued_at, is_deleted.
- Relationships: invoice items, voucher redemption, payments, reward ledger.
- Validation: totals must reconcile with items, discounts, rewards, and payments.
- Status transitions: draft -> issued -> partially_paid -> paid -> adjusted;
  issued/partially_paid may move to cancelled if business rules permit.

### InvoiceItem

- Fields: invoice, item_type, service, description, quantity, unit_price,
  line_total.
- Purpose: snapshot billable service and incidental amounts.

### PaymentTransaction

- Fields: invoice, customer, amount, method, status, reference_code,
  failure_reason, processed_at, is_deleted.
- Relationships: payment status history.
- Status transitions: attempted -> pending -> successful/failed/cancelled;
  successful may move to refunded or adjusted through explicit records.

### PaymentStatusHistory

- Fields: payment, old_status, new_status, changed_by, changed_at, reason.
- Purpose: domain-level payment traceability.

### Promotion

- Fields: name, description, discount_type, discount_value, starts_at, ends_at,
  active, usage_limit, service_scope, is_deleted.
- Validation: active promotions require valid date range and discount value.

### Voucher

- Fields: code, customer, promotion, discount_type, discount_value, min_invoice,
  starts_at, expires_at, status, usage_limit, used_count, is_deleted.
- Relationships: voucher redemptions and invoices.
- Status transitions: active -> redeemed/expired/cancelled.

### VoucherRedemption

- Fields: voucher, invoice, redeemed_by, redeemed_at, discount_amount.
- Validation: voucher must be active and eligible for the customer and invoice.

### RewardPointLedger

- Fields: customer, invoice, movement_type, points, balance_after, reason,
  created_by, created_at.
- Movement types: earn, redeem, adjust, expire, reverse.
- Validation: redemptions cannot make customer point balance negative.

### Feedback

- Fields: customer, appointment, message, status, received_by, response,
  closed_at.
- Status transitions: received -> reviewed -> responded -> closed.

### Complaint

- Fields: customer, appointment, title, description, severity, status,
  assigned_to, escalated_to, resolution, customer_visible_result, closed_at.
- Status transitions: received -> assigned -> in_review -> escalated ->
  resolved -> closed; received/in_review may move to rejected with reason.

### ComplaintStatusHistory

- Fields: complaint, old_status, new_status, changed_by, changed_at, note.
- Purpose: track complaint progress and escalation.

### Notification

- Fields: recipient, category, title, message, related_object_type,
  related_object_id, delivery_status, read_at, is_deleted.
- Statuses: created, delivered, read, failed.

### AuditEvent

- Fields: actor, actor_role, action, entity_type, entity_id, prior_state,
  resulting_state, rejection_reason, created_at, metadata.
- Purpose: cross-domain traceability for important accepted and rejected actions.

## Relationship Summary

- CustomerProfile has many Appointments, Invoices, Payments, Vouchers,
  RewardPointLedger rows, Feedback records, Complaints, and Notifications.
- EmployeeProfile has many assigned Appointments, StaffAvailability blocks, and
  ServiceExecution records.
- Appointment has many AppointmentServices and at most one ServiceExecution and
  Invoice.
- Invoice has many InvoiceItems and PaymentTransactions and may have a
  VoucherRedemption and RewardPointLedger entries.
- Complaint and PaymentTransaction each have dedicated status history tables.

## Validation Rules

- Appointment time ranges must not overlap another active appointment for the
  same staff member.
- Appointment services and staff must be active when an appointment is confirmed.
- Staff can update only assigned service execution records.
- Invoice totals must be recalculated from authoritative line items and discount
  records before issue/payment.
- Voucher redemption requires active voucher, valid date range, eligible customer,
  remaining usage, compatible promotion rules, and invoice eligibility.
- Reward point redemptions cannot exceed available balance.
- Complaint transitions must follow the allowed workflow and preserve history.
- Reports must only use authorized, non-deleted business records while preserving
  historical records that remain relevant.
