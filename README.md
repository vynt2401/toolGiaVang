Công cụ lấy giá vàng PNJ
Đây là một công cụ Python đơn giản để lấy giá vàng từ trang web PNJ và xuất dữ liệu ra tệp Excel.

1. Tải dự án về máy
Bạn có thể tải dự án bằng cách clone repository từ GitHub. Mở Terminal hoặc Command Prompt và chạy lệnh sau:

Bash

git clone https://github.com/vynt2401/toolGiaVang.git
2. Cài đặt các thư viện cần thiết
Dự án này sử dụng các thư viện Python được liệt kê trong tệp requirements.txt.
Đầu tiên, hãy di chuyển vào thư mục dự án:

Bash

cd toolGiaVang
Sau đó, chạy lệnh sau để cài đặt tất cả các thư viện:

Bash

pip install -r requirements.txt
Ngoài ra, dự án sử dụng playwright để lấy dữ liệu. Bạn cần cài đặt thêm trình duyệt bằng lệnh sau:

Bash

playwright install
3. Chạy chương trình
Chạy tệp main.py để lấy giá vàng và lưu vào tệp Excel:

Bash

python main.py
Chương trình sẽ tự động tạo một tệp Excel có tên gia_vang_pnj.xlsx trong cùng thư mục với chương trình.

Nếu tệp đã tồn tại, dữ liệu mới sẽ được thêm vào cuối tệp.

Các tính năng chính
Lấy dữ liệu tự động: Tự động truy cập trang web PNJ để lấy giá vàng.

Xuất ra Excel: Lưu dữ liệu vào tệp gia_vang_pnj.xlsx với các cột: loai vang, mua vao, ban ra, nguon, days.

Dễ dàng sử dụng: Chạy trực tiếp từ dòng lệnh.

Ghi chú
Đảm bảo bạn có kết nối Internet để chương trình có thể truy cập trang web PNJ.

Bạn có thể thay đổi tên tệp xuất trong biến OUTPUT_FILE trong main.py nếu muốn.
