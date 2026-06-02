# API Contracts: Salon Management System Backend

## Common Rules

- Base path: `/api/`
- Authentication: token-based login for protected endpoints.
- Response shape for success:

```json
{
  "data": {},
  "message": "Success"
}
```

- Response shape for errors:

```json
{
  "error": {
    "code": "business_error_code",
    "message": "Readable business message",
    "details": {}
  }
}
```

- All list endpoints apply role-based queryset scoping.
- Delete endpoints for critical records perform soft delete/archive unless noted.

## Auth and Accounts

- `POST /api/auth/register/`: customer registration.
- `POST /api/auth/login/`: login and token issue.
- `POST /api/auth/logout/`: invalidate current session/token where supported.
- `GET /api/auth/me/`: current user profile and role.
- `PATCH /api/auth/me/`: update current user's allowed profile fields.
- `GET /api/accounts/`: manager lists user accounts.
- `POST /api/accounts/`: manager creates receptionist, staff, or manager account.
- `PATCH /api/accounts/{id}/`: manager updates account status or role-compatible fields.
- `POST /api/accounts/{id}/deactivate/`: manager deactivates account.

## Customers

- `GET /api/customers/`: receptionist/manager list; customer sees own profile only.
- `POST /api/customers/`: receptionist creates customer profile.
- `GET /api/customers/{id}/`: scoped detail.
- `PATCH /api/customers/{id}/`: scoped update.
- `POST /api/customers/{id}/archive/`: receptionist/manager archive customer.
- `GET /api/customers/{id}/history/`: service, appointment, invoice, payment,
  feedback, and complaint history in scope.

## Employees

- `GET /api/employees/`: manager list; receptionist can view availability fields
  needed for scheduling.
- `POST /api/employees/`: manager creates employee profile.
- `GET /api/employees/{id}/`: scoped detail.
- `PATCH /api/employees/{id}/`: manager update.
- `POST /api/employees/{id}/archive/`: manager archive employee.
- `GET /api/employees/{id}/availability/`: receptionist/manager availability.
- `POST /api/employees/{id}/availability/`: manager creates availability block.

## Services

- `GET /api/services/`: active services for all authenticated users; manager can
  include inactive records.
- `POST /api/services/`: manager creates service.
- `GET /api/services/{id}/`: service detail.
- `PATCH /api/services/{id}/`: manager updates service and writes price history.
- `POST /api/services/{id}/archive/`: manager archives service.
- `GET /api/services/{id}/price-history/`: manager views changes.

## Appointments

- `GET /api/appointments/`: scoped list by role.
- `POST /api/appointments/`: customer or receptionist creates appointment request.
- `GET /api/appointments/{id}/`: scoped appointment detail.
- `PATCH /api/appointments/{id}/`: allowed non-terminal updates.
- `POST /api/appointments/{id}/confirm/`: receptionist confirms after conflict check.
- `POST /api/appointments/{id}/reschedule/`: customer or receptionist reschedules.
- `POST /api/appointments/{id}/cancel/`: customer or receptionist cancels when allowed.
- `POST /api/appointments/{id}/arrive/`: receptionist marks customer arrived.
- `POST /api/appointments/{id}/no-show/`: receptionist marks no-show.
- `GET /api/appointments/availability/`: available staff/time slots for service.

## Service Execution

- `GET /api/service-executions/`: staff sees assigned records; manager can review.
- `POST /api/service-executions/{appointment_id}/start/`: assigned staff starts service.
- `POST /api/service-executions/{id}/incidentals/`: assigned staff adds incidentals.
- `POST /api/service-executions/{id}/complete/`: assigned staff records result and completion.

## Invoices and Payments

- `GET /api/invoices/`: scoped invoice list.
- `POST /api/invoices/from-appointment/{appointment_id}/`: receptionist/manager
  creates invoice from completed appointment.
- `GET /api/invoices/{id}/`: scoped invoice detail.
- `POST /api/invoices/{id}/apply-voucher/`: apply eligible voucher.
- `POST /api/invoices/{id}/use-reward-points/`: apply allowed reward points.
- `POST /api/invoices/{id}/issue/`: issue invoice.
- `POST /api/invoices/{id}/adjust/`: manager records allowed adjustment.
- `GET /api/payments/`: scoped payment list.
- `POST /api/payments/`: record payment attempt for invoice.
- `GET /api/payments/{id}/`: scoped payment detail.
- `POST /api/payments/{id}/mark-success/`: receptionist/manager marks successful payment.
- `POST /api/payments/{id}/mark-failed/`: receptionist/manager records failure.
- `POST /api/payments/{id}/refund/`: manager records refund.
- `GET /api/payments/{id}/history/`: status history.

## Promotions, Vouchers, and Rewards

- `GET /api/promotions/`: active promotions for customers; manager full scope.
- `POST /api/promotions/`: manager creates promotion.
- `PATCH /api/promotions/{id}/`: manager updates promotion.
- `POST /api/promotions/{id}/archive/`: manager archives promotion.
- `GET /api/vouchers/`: customer own vouchers; manager/receptionist scoped views.
- `POST /api/vouchers/`: manager issues voucher.
- `POST /api/vouchers/{id}/cancel/`: manager cancels voucher.
- `GET /api/reward-ledger/`: customer own ledger; manager scoped ledger.
- `POST /api/reward-ledger/adjust/`: manager records point adjustment.

## Feedback and Complaints

- `GET /api/feedback/`: scoped feedback list.
- `POST /api/feedback/`: customer submits feedback.
- `POST /api/feedback/{id}/respond/`: receptionist/manager responds.
- `POST /api/feedback/{id}/close/`: receptionist/manager closes.
- `GET /api/complaints/`: scoped complaint list.
- `POST /api/complaints/`: customer or receptionist submits complaint.
- `POST /api/complaints/{id}/assign/`: receptionist/manager assigns owner.
- `POST /api/complaints/{id}/escalate/`: receptionist escalates to manager.
- `POST /api/complaints/{id}/resolve/`: assigned receptionist/manager resolves.
- `POST /api/complaints/{id}/close/`: manager or authorized handler closes.
- `GET /api/complaints/{id}/history/`: status history.

## Notifications

- `GET /api/notifications/`: current user's notifications.
- `POST /api/notifications/{id}/mark-read/`: mark notification as read.
- `POST /api/notifications/mark-all-read/`: mark all current user's notifications read.

## Reports

- `GET /api/reports/revenue/?from=&to=`: manager revenue summary.
- `GET /api/reports/appointments/?from=&to=`: manager appointment status summary.
- `GET /api/reports/services/?from=&to=`: manager service usage summary.
- `GET /api/reports/customers/?from=&to=`: manager customer activity summary.
- `GET /api/reports/staff-performance/?from=&to=`: manager staff performance summary.

## Key Business Error Codes

- `permission_denied`: actor role or scope is not allowed.
- `appointment_conflict`: staff is unavailable or already booked.
- `invalid_status_transition`: workflow transition is not allowed.
- `inactive_service`: selected service is inactive or archived.
- `voucher_not_eligible`: voucher cannot be applied to this invoice.
- `insufficient_reward_points`: customer does not have enough points.
- `payment_state_error`: payment status change is invalid.
- `complaint_assignment_error`: complaint assignment or escalation is invalid.
