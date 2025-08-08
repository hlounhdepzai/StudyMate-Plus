# app.py

# Import các thư viện cần thiết từ Flask
from flask import Flask, render_template, request, redirect, url_for

# Khởi tạo ứng dụng Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'bi-mat-cua-ban!' # Một khóa bí mật để bảo vệ ứng dụng

# Định nghĩa route (đường dẫn) cho trang chủ
@app.route('/', methods=['GET', 'POST'])
def index():
    # Nếu người dùng gửi dữ liệu lên (nhấn nút "Tham gia")
    if request.method == 'POST':
        # Lấy tên phòng từ form người dùng nhập
        room_id = request.form.get('room_id')
        if room_id:
            # Nếu có tên phòng, chuyển hướng người dùng đến phòng đó
            return redirect(url_for('room', room_id=room_id))
    # Nếu là lần đầu truy cập (GET), chỉ hiển thị trang chủ
    return render_template('index.html')

# Định nghĩa route cho phòng học, ví dụ: /room/lop-toan
@app.route('/room/<string:room_id>')
def room(room_id):
    # Hiển thị trang phòng học và truyền tên phòng vào để hiển thị
    return render_template('room.html', room_id=room_id)

# Dòng này để đảm bảo server chỉ chạy khi file này được thực thi trực tiếp
if __name__ == '__main__':
    app.run(debug=True)
