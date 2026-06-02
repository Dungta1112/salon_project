# Salon Management Backend (API Hướng Đối Tượng & Nghiệp Vụ)

Đây là hệ thống Backend được xây dựng bằng **Django 5.x** và **Django REST Framework (DRF)** nhằm phục vụ cho hệ thống quản lý Salon cao cấp (Salon Store). Dự án triển khai hệ thống RESTful API hoàn chỉnh hỗ trợ các luồng nghiệp vụ phức tạp, bảo mật phân quyền theo vai trò (Role-based Access Control), lưu giữ lịch sử dữ liệu và tự động kiểm thử.

---

## 🛠 Công Nghệ & Thành Phần Chính

*   **Ngôn ngữ/Phiên bản**: Python 3.11+
*   **Framework chính**: Django 5.x, Django REST Framework (DRF)
*   **Xác thực**: `djangorestframework-simplejwt` (JWT Access/Refresh Tokens)
*   **Bộ lọc**: `django-filter`
*   **Cơ sở dữ liệu**: SQLite (thích hợp cho môi trường phát triển cục bộ và demo giảng dạy)
*   **Kiểm thử**: `pytest`, `pytest-django`

---

## 📂 Cấu Trúc Dự Án (Backend Apps)

Hệ thống được thiết kế theo mô hình Modular Monolith, chia nhỏ thành các ứng dụng Django chuyên biệt nhằm dễ dàng bảo trì và mở rộng:

*   **`core`**: Chứa các model cơ sở (Timestamped, Soft-Delete, Audit Event), các class exceptions dùng chung và các hàm helper hỗ trợ chuẩn hóa cấu trúc phản hồi API.
*   **`accounts`**: Quản lý tài khoản người dùng, phân quyền theo 4 vai trò chính (`customer`, `receptionist`, `staff`, `manager`), xác thực JWT.
*   **`customers`**: Hồ sơ khách hàng, thông tin tích điểm và lịch sử trải nghiệm.
*   **`employees`**: Hồ sơ nhân viên, quản lý ca làm việc và lịch rảnh của thợ (Staff Availability).
*   **`services`**: Danh mục dịch vụ (cắt tóc, gội đầu, làm móng...), lịch sử thay đổi giá và thời gian thực hiện.
*   **`appointments`**: Luồng đặt lịch hẹn, tự động kiểm tra trùng lịch (Conflict check) giữa nhân viên và khung giờ.
*   **`service_execution`**: Ghi nhận hành trình thực tế: Khách đến (Check-in), Bắt đầu làm dịch vụ, Ghi nhận dịch vụ phát sinh thêm, và Hoàn thành dịch vụ.
*   **`billing`**: Tạo hóa đơn và tính toán giá tiền tự động dựa trên dịch vụ hoàn thành và phụ phí phát sinh.
*   **`payments`**: Ghi nhận giao dịch thanh toán và lịch sử thay đổi trạng thái thanh toán.
*   **`promotions`**: Quản lý các chiến dịch khuyến mãi, mã giảm giá (Vouchers) và sổ cái tích lũy điểm thưởng (Reward Point Ledger).
*   **`feedback`**: Tiếp nhận đánh giá dịch vụ và xử lý quy trình khiếu nại (Complaint workflow) gồm các bước: Tiếp nhận → Phân công → Đánh giá → Giải quyết.
*   **`notifications`**: Hệ thống thông báo in-app cho người dùng khi có cập nhật trạng thái lịch hẹn, ưu đãi mới.
*   **`reports`**: Các API thống kê báo cáo doanh thu, hiệu suất nhân viên dành riêng cho Quản trị viên (Manager).

---

## 🚀 Hướng Dẫn Cài Đặt & Khởi Chạy

Thực hiện các lệnh sau trên PowerShell hoặc Terminal để cấu hình và chạy môi trường phát triển:

### 1. Tạo môi trường ảo và cài đặt thư viện
```powershell
# Di chuyển vào thư mục dự án
cd D:\project\salon_project

# Tạo môi trường ảo python
python -m venv .venv

# Kích hoạt môi trường ảo (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Cài đặt các thư viện cần thiết
python -m pip install -r backend\requirements.txt
```

### 2. Thiết lập Cơ sở dữ liệu & Tạo dữ liệu mẫu (Seed Data)
```powershell
# Di chuyển vào thư mục backend
cd backend

# Chạy migrations để khởi tạo cấu trúc bảng
python manage.py migrate

# Nạp dữ liệu thử nghiệm nhanh (Seed demo data)
python manage.py seed_demo_data

# Tạo tài khoản quản trị tối cao (Superuser)
python manage.py createsuperuser

# Khởi chạy máy chủ phát triển
python manage.py runserver
```

Sau khi chạy lệnh trên, máy chủ backend sẽ khả dụng tại địa chỉ: **`http://127.0.0.1:8000/`**

---

## 🔑 Dữ Liệu Demo Mặc Định (Seed Accounts)

Sau khi chạy lệnh `python manage.py seed_demo_data`, hệ thống sẽ tự động tạo sẵn các tài khoản thử nghiệm sau (tất cả đều sử dụng mật khẩu là `ChangeMe123!`):

| Username | Vai Trò (Role) | Chức năng kiểm thử |
| :--- | :--- | :--- |
| **`manager`** | Quản lý (`manager`) | Xem báo cáo doanh thu, phê duyệt khiếu nại, cấu hình tài khoản hệ thống. |
| **`receptionist`** | Lễ tân (`receptionist`) | Duyệt lịch hẹn, tạo hóa đơn, áp mã voucher, ghi nhận thanh toán, chuyển tiếp khiếu nại. |
| **`staff1`** | Nhân viên kỹ thuật (`staff`) | Xem lịch làm việc cá nhân, bắt đầu thực hiện dịch vụ, cập nhật phát sinh, hoàn tất dịch vụ. |
| **`customer1`** | Khách hàng (`customer`) | Xem danh mục dịch vụ, đặt lịch hẹn, tích điểm, nhận voucher, gửi khiếu nại/đánh giá. |

