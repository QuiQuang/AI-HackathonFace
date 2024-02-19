# Giới thiệu các tập tin trong thư mục:
|_> skintone_pred.ipynb: tập tin dùng để đưa ra kết quả dự đoán.
|_> skintone_training.ipynb: tập tin dùng để huấn luyện mô hình.

# Các thư viện của python cần tải về:
|_> numpy
|_> pandas
|_> torch
|_> torchvision
|_> torchmetrics
|_> transformers
|_> pytorch_lightning
** Cú pháp **
    |_> pip install [tên thư viện]

# Các đường dẫn cần sửa đổi của tập tin skintone_training:
|_> Tên biến 'data_dir': Đường dẫn dẫn đến của thư mục có chứa ảnh huấn luyện.
|_> Tên biến 'label_dir': Đường dẫn dẫn đến của tập tin csv chứa nhãn huấn luyện.

# Các đường dẫn cần sửa đổi của tập tin age_pred:
|_> Tên biến 'bboxes_dir': Đường dẫn dẫn đến của tập tin csv chứa nhãn bbox đã được dự đoán.
|_> Tên biến 'data_dir': Đường dẫn dẫn đến của thư mục có chứa các ảnh cần dự đoán.
|_> Tên biến 'model_dir': Đường dẫn đến tập tin các trọng số của mô hình dự đoán.

# Cách chạy cả 2 tập tin skintone_pred và skintone_training:
|_> Bước 1: Mở thư mục có chứa tập tin cần chạy.
|_> Bước 2: Nhấp vào tâp tin cần chạy.
|_> Bước 3: Thay đổi các đường dẫn đã đề cập ở trên.
|_> Bước 4: Nhấn run all.
|_> Bước 5: Chọn ngôn ngữ hỗ trợ là python.
|_> Bước 6: Đợi kết quả.
** Lưu ý **
    |_> Cần phải chạy tập tin skintone_training trước để có kết quả của mô hình để có thể chạy tập tin skintone_pred.


