# Feature Specification: Salon Management System

**Feature Branch**: `001-salon-management-system`

**Created**: 2026-06-02

**Status**: Draft

**Input**: User description: "Xây dựng hệ thống quản lý Salon hỗ trợ bốn vai trò gồm Khách hàng, Lễ tân, Nhân viên và Quản lý..."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Khách hàng tự quản lý trải nghiệm dịch vụ (Priority: P1)

Khách hàng có thể đăng ký, đăng nhập, cập nhật thông tin cá nhân, xem dịch vụ,
đặt lịch hẹn, thay đổi hoặc hủy lịch hẹn trong phạm vi cho phép, theo dõi trạng
thái lịch hẹn, xem lịch sử dịch vụ và thanh toán, nhận thông báo, gửi phản hồi
hoặc khiếu nại và theo dõi kết quả xử lý.

**Why this priority**: Đây là luồng tạo nhu cầu sử dụng dịch vụ và là giá trị
cốt lõi trực tiếp cho khách hàng.

**Independent Test**: Có thể kiểm thử bằng cách tạo một tài khoản khách hàng,
đặt một lịch hẹn hợp lệ, thay đổi lịch, hủy lịch, xem lịch sử và gửi một khiếu
nại mà không cần hoàn tất toàn bộ module quản trị.

**Acceptance Scenarios**:

1. **Given** khách hàng đã đăng nhập và có dịch vụ còn hiệu lực, **When** khách
   hàng chọn dịch vụ, nhân viên hoặc khung giờ còn trống và xác nhận đặt lịch,
   **Then** hệ thống tạo lịch hẹn ở trạng thái phù hợp và hiển thị thông báo xác nhận.
2. **Given** khách hàng có lịch hẹn chưa bắt đầu, **When** khách hàng yêu cầu đổi
   sang khung giờ hợp lệ, **Then** hệ thống cập nhật lịch hẹn nếu không có xung
   đột và ghi nhận lịch sử thay đổi.
3. **Given** khách hàng đã sử dụng dịch vụ và có hóa đơn, **When** khách hàng mở
   lịch sử, **Then** hệ thống hiển thị dịch vụ đã dùng, hóa đơn, trạng thái thanh
   toán và giao dịch liên quan thuộc chính khách hàng đó.
4. **Given** khách hàng gửi phản hồi hoặc khiếu nại, **When** lễ tân hoặc quản lý
   cập nhật quá trình xử lý, **Then** khách hàng xem được trạng thái mới nhất và
   kết quả xử lý được phép hiển thị.

---

### User Story 2 - Lễ tân điều phối khách hàng và lịch hẹn (Priority: P1)

Lễ tân quản lý thông tin khách hàng, tạo lịch hẹn thay khách, xác nhận, thay đổi
hoặc hủy lịch hẹn, kiểm tra lịch trống của nhân viên, tiếp nhận phản hồi hoặc
khiếu nại, xử lý các trường hợp thuộc thẩm quyền và chuyển các trường hợp cần
thiết cho quản lý.

**Why this priority**: Lễ tân là vai trò vận hành chính để đảm bảo lịch hẹn, tiếp
nhận khách và phản hồi khách hàng diễn ra liên tục.

**Independent Test**: Có thể kiểm thử bằng cách cho lễ tân tạo khách hàng, đặt
lịch cho khách, xác nhận lịch, kiểm tra xung đột lịch nhân viên và chuyển một
khiếu nại vượt thẩm quyền.

**Acceptance Scenarios**:

1. **Given** lễ tân có quyền quản lý lịch hẹn, **When** lễ tân tạo lịch cho khách
   với nhân viên và khung giờ trống, **Then** hệ thống tạo lịch và hiển thị trạng
   thái cần xác nhận hoặc đã xác nhận theo quy trình.
2. **Given** nhân viên đã có lịch hẹn trong cùng khoảng thời gian, **When** lễ tân
   cố tạo hoặc xác nhận lịch trùng, **Then** hệ thống từ chối và nêu rõ lý do xung đột.
3. **Given** lễ tân tiếp nhận một khiếu nại vượt thẩm quyền, **When** lễ tân chuyển
   cho quản lý, **Then** hệ thống cập nhật người phụ trách, trạng thái xử lý và
   ghi lại lịch sử chuyển tiếp.

---

### User Story 3 - Nhân viên thực hiện và hoàn tất dịch vụ (Priority: P2)

Nhân viên có thể xem lịch làm việc được phân công, xem thông tin lịch hẹn, tiếp
nhận khách, bắt đầu dịch vụ, cập nhật dịch vụ hoặc sản phẩm phát sinh trong quá
trình phục vụ, ghi nhận kết quả thực hiện và xác nhận hoàn thành dịch vụ.