---

## 📡 Danh Sách Các Endpoints API Chính

Tất cả các API nghiệp vụ đều yêu cầu truyền Token xác thực ở Header: `Authorization: Bearer <access_token>`.

### 🛡 Hệ thống Xác thực & Tài khoản
*   `POST /api/auth/register/` - Đăng ký tài khoản khách hàng mới.
*   `POST /api/auth/login/` - Đăng nhập nhận chuỗi Access & Refresh Tokens.
*   `POST /api/auth/logout/` - Đăng xuất khỏi hệ thống.
*   `GET /api/auth/me/` | `PATCH /api/auth/me/` - Xem & cập nhật thông tin cá nhân hiện tại.
*   `POST /api/accounts/<id>/deactivate/` - Vô hiệu hóa tài khoản (Chỉ dành cho Manager).

### 📅 Nghiệp Vụ Chính (Lịch Hẹn & Dịch Vụ)
*   `GET /api/services/` - Liệt kê danh mục dịch vụ đang hoạt động.
*   `GET /api/employees/` - Liệt kê danh sách nhân viên và ca trực trống.
*   `POST /api/appointments/` - Yêu cầu đặt lịch hẹn mới (Tự động kiểm tra trùng lịch nhân viên).
*   `POST /api/appointments/<id>/confirm/` - Lễ tân xác nhận lịch hẹn hợp lệ.
*   `POST /api/service-executions/<id>/check-in/` - Ghi nhận khách đến salon.
*   `POST /api/service-executions/<id>/start/` - Nhân viên bắt đầu làm việc.
*   `POST /api/service-executions/<id>/complete/` - Nhân viên hoàn thành và nhập ghi chú kết quả.

### 💰 Hóa Đơn & Thanh Toán
*   `POST /api/invoices/` - Lập hóa đơn tạm tính dựa trên lịch hẹn hoàn thành và phụ phí phát sinh.
*   `POST /api/invoices/<id>/apply-voucher/` - Áp mã voucher giảm giá (Kiểm tra điều kiện hạn mức, ngày hết hạn).
*   `POST /api/payments/` - Ghi nhận thanh toán thành công (Tự động kích hoạt quy trình cộng điểm thưởng tích lũy).

### 📈 Báo Cáo & Quản Trị
*   `GET /api/reports/revenue/` - Báo cáo tổng quan doanh thu theo ngày/tháng/năm (Chỉ Manager).
*   `GET /api/reports/staff-performance/` - Đánh giá năng suất của từng kỹ thuật viên (Chỉ Manager).
*   `GET /api/complaints/` - Danh sách khiếu nại cần xử lý và theo dõi trạng thái.

---

## 🧪 Luồng Nghiệp Vụ Kiểm Thử (Smoke Test Flow)

Để kiểm chứng toàn bộ hệ thống hoạt động chính xác, bạn có thể thực hiện kiểm thử theo kịch bản 12 bước sau:

1.  **Đăng ký & Đăng nhập**: `customer1` đăng ký tài khoản và thực hiện đăng nhập để lấy Token JWT.
2.  **Khám phá**: Khách hàng lấy danh sách dịch vụ hoạt động (`/api/services/`).
3.  **Đặt lịch**: Khách hàng kiểm tra lịch trống của `staff1` và gửi yêu cầu đặt lịch hẹn (`POST /api/appointments/`).
4.  **Phê duyệt**: Lễ tân đăng nhập (`receptionist`), duyệt và xác nhận lịch hẹn (`POST /api/appointments/<id>/confirm/`).
5.  **Check-in**: Khi khách đến, lễ tân ghi nhận khách đến nơi (`POST /api/service-executions/<id>/check-in/`).
6.  **Thực thi**: Nhân viên kỹ thuật (`staff1`) đăng nhập, bắt đầu làm việc (`/start/`) và hoàn thành dịch vụ (`/complete/`).
7.  **Tính tiền**: Lễ tân tạo hóa đơn tạm tính cho cuộc hẹn vừa hoàn thành (`POST /api/invoices/`).
8.  **Giảm giá**: Lễ tân áp dụng mã Voucher `WELCOME50` của khách hàng vào hóa đơn (`/apply-voucher/`).
9.  **Thanh toán**: Khách hàng thanh toán và lễ tân ghi nhận giao dịch thành công (`POST /api/payments/`). Hệ thống tự động ghi nhận điểm tích lũy vào sổ cái (`Reward Point Ledger`).
10. **Thông báo**: Khách hàng kiểm tra lịch sử thông báo nhận điểm thưởng (`GET /api/notifications/`).
11. **Khiếu nại**: Khách hàng cảm thấy chưa hài lòng và gửi khiếu nại lên hệ thống (`POST /api/complaints/`).
12. **Báo cáo**: Quản lý (`manager`) xem và xử lý khiếu nại, đồng thời truy cập `/api/reports/revenue/` để xem doanh thu cập nhật sau thanh toán.

---

## 🚦 Chạy Kiểm Thử Tự Động (Automated Tests)

Mã nguồn được đính kèm bộ kiểm thử tự động toàn diện giúp xác thực tính toàn vẹn của dữ liệu và các quy tắc nghiệp vụ.

Chạy kiểm thử bằng cách thực thi lệnh sau từ thư mục `backend/`:
```powershell
# Chạy toàn bộ test suite
pytest

# Chạy và hiển thị chi tiết thông tin
pytest -v
```
