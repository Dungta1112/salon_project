# Hệ Thống Quản Lý Salon Tóc - Salon Management System

Hệ thống quản lý salon chuyên nghiệp bao gồm backend Django REST Framework và frontend React + TypeScript + Ant Design. Giao diện được thiết kế chuyên biệt và tối ưu hóa trải nghiệm cho bốn vai trò người dùng khác nhau.

---

## 🔑 Tài Khoản Đăng Nhập Demo

Dữ liệu demo đã được cài đặt mật khẩu đồng bộ để dễ dàng kiểm thử và đánh giá giao diện của từng vai trò:

| Vai Trò | Username | Mật Khẩu | Đặc Điểm Giao Diện |
| :--- | :--- | :--- | :--- |
| **Manager (Quản Lý)** | `manager` | `admin123` | Giao diện tối màu chuyên sâu với hệ thống báo cáo doanh thu, hiệu suất nhân viên và nhật ký hệ thống. |
| **Receptionist (Lễ Tân)** | `receptionist` | `admin123` | Giao diện sáng tập trung vào điều hành lịch hẹn, xuất hóa đơn, ghi nhận thanh toán và check-in khách hàng. |
| **Staff (Nhân Viên Kỹ Thuật)** | `staff1` | `admin123` | Giao diện tối ưu hóa cho thiết bị di động, quản lý lịch biểu cá nhân và ghi nhận thực hiện dịch vụ. |
| **Customer (Khách Hàng)** | `customer1` | `admin123` | Cổng thông tin khách hàng với chức năng đặt lịch, xem điểm tích lũy, ví voucher và gửi khiếu nại/góp ý. |

---

## 🛠️ Hướng Dẫn Cài Đặt và Khởi Chạy

### 1. Khởi Chạy Backend (Django REST Framework)

Mở một cửa sổ dòng lệnh mới và thực hiện các bước sau:

```powershell
# Di chuyển vào thư mục dự án
cd c:\BAITAP\slong\salon_project-main

# Kích hoạt môi trường ảo Python
.\.venv\Scripts\Activate.ps1

# Di chuyển vào thư mục backend
cd backend

# Chạy lệnh migrate cơ sở dữ liệu (nếu cần)
python manage.py migrate

# Chạy lệnh seed dữ liệu demo (nếu dữ liệu chưa được nạp)
python manage.py seed_demo_data

# Khởi động máy chủ backend
python manage.py runserver
```

*Máy chủ backend sẽ chạy tại địa chỉ: `http://127.0.0.1:8000`*

### 2. Khởi Chạy Frontend (React + Vite)

Mở một cửa sổ dòng lệnh thứ hai và thực hiện các bước sau:

```powershell
# Di chuyển vào thư mục frontend
cd c:\BAITAP\slong\salon_project-main\fonend\frontend

# Khởi động máy chủ phát triển frontend
npm run dev
```

*Giao diện người dùng sẽ sẵn sàng tại địa chỉ: `http://localhost:5173`*

---

## 📂 Kiến Trúc Hệ Thống Vai Trò (Role-Based Architecture)

Hệ thống điều hướng và phân quyền giao diện được cấu trúc chặt chẽ để đảm bảo tính độc lập giữa các nhóm người dùng:

### 1. Bộ Định Tuyến và Phân Quyền (`src/app/router.tsx`)
- **`RoleGuard`**: Kiểm tra quyền truy cập của tài khoản hiện tại đối với từng nhóm tuyến đường cụ thể.
- **`DashboardRedirect`**: Tự động nhận diện vai trò sau khi đăng nhập thành công và chuyển hướng người dùng về trang giao diện chính tương ứng:
  - Khách hàng -> `/customer/dashboard`
  - Lễ tân -> `/receptionist/dashboard`
  - Nhân viên -> `/staff/dashboard`
  - Quản lý -> `/manager/dashboard`

### 2. Cấu Trúc Thư Mục Giao Diện Người Dùng (`src/pages/`)
Mỗi vai trò sở hữu bộ giao diện độc lập với tổng cộng 36 trang nghiệp vụ:

#### 💼 Phân Hệ Quản Lý (Manager Console) - `src/pages/manager/`
- `ManagerDashboardPage.tsx`: Thống kê doanh thu, biểu đồ tần suất đặt lịch và hiệu suất nhân sự.
- `ManagerEmployeeListPage.tsx` & `ManagerEmployeeDetailPage.tsx`: Quản lý hồ sơ nhân viên, hiệu chỉnh trạng thái công việc.
- `ManagerCustomerListPage.tsx` & `ManagerCustomerDetailPage.tsx`: Theo dõi thông tin khách hàng, cấp bậc và lịch sử dịch vụ.
- `ManagerServiceListPage.tsx` & `ManagerServiceDetailPage.tsx`: Cấu hình danh mục dịch vụ, thời gian thực hiện và đơn giá.
- `ManagerPromotionListPage.tsx` & `ManagerVoucherListPage.tsx`: Quản trị các chương trình ưu đãi và danh sách mã giảm giá.
- `ManagerReportListPage.tsx`: Truy cập sâu các báo cáo doanh thu, cơ cấu dịch vụ và nhân viên xuất sắc.
- `ManagerAuditLogPage.tsx` & `ManagerAccessLedgerPage.tsx`: Giám sát lịch sử thay đổi nghiệp vụ hệ thống.

