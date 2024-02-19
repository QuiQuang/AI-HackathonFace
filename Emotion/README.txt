# Giới thiệu các tập tin trong thư mục:
|_> emotion_pred.ipynb: tập tin dùng để đưa ra kết quả dự đoán.
|_> emotion_train.ipynb: tập tin dùng để huấn luyện mô hình.
|_> model_emotion.h5: tập tin lưu trữ kết quả các trọng số của mô hình sau khi huấn luyện.
|_> requirements.txt

# Các thư viện của python cần tải về:
** Cú pháp **
    |_> pip install -r requirements.txt

# Các đường dẫn cần sửa đổi của tập tin emotion_train:
|_> Tên biến 'data_cater': Đường dẫn dẫn đến thư mục có chứa ảnh huấn luyện được phân từng sub-folder (theo emotion).
|_> Tên biến 'data_link' : Đường dẫn dẫn đến thư mục có chứa ảnh huấn luyện không cần phân nhóm. 
|_> Tên biến 'label_file_csv': Đường dẫn dẫn đến của tập tin csv chứa nhãn huấn luyện.
|_> Tên biến 'model_name' : Tên model để train và lưu.

# Các đường dẫn cần sửa đổi của tập tin emotion_pred:
|_> Tên biến 'bbox_label_file': Đường dẫn dẫn đến của tập tin csv chứa nhãn bbox đã được dự đoán.
|_> Tên biến 'link_folder': Đường dẫn dẫn đến của thư mục có chứa các ảnh cần dự đoán.
|_> Tên biến 'model_name' : Tên model để dự đoánn.

# Cách chạy emotion_train:
|_> Bước 1: Mở thư mục có chứa tập tin cần chạy.
|_> Bước 2: Nhấp vào tâp tin cần chạy.
|_> Bước 3: Thay đổi các đường dẫn đã đề cập ở trên.
|_> Bước 4: Chạy từng cell đến khi đến markdown LOAD FILE thì:
** Lưu ý **
    |_> Chỉ chạy 1 trong 2 cell LOAD FILE tuỳ theo cấu trúc folder được định nghĩa như trên (với folder đã được phân loại thì chạy LOAD DATA FROM CATERGORRIZED-FOLDER, còn với folder chưa được phân loại nhưng mà có file label thì chạy LOAD DATA FROM UNCATERGORRIZED-FOLDER)
    |_> Cấu trúc của 2 folder như sau:
        |_> Folder đã được phân loại:
    data
    ├─ Anger              
    ├─ Disgust                    
    ├─ Fear             
    ├─ Happiness         
    ├─ Neutral    
    ├─ Sadness             
    └─ Surprise   
       
        |_> Folder chưa được phân loại:
    data
    ├─ img1.png             
    ├─ img2.png 
    ├─ img3.png         
    ├─ img4.png         
    ├─ img5.png   
    ├─ img6.png            
    └─ ...     
|_> Bước 5: Đợi kết quả.
|_> Bước 6: Model sẽ tự động lưu theo tên tùy chỉnh.


# Cách chạy emotion_pred:
|_> Bước 1: Mở thư mục có chứa tập tin cần chạy.
|_> Bước 2: Nhấp vào tâp tin cần chạy.
|_> Bước 3: Thay đổi các đường dẫn đã đề cập ở trên.
|_> Bước 4: Nhấn run all.
|_> Bước 5: Chọn ngôn ngữ hỗ trợ là python.
|_> Bước 6: Đợi kết quả.
** Lưu ý **
    |_> Cần phải chạy tập tin emotion_train trước để có kết quả của mô hình (hoặc sử dụng mô hình model_emotion.h5) để có thể chạy tập tin emotion_pred.



