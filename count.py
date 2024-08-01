import pandas as pd

# โหลดข้อมูลจากไฟล์ CSV
file_path = 'D:\\Prowu\\data\\data1.csv'  # เปลี่ยนเส้นทางไฟล์ตามที่คุณเก็บไฟล์ CSV
df = pd.read_csv(file_path)

# สร้างตัวแปรเพื่อเก็บผลลัพธ์
count_dict = {}

# นับข้อมูลในคอลัมน์ 'label'
for label in df['label']:
    if label in count_dict:
        count_dict[label] += 1
    else:
        count_dict[label] = 1

# แสดงผลลัพธ์
for label, count in count_dict.items():
    print(f'Label {label}: {count} ครั้ง')
