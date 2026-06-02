<!--
Sync Impact Report
- Version change: template -> 1.0.0
- Modified principles:
  - Template principle 1 -> I. Role-Based Access and Data Scope
  - Template principle 2 -> II. Auditable Business Operations
  - Template principle 3 -> III. Historical Data Preservation
  - Template principle 4 -> IV. Business Rule Integrity
  - Template principle 5 -> V. Maintainable and Extensible Design
- Added sections:
  - Salon Domain Rules
  - Specification and Delivery Standards
- Removed sections:
  - Placeholder SECTION_2 and SECTION_3 content
- Templates requiring updates:
  - OK updated: .specify/templates/plan-template.md
  - OK updated: .specify/templates/spec-template.md
  - OK updated: .specify/templates/tasks-template.md
  - WARN pending: .specify/templates/commands/*.md (directory not present)
  - OK reviewed: AGENTS.md
- Extension hook notes:
  - before_constitution hook /speckit-git-initialize attempted; script failed due to
    encoding/parser error, but repository already exists.
- Follow-up deferred items: None
-->
# Salon Management System Constitution

## Core Principles

### I. Role-Based Access and Data Scope
The system MUST support the Customer, Receptionist, Staff, and Manager roles as
first-class access domains. Every user-facing function, API endpoint, background
operation, report, and data query MUST enforce role-based authorization before
returning or mutating data. Users MUST only access data within their assigned
responsibility scope, such as their own customer profile, assigned appointments,
front-desk appointment operations, or manager-level operational data.

Rationale: Salon workflows include sensitive customer, employee, schedule, and
financial information. Explicit role and scope controls prevent accidental data
exposure and make future role expansion predictable.

### II. Auditable Business Operations
All important operations MUST be recorded for inspection and traceability. Audit
records MUST include the actor, role, action, affected entity, timestamp, prior
state when relevant, resulting state when relevant, and failure or rejection
reason when applicable. Important operations include changes to customers,
employees, services, appointments, invoices, payment transactions, complaints,
permissions, promotions, and system configuration.

Rationale: Operational accountability is required to resolve disputes, investigate
errors, and verify that staff actions followed business rules.

### III. Historical Data Preservation
Critical business data MUST NOT be permanently deleted through normal
application flows. Customers, employees, services, appointments, invoices, and
payment transactions MUST use soft deletion, archival status, immutable history,
or equivalent retention mechanisms. Historical records MUST remain available for
authorized audit, reconciliation, reporting, and complaint handling.

Rationale: Salon operations depend on historical context for customer service,
staff accountability, financial reconciliation, and regulatory-style review.

### IV. Business Rule Integrity
The system MUST validate all business rules before confirming state changes.
Appointments MUST be checked for valid customer, service, staff, time range,
status transition, and scheduling conflicts before confirmation. Payment
transactions MUST preserve complete status and processing history. Feedback and
complaints MUST follow a clear intake, assignment, processing, resolution, and
status-tracking workflow. Related business data MUST remain consistent across
appointments, invoices, transactions, services, staff availability, and customer
records.

Rationale: Incorrect state transitions create double bookings, financial
discrepancies, unresolved complaints, and unreliable operational reports.

### V. Maintainable and Extensible Design
Features MUST be designed for clear ownership, explicit contracts, and future
extension. The system MUST support adding services, promotions, payment methods,
and roles without breaking existing behavior. Shared authorization, validation,
audit, lifecycle, and error-response logic MUST be centralized or consistently
abstracted when repeated across features. Correctness, security, and
maintainability take precedence over early optimization.

Rationale: Salon business rules will evolve. A maintainable design reduces
regression risk when new services, campaigns, payment channels, or responsibilities
are introduced.

## Salon Domain Rules

- Customer, employee, service, appointment, invoice, and transaction data MUST
  have explicit lifecycle states rather than relying on physical deletion.
- Appointment confirmation MUST fail with a clear reason when time, staff,
  service, customer, or availability rules are invalid.
- Payment processing MUST record each attempted, pending, successful, failed,
  refunded, or cancelled state transition.
- Feedback and complaints MUST expose status tracking and responsible handling
  ownership to authorized roles.
- APIs and user-facing functions MUST return consistent, understandable responses
  and must include actionable error information without leaking unauthorized data.

## Specification and Delivery Standards

Every business requirement MUST be written clearly, include concrete acceptance
criteria, and be testable through user scenarios, contract checks, integration
tests, or equivalent verification. Plans, specs, and tasks MUST identify relevant
authorization, data-scope, audit, soft-delete/history, validation, consistency,
and error-handling requirements for each affected workflow. Any exception to a
principle MUST be documented in the feature plan with the business reason,
affected risk, and compensating control.

## Governance

This constitution supersedes conflicting project guidance for business rules,
security, auditability, data lifecycle, and delivery quality. New feature specs
MUST pass the constitution checks before implementation planning is accepted, and
plans MUST re-check compliance after design decisions are made.

Amendments MUST document the changed principles or sections, the reason for the
change, and any templates or runtime guidance that were updated. Versioning uses
semantic versioning: MAJOR for incompatible governance or principle removals,
MINOR for added principles or materially expanded requirements, and PATCH for
clarifications that do not change obligations. Compliance reviews MUST verify
role access, scoped data access, audit records, data retention behavior, business
rule validation, payment and complaint state history, consistency guarantees, and
clear error responses before release.

**Version**: 1.0.0 | **Ratified**: 2026-06-02 | **Last Amended**: 2026-06-02
