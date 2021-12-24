# Unique UET

Website bán hàng đơn giản sử dụng nhằm mục đích bán các loại hàng hóa mỹ phẩm thường dùng. Viết bằng [python Django](https://www.djangoproject.com/)

---

## Project Summary

Website hiển thị danh sách sản phẩm. Người dùng sau đó có thể đăng ký / đăng nhập. Sau khi đăng nhập vào hệ thống, người dùng có thể thêm bớt sản phẩm vào giỏ hàng và chọn số lượng muốn mua và lựa chọn hình thức thanh toán.

---

## Build và chạy project

Để chạy project, trước hết ta cần có Python3 ở trên thiết bị. (Phiên bản sử dụng trong quá trình development: [Python 3.9.7](https://www.python.org/downloads/release/python-397/))

Chúng tôi khuyên bạn nên tạo 1 virtual environment để lưu riêng các dependencies của project. Bạn có thể cài virtualenv từ python bằng cách sử dụng:

```
pip install virtualenv
```

Sau đó, bạn có thể download repo chứa project này về, sử dụng terminal ở trong thư mục chứa repo, và tạo virtual environment bằng cách:

```
virtualenv env
```

Nếu phiên bản Python chính của máy bạn không phải Python 3.9, bạn có thể cài phiên bản python mới (và chọn **KHÔNG** thêm đường dẫn vào Environment Variable / PATH). Sau đó, bạn có thể tạo virtualenv bằng câu lệnh

```
virtualenv env -p {path_to_python_file}
```

Câu lệnh trên sẽ tạo folder env ở trong thư mục ban đầu của repo. Bạn có thể kích hoạt virtualenv bằng câu lệnh

```
env\Scripts\activate
```
cho Windows, hoặc

```
env/bin/activate
```
cho Linux.


Sau đó, ta có thể thực hiện cài các dependency để chạy repo:

```
pip install -r requirements.txt
```

Sau đó, ta có thể mở server bằng:

```
python manage.py runserver
```

**Note:** Để Stripe có thể chạy được, bạn cần phải thay đổi API key thành key của bạn trong file .env ở thư mục ban đầu

---
# Xin cảm ơn!
