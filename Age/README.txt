# Giới thiệu các tập tin trong thư mục:
|_> age_pred.ipynb: tập tin dùng để đưa ra kết quả dự đoán.
|_> age_train.ipynb: tập tin dùng để huấn luyện mô hình.
|_> model_age.h5: tập tin lưu trữ kết quả các trọng số của mô hình sau khi huấn luyện.

# Các thư viện của python cần tải về:
|_> Thư viện numpy
|_> Thư viện pandas
|_> Thư viện os
|_> Thư viện keras
|_> Thư viện sklearn
|_> Thư viện matplotlib
|_> Thư viện ast
|_> Thư viện tqdm
** Cú pháp **
    |_> pip install [tên thư viện]

# Các đường dẫn cần sửa đổi của tập tin age_train:
|_> Tên biến 'path_to_data': Đường dẫn dẫn đến của thư mục có chứa ảnh huấn luyện.
|_> Tên biến 'path_to_label': Đường dẫn dẫn đến của tập tin csv chứa nhãn huấn luyện.

# Các đường dẫn cần sửa đổi của tập tin age_pred:
|_> Tên biến 'path_to_bbox': Đường dẫn dẫn đến của tập tin csv chứa nhãn bbox đã được dự đoán.
|_> Tên biến 'path_to_test_data': Đường dẫn dẫn đến của thư mục có chứa các ảnh cần dự đoán.

# Cách chạy cả 2 tập tin age_pred và age_train:
|_> Bước 1: Mở thư mục có chứa tập tin cần chạy.
|_> Bước 2: Nhấp vào tâp tin cần chạy.
|_> Bước 3: Thay đổi các đường dẫn đã đề cập ở trên.
|_> Bước 4: Nhấn run all.
|_> Bước 5: Chọn ngôn ngữ hỗ trợ là python.
|_> Bước 6: Đợi kết quả.
** Lưu ý **
    |_> Cần phải chạy tập tin age_train trước để có kết quả của mô hình (model_age.h5) để có thể chạy tập tin age_pred.


