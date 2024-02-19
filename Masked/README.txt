# Giới thiệu các tập tin trong thư mục:
|_> Masked_Prediction.ipynb: tập tin dùng để đưa ra kết quả dự đoán.
|_> Masked_Training.ipynb: tập tin dùng để huấn luyện mô hình.
|_> Masked_Model_Best.h5: tập tin lưu trữ kết quả các trọng số của mô hình sau khi huấn luyện.

# Các thư viện của python cần tải về:
|_> Thư viện os
|_> Thư viện opencv-python
|_> Thư viện pandas
|_> Thư viện numpy
|_> Thư viện seaborn
|_> Thư viện matplotlib
|_> Thư viện tensorflow
|_> Thư viện pillow
|_> Thư viện scikit-learn
|_> Thư viện ipykernel
|_> Thư viện AST

** Cú pháp **
    |_> pip install [tên thư viện]

# Các đường dẫn cần sửa đổi của tập tin Masked_Training:
|_> Tên biến 'data_cater': Đường dẫn dẫn đến của thư mục có chứa ảnh huấn luyện, thư mục chính và 2 thư mục con masked và unmasked.
|_> Tên biến 'model_name': Đường dẫn dẫn đến của tập tin lưu trữ kết quả trọng số.

# Các đường dẫn cần sửa đổi của tập tin Masked_Prediction:
|_> Tên biến 'name_model': Đường dẫn dẫn đến của tập tin lưu trữ kết quả trọng số.
|_> Tên biến 'bbox_label_file': Đường dẫn dẫn đến của tập tin csv chứa nhãn huấn luyện.
|_> Tên biến 'link_folder': Đường dẫn dẫn đến của thư mục có chứa các ảnh cần dự đoán.

# Cách chạy cả 2 tập tin Masked_Prediction và Masked_Training:
|_> Bước 1: Mở thư mục có chứa tập tin cần chạy.
|_> Bước 2: Nhấp vào tâp tin cần chạy.
|_> Bước 3: Thay đổi các đường dẫn đã đề cập ở trên.
|_> Bước 4: Nhấn run all.
|_> Bước 5: Chọn ngôn ngữ hỗ trợ là python.
|_> Bước 6: Đợi kết quả.
** Lưu ý **
    |_> Cần phải chạy tập tin Masked_Training trước để có kết quả của mô hình (Masked_Model_Best.h5) để có thể chạy tập tin Masked_Prediction.


