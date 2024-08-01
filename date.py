# import pandas as pd
# from datetime import datetime

# # กำหนดวันที่เริ่มต้น
# start_date = datetime(2023, 10, 9)

# # อ่านไฟล์ CSV
# csv_file_path = "D:\\SP_TrainData\\adnormal\\data1.csv"  # ระบุที่อยู่ของไฟล์ CSV ของคุณ
# df = pd.read_csv(csv_file_path)

# # แปลงคอลัมน์ที่มีวันที่เป็น datetime
# df['timestamp'] = pd.to_datetime(df['timestamp'])

# # กรองข้อมูลเฉพาะที่มีวันที่มากกว่าหรือเท่ากับ start_date
# filtered_df = df[df['timestamp'] >= start_date]

# # แสดงผลลัพธ์
# print(filtered_df)

# # ระบุ path ที่ต้องการบันทึกไฟล์ CSV ใหม่
# output_csv_path = "D:\\SP_TrainData\\adnormal\\filtered_data.csv"

# # บันทึก DataFrame ที่ถูกกรองเป็นไฟล์ CSV ใหม่
# filtered_df.to_csv(output_csv_path, index=False)


# import pandas as pd

# # กำหนดที่อยู่ของไฟล์ CSV
# csv_file_path = "D:\\SP_TrainData\\adnormal\\alss11.csv"

# # อ่านไฟล์ CSV
# df = pd.read_csv(csv_file_path)

# # ตรวจสอบและลบแถวที่มีค่าว่างในคอลัมน์ 'outdoor'
# df = df.dropna(subset=['outdoor1'])

# # แสดงผลลัพธ์หลังจากลบแถวที่มีค่าว่าง
# print(df)

# # สร้างไฟล์ CSV ใหม่หลังจากการลบแถวที่มีค่าว่าง
# output_csv_path = "D:\\SP_TrainData\\adnormal\\data_filtered.csv"
# df.to_csv(output_csv_path, index=False)




