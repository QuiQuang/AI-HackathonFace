import json
import pandas as pd
# List of CSV files to be merged
path_to_emotion = 'Emotion/emotion_result.csv'
path_to_masked = 'Masked/masked_result.csv'
path_to_race = 'Race/race_result.csv'
path_to_skintone = 'Skintone/skintone_result.csv'
path_to_gender = 'Gender/gender_result.csv'
path_to_age = 'Age/age_result.csv'

csv_files = [path_to_emotion, path_to_masked, path_to_race, path_to_skintone, path_to_gender, path_to_age]

# Initialize merged_df with the sorted df_image_id
merged_df = pd.read_csv(csv_files[0])

# Merge other DataFrames based on 'file_name'
for index in range(1,len(csv_files)):
    try:
        df_temp = pd.read_csv(csv_files[index])
        merged_df = pd.merge(merged_df, df_temp, on=['file_name', 'bbox'], how='inner')
    except FileNotFoundError:
        print(f"Warning: File {csv_files[index]} not found.")

# Đọc dữ liệu từ tệp JSON
path_to_json = 'D:/Contest/AIFace/file_name_to_image_id.json'
with open(path_to_json, 'r') as json_file:
    file_name_to_id = json.load(json_file)

# Thêm cột 'id' vào merged_df dựa trên giá trị 'file_name'
merged_df['image_id'] = merged_df['file_name'].map(file_name_to_id)
merged_df = merged_df.sort_values(by='image_id')

# Save the final merged DataFrame to a CSV file
# Define the desired order of columns
desired_column_order = ['file_name', 'bbox', 'image_id', 'race', 'age', 'emotion', 'gender', 'skintone', 'masked']

# Reorder the columns based on the desired order
merged_df = merged_df[desired_column_order]

merged_df.to_csv('answer.csv', index=False)
print(merged_df)