**Why this priority**: Dữ liệu thực hiện dịch vụ là đầu vào cho hóa đơn, lịch sử
khách hàng, đánh giá hiệu suất và báo cáo vận hành.

**Independent Test**: Có thể kiểm thử bằng cách phân công một lịch hẹn cho nhân
viên, cho nhân viên bắt đầu dịch vụ, thêm phát sinh, ghi kết quả và hoàn tất dịch vụ.

**Acceptance Scenarios**:

1. **Given** nhân viên có lịch hẹn được phân công, **When** nhân viên mở lịch làm
   việc, **Then** hệ thống chỉ hiển thị lịch thuộc phạm vi phân công của nhân viên đó.
2. **Given** khách đã đến salon, **When** nhân viên bắt đầu thực hiện dịch vụ,
   **Then** trạng thái lịch hẹn chuyển sang đang phục vụ và sự kiện được ghi nhận.
3. **Given** có dịch vụ hoặc sản phẩm phát sinh, **When** nhân viên cập nhật phát
   sinh trong phạm vi được phép, **Then** dữ liệu phát sinh được gắn với lịch hẹn
   và được tính vào hóa đơn chờ thanh toán.

---

### User Story 4 - Quản lý điều hành danh mục, nhân sự và khuyến mãi (Priority: P2)

Quản lý có thể quản lý tài khoản nhân viên, danh mục dịch vụ, giá và thời lượng
dịch vụ, chương trình khuyến mãi, voucher, điểm thưởng khách hàng, khiếu nại vượt
thẩm quyền và các cấu hình vận hành liên quan.

**Why this priority**: Quản lý cần kiểm soát nguồn lực, giá trị dịch vụ và chính
sách ưu đãi để salon vận hành đúng quy định.

**Independent Test**: Có thể kiểm thử bằng cách quản lý tạo hoặc cập nhật nhân
viên, cập nhật giá dịch vụ, tạo voucher, điều chỉnh điểm thưởng và xử lý một
khiếu nại được chuyển lên.

**Acceptance Scenarios**:

1. **Given** quản lý cập nhật giá hoặc thời lượng dịch vụ, **When** thay đổi được
   lưu, **Then** lịch sử thay đổi được ghi nhận và lịch/hóa đơn đã phát sinh không
   bị sửa sai ngoài quy trình cho phép.
2. **Given** voucher hoặc chương trình khuyến mãi có điều kiện sử dụng, **When**
   áp dụng vào hóa đơn, **Then** hệ thống chỉ chấp nhận nếu điều kiện còn hiệu lực
   và ghi nhận ưu đãi đã dùng.
3. **Given** khiếu nại đã được chuyển cho quản lý, **When** quản lý cập nhật kết
   quả xử lý, **Then** trạng thái khiếu nại, lịch sử xử lý và thông báo cho khách
   hàng được cập nhật.

---

### User Story 5 - Thanh toán, hóa đơn, thông báo và báo cáo vận hành (Priority: P3)

Hệ thống tạo hóa đơn từ dịch vụ đã sử dụng, tính chi phí phát sinh, áp dụng ưu
đãi hoặc voucher, ghi nhận thanh toán, lưu lịch sử giao dịch, gửi thông báo phù
hợp và cung cấp báo cáo doanh thu, lịch hẹn, dịch vụ, khách hàng và hiệu suất
nhân viên cho quản lý.

**Why this priority**: Đây là luồng tổng hợp sau vận hành, cần cho tài chính,
truy vết giao dịch và quyết định quản trị.

**Independent Test**: Có thể kiểm thử bằng cách hoàn tất một lịch hẹn, tạo hóa
đơn, áp dụng voucher hợp lệ, ghi nhận thanh toán, xem lịch sử giao dịch và xem
báo cáo tổng hợp.

**Acceptance Scenarios**:

1. **Given** lịch hẹn đã hoàn thành và có phát sinh, **When** hệ thống tạo hóa đơn,
   **Then** hóa đơn bao gồm dịch vụ chính, phát sinh, ưu đãi hợp lệ, tổng tiền và
   trạng thái thanh toán.
2. **Given** giao dịch thanh toán được thực hiện, **When** trạng thái giao dịch
   thay đổi, **Then** hệ thống lưu đầy đủ lịch sử trạng thái và hiển thị kết quả
   dễ hiểu cho vai trò có quyền.
