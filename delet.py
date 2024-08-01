import pandas as pd

# กำหนดที่อยู่ของไฟล์ CSV
csv_file_path = "D:\\Prowu\\data\\adnormal\\all\\data1.csv"

# อ่านไฟล์ CSV
df = pd.read_csv(csv_file_path)



# ลบคอลัมน์ที่ต้องการ
columns_to_drop = ['768', '769', '770', '771', '772', '773', '774', '775', '776', '777', '778', '779', '780', '781', '782', '783']
df = df.drop(columns=columns_to_drop)



# สร้างไฟล์ CSV ใหม่หลังจากการลบแถวที่มีค่าว่างและคอลัมน์ที่ต้องการ
output_csv_path = "D:\\Prowu\\data\\adnormal\\all\\data_filtered.csv"
df.to_csv(output_csv_path, index=False)