#### 🛎️ Phân Hệ Lễ Tân (Reception Desk) - `src/pages/receptionist/`
- `ReceptionistDashboardPage.tsx`: Theo dõi số lượng khách trong ngày, cập nhật trạng thái lịch hẹn tức thời.
- `ReceptionistAppointmentListPage.tsx` & `ReceptionistAppointmentDetailPage.tsx`: Lập lịch hẹn mới, xác nhận đặt chỗ, điều phối đổi lịch.
- `ReceptionistCustomerListPage.tsx`: Tra cứu nhanh thông tin thành viên, tạo hồ sơ khách hàng trực tiếp tại quầy.
- `ReceptionistInvoiceListPage.tsx` & `ReceptionistInvoiceDetailPage.tsx`: Lập hóa đơn từ lịch hẹn đã hoàn tất, áp dụng mã voucher, tính toán điểm thưởng.
- `ReceptionistPaymentListPage.tsx` & `ReceptionistPaymentDetailPage.tsx`: Ghi nhận giao dịch thanh toán tiền mặt, thẻ hoặc chuyển khoản.
- `ReceptionistFeedbackListPage.tsx` & `ReceptionistComplaintListPage.tsx`: Tiếp nhận và ghi chú ý kiến khách hàng để phản hồi trực tiếp.

#### ✂️ Phân Hệ Nhân Viên (Stylist Workbench) - `src/pages/staff/`
- `StaffDashboardPage.tsx`: Lịch làm việc cá nhân trong ngày, danh sách lịch hẹn được phân công.
- `StaffSchedulePage.tsx` & `StaffAvailabilityPage.tsx`: Đăng ký giờ làm việc linh hoạt, báo bận đột xuất.
- `StaffServiceExecutionListPage.tsx` & `StaffServiceExecutionDetailPage.tsx`: Thực hiện quy trình dịch vụ, ghi nhận các chi phí phụ thu phát sinh ngoài hợp đồng.
- `StaffCommissionPage.tsx` & `StaffPerformancePage.tsx`: Thống kê doanh số dịch vụ đã làm và hoa hồng tạm tính.

#### 🌸 Phân Hệ Khách Hàng (Customer Portal) - `src/pages/customer/`
- `CustomerDashboardPage.tsx`: Hiển thị số dư điểm tích lũy, hạng thành viên, lịch hẹn sắp tới.
- `CustomerAppointmentListPage.tsx` & `CustomerAppointmentBookingPage.tsx`: Đặt chỗ trực tuyến chọn dịch vụ và nhân viên yêu thích.
- `CustomerInvoiceListPage.tsx` & `CustomerInvoiceDetailPage.tsx`: Kiểm tra lịch sử hóa đơn thanh toán và số tiền đã chi tiêu.
- `CustomerVoucherListPage.tsx`: Quản lý kho voucher cá nhân khả dụng cho lần làm đẹp tiếp theo.
- `CustomerFeedbackPage.tsx` & `CustomerComplaintPage.tsx`: Phản hồi chất lượng phục vụ hoặc gửi yêu cầu xử lý khiếu nại.

---

## 📐 Cấu Trúc Layouts Riêng Biệt (`src/layouts/`)

Mỗi phân hệ giao diện được áp dụng một bộ Layout Layouts khác nhau nhằm phản ánh đúng ngữ cảnh sử dụng:

1. **`ManagerLayout`**:
   - Sử dụng tông màu tối sang trọng làm chủ đạo.
   - Thanh điều hướng bên trái được bố trí khoa học phục vụ quản trị diện rộng.
2. **`ReceptionistLayout`**:
   - Thiết kế dạng bảng điều khiển nghiệp vụ sáng sủa, trực quan.
   - Thao tác nhanh được đưa lên thanh tiêu đề để giảm thiểu thời gian xử lý giao dịch.
3. **`StaffLayout`**:
   - Tối ưu hóa kích thước hiển thị trên máy tính bảng hoặc điện thoại.
   - Sử dụng các phần tử chạm phản hồi nhanh cho thợ làm tóc đang làm việc tại tiệm.
4. **`CustomerLayout`**:
   - Bố cục dạng cổng thông tin khách hàng hiện đại.
   - Thanh menu ngang phía trên giúp tối giản giao diện, tập trung vào hành vi đặt dịch vụ và tra cứu thông tin ưu đãi.

---

## 🧪 Quy Trình Kiểm Thử Đóng Gói (Build Verification)

Dự án đã được biên dịch và kiểm tra tính toàn vẹn mã nguồn:

```powershell
# Chạy biên dịch kiểm thử trong thư mục frontend
npm run build
```

*Quy trình đóng gói đã hoàn tất thành công, không gặp lỗi cú pháp TypeScript hoặc các vấn đề xung đột thư viện.*