3. **Given** quản lý mở báo cáo trong một khoảng thời gian, **When** dữ liệu đủ
   điều kiện thống kê, **Then** hệ thống hiển thị doanh thu, số lịch hẹn, dịch vụ
   phổ biến, khách hàng và hiệu suất nhân viên trong phạm vi được phép.

### Edge Cases

- Khách hàng hoặc lễ tân cố đặt lịch với nhân viên không còn trống, dịch vụ không
  còn hoạt động, hoặc khoảng thời gian không hợp lệ.
- Khách hàng yêu cầu thay đổi hoặc hủy lịch sau thời điểm salon không còn cho phép.
- Nhân viên cố xem hoặc cập nhật lịch hẹn không thuộc phân công của mình.
- Voucher hết hạn, đã dùng, không thỏa điều kiện, hoặc bị áp dụng đồng thời với
  ưu đãi không tương thích.
- Thanh toán bị lỗi, bị hủy, thanh toán một phần, hoàn tiền, hoặc ghi nhận trùng.
- Hóa đơn đã thanh toán có yêu cầu điều chỉnh do phát sinh hoặc khiếu nại.
- Khiếu nại quá hạn xử lý, bị chuyển nhiều lần, hoặc không đủ thông tin ban đầu.
- Thông tin khách hàng, nhân viên, dịch vụ, lịch hẹn, hóa đơn hoặc giao dịch bị
  xóa mềm nhưng vẫn cần xuất hiện trong lịch sử được phép xem.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST support account registration, login, profile update,
  and session access for customers.
- **FR-002**: System MUST support Customer, Receptionist, Staff, and Manager
  roles with separate permissions and visible data scopes.
- **FR-003**: System MUST allow customers to view active services, service price
  information, service duration, eligible promotions, and availability needed to
  request appointments.
- **FR-004**: System MUST allow customers and receptionists to create, change,
  cancel, and track appointments according to role permissions and appointment
  lifecycle rules.
- **FR-005**: System MUST validate customer, service, staff, time range,
  appointment status, and schedule conflicts before confirming an appointment.
- **FR-006**: System MUST allow receptionists to manage customer information,
  inspect staff availability, confirm appointments, and escalate complaints to
  managers when outside receptionist authority.
- **FR-007**: System MUST allow staff to view assigned work schedules, receive
  customers, start services, add authorized service or product incidentals,
  record results, and mark services complete.
- **FR-008**: System MUST allow managers to manage employee accounts, services,
  service prices, service durations, promotions, vouchers, reward points, and
  escalated complaints.
- **FR-009**: System MUST create invoices from completed or billable service
  usage, include incidentals, apply eligible promotions or vouchers, calculate
  totals, and expose invoice status.
- **FR-010**: System MUST record payments and preserve payment transaction status
  history, including attempted, pending, successful, failed, cancelled, refunded,
  and adjusted states when applicable.
- **FR-011**: System MUST allow customers to view their own service history,
  invoice history, payment history, notifications, feedback, complaint status,
  and complaint results.
- **FR-012**: System MUST allow receptionists and managers to receive, assign,
  process, escalate, resolve, and track feedback or complaints with visible
  statuses and responsible owners.
- **FR-013**: System MUST automatically update appointment status when relevant
  business events occur, including confirmation, cancellation, customer arrival,
  service start, service completion, invoicing, and closure.
- **FR-014**: System MUST provide manager reports for revenue, appointments,
  services, customers, and staff performance over selectable reporting periods.
- **FR-015**: System MUST send notifications for appointment changes, appointment
  reminders, complaint status changes, payment results, and important customer
  or staff workflow events.
- **FR-016**: System MUST record audit history for important business operations,
  permission-sensitive actions, rejected state changes, financial events, and
  complaint handling actions.
- **FR-017**: System MUST preserve history or use soft deletion for customers,
  employees, services, appointments, invoices, payment transactions, promotions,
  vouchers, reward points, feedback, complaints, and notifications.
- **FR-018**: System MUST keep related customer, employee, service, appointment,
  invoice, payment, promotion, voucher, reward, feedback, complaint, and
  notification data consistent after each accepted workflow step.
- **FR-019**: System MUST provide consistent, understandable responses for
  successful actions, validation failures, authorization failures, scheduling
  conflicts, payment problems, and complaint workflow errors.
- **FR-020**: System MUST prevent users from viewing, changing, reporting on, or
  exporting data outside their role and responsibility scope.

### Key Entities *(include if feature involves data)*

- **User Account**: Login identity, role assignment, status, contact details, and
  lifecycle history.
