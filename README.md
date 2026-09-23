# 🧮 Ứng dụng Máy tính Khoa học Mở rộng (PyQt6 Scientific Calculator)

Một ứng dụng máy tính cá nhân trên Desktop được xây dựng hoàn toàn bằng **Python** và thư viện **PyQt6**. Ứng dụng không chỉ cung cấp các phép tính cơ bản mà còn tích hợp các hàm toán học nâng cao, giao diện Responsive (co giãn linh hoạt) và cơ chế **bắt lỗi đầu vào (Input/Math Error Handling)** cực kỳ chặt chẽ.

![Mô phỏng giao diện](https://via.placeholder.com/800x400.png?text=B%E1%BA%A1n+c%C3%B3+th%E1%BB%83+ch%C3%A8n+%E1%BA%A3nh+ch%E1%BB%A5p+m%C3%A0n+h%C3%ACnh+app+v%C3%A0o+%C4%91%C3%A2y)

---

## ✨ Tính năng nổi bật

### 1. Phép toán đa dạng
- **Cơ bản:** Cộng (+), Trừ (-), Nhân (*), Chia (/).
- **Khoa học:** Căn bậc 2 (√), Bình phương (x²), Lũy thừa (^), Lượng giác (sin, cos, tan), Logarit (log), Hằng số Pi (π).
- **Hỗ trợ dấu ngoặc:** `(` và `)` để ưu tiên thứ tự thực hiện phép tính.

### 2. Giao diện thông minh (Responsive UI)
- Giao diện được thiết kế tự động co giãn (Auto-scale), không bị bẹp hoặc vỡ layout khi thay đổi kích thước cửa sổ.
- Phân chia Layout rõ ràng: Tỷ lệ 65% cho khu vực bàn phím và 35% cho khu vực **Lịch sử tính toán**.

### 3. Bắt lỗi toàn diện (Error Handling)
- **Bắt lỗi Input (Đầu vào):** 
  - Khóa nhập liệu từ bàn phím (tránh ký tự lạ).
  - Tự động thay thế toán tử (VD: Nhập `+` rồi `*` máy tự đổi thành `*`).
  - Không cho phép nhập 2 dấu chấm thập phân trong một số (VD: chặn `5.5.5`).
  - Tự động đóng dấu ngoặc nếu người dùng quên (VD: `sin(90` ➔ `sin(90)`).
- **Bắt lỗi Tính toán:**
  - Chặn lỗi chia cho 0 (`ZeroDivisionError`).
  - Chặn tính toán sai miền giá trị (VD: Căn bậc 2 của số âm - `ValueError`).
  - Xử lý trôi sai số thập phân của Python (VD: `0.1 + 0.2` sẽ hiển thị chính xác là `0.3` thay vì `0.30000000004`).

---

## 🛠 Tiền quyết & Cài đặt

Yêu cầu máy tính của bạn đã cài đặt sẵn [Python 3.x](https://www.python.org/).