- **Customer**: Customer profile, preferences, service history, reward points,
  vouchers, appointments, invoices, payments, feedback, and complaints.
- **Employee**: Staff or receptionist profile, role, work status, assigned
  schedules, permissions, and historical employment state.
- **Service**: Salon service name, description, price, duration, active status,
  promotion eligibility, and change history.
- **Appointment**: Customer, selected services, assigned staff, time range,
  status, source of booking, changes, cancellations, and conflict validation
  outcome.
- **Service Execution Record**: Actual service start, service completion, staff
  notes, results, incidentals, and completion confirmation.
- **Invoice**: Billable services, incidentals, discounts, voucher application,
  reward usage, totals, status, and adjustment history.
- **Payment Transaction**: Invoice reference, amount, method category, processing
  status, timestamps, result, failure reason, refund or adjustment details.
- **Promotion**: Campaign rules, eligible services or customers, effective dates,
  discount value, usage limits, and status.
- **Voucher**: Customer-facing discount entitlement, eligibility conditions,
  usage state, expiration, and redemption history.
- **Reward Point Ledger**: Earned, used, adjusted, expired, and reversed customer
  point movements.
- **Feedback**: Customer message, related appointment or service when available,
  receiving role, status, response, and closure details.
- **Complaint**: Issue details, severity, responsible owner, escalation path,
  status, processing notes, resolution, and customer-visible result.
- **Notification**: Recipient, event source, message category, delivery status,
  read status, and relevant business record.
- **Audit Event**: Actor, role, action, affected entity, prior state when relevant,
  resulting state when relevant, timestamp, and rejection reason when applicable.

### Authorization, Audit, and Lifecycle *(mandatory for salon workflows)*

- **Roles and Scope**: Customers can access their own account, appointment,
  invoice, payment, feedback, complaint, reward, voucher, and notification data.
  Receptionists can access customer and appointment data needed for front-desk
  work and complaint intake. Staff can access assigned schedules and service
  execution data. Managers can access employee, service, promotion, voucher,
  reward, complaint escalation, and reporting data needed for salon management.
- **Audit Events**: The system records account changes, role or permission
  changes, customer data updates, service catalog changes, appointment creation
  or state transitions, invoice creation or adjustment, payment status changes,
  promotion/voucher/reward changes, complaint processing, report access, and
  rejected authorization or validation attempts.
- **Lifecycle/History**: Critical records use active, inactive, archived,
  cancelled, completed, resolved, or equivalent lifecycle states. Normal user
  flows do not permanently delete business records.
- **Business Rules**: Appointment confirmation requires no schedule conflict and
  valid customer, service, staff, time range, and status transition. Payment and
  complaint workflows preserve status history. Invoice, reward, voucher, and
  promotion changes must remain consistent with appointments and transactions.
- **Error Responses**: Unauthorized actions, invalid inputs, schedule conflicts,
  payment failures, voucher problems, complaint workflow problems, and stale
  status transitions return clear messages that identify the business reason
  without exposing data outside the actor's scope.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: At least 95% of customers in acceptance testing can register, find a
  service, and submit a valid appointment request without staff assistance.
- **SC-002**: At least 98% of attempted appointment confirmations with conflicting
  staff schedules are rejected before confirmation.
- **SC-003**: Receptionists can create or confirm a valid appointment for an
  existing customer in under 3 minutes during workflow testing.
- **SC-004**: Staff can find assigned appointments and record service completion
  in under 2 minutes per appointment during workflow testing.
- **SC-005**: At least 99% of completed billable service records produce invoices
  whose totals match selected services, incidentals, eligible discounts, voucher
  use, and recorded payments.
- **SC-006**: Every sampled important operation during audit review has an actor,
  role, action, affected record, timestamp, and resulting status or rejection reason.
- **SC-007**: Customers and authorized staff can determine the current status of
  every appointment, payment, feedback item, and complaint in the test set.
- **SC-008**: Managers can obtain revenue, appointment, service, customer, and
  staff performance reports for a selected period with results that reconcile to
  the underlying records used in the test set.

## Assumptions

- The first release covers the four stated roles: Customer, Receptionist, Staff,
  and Manager. Additional roles may be added later without changing existing
  role behavior.
- Customers may self-book appointments, and receptionists may book on behalf of
  customers.
- Appointment changes and cancellations are allowed only while the appointment
  is in a business state that permits modification.
- Reports are intended for managers and use authorized salon operating data.
- Notifications may be shown inside the system first; additional delivery
  channels can be added later without changing the required notification events.
- Payment methods are treated as business categories at this stage so future
  payment options can be added without changing invoice and transaction rules.
