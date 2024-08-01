import pandas as pd

file1_data = pd.read_csv(
    "D:\\Prowu\\data\\adnormal\\all1.csv")
file2_data = pd.read_csv(
    "D:\\SP_TrainData\\adnormal\\smart_air.csv")
file3_data = pd.read_csv(
    "D:\\SP_TrainData\\adnormal\\merged_dataset.csv")
# file1_data = file12_data.sample(frac =.01)
file1_data['timestamp'] = pd.to_datetime(file1_data['timestamp'], format='%Y-%m-%d %H:%M:%S.%f')
# file2_data['timestamp'] = pd.to_datetime(file2_data['timestamp'], format='%m/%d/%Y %H:%M') #merged_dataset ไฟลท์
file2_data['timestamp'] = pd.to_datetime(file2_data['timestamp'], format='%d/%m/%Y %H:%M') #smart air ph.d book
file3_data['timestamp'] = pd.to_datetime(file3_data['timestamp'], format='%m/%d/%Y %H:%M') #smart air ph.d book
new_data = file1_data.copy()

# สร้างเซ็ตเปล่าเพื่อเก็บ index ของแถวที่ยังไม่ได้รับการจับคู่
unmatched_rows = set(file1_data.index)
unmatched2_rows = set(file1_data.index)
unmatched3_rows = set(file1_data.index)
# ลูปเพื่อจับคู่ในช่วงทุก 2 นาที
for index, row in file1_data.iterrows():
    print("!!!!!!!!!!!!!!!")
    timestamp = row['timestamp']
    minute = timestamp.minute
    minute = (minute // 2) * 2 #ปัดเศษของค่านาทีให้เป็นเวลาที่หาร 5 ลงตัวและคูณกลับด้วย 5 เพื่อให้เวลาเป็นช่วงทุก 5 นาที.
    timestamp = timestamp.replace(minute=minute) #แทนค่านาทีใน timestamp ด้วยค่า minute ที่ถูกปรับแล้วเพื่อให้ timestamp เป็นช่วงทุก 5 นาที.
    matching_row = file2_data[
        (file2_data['timestamp'].dt.day == timestamp.day) & (file2_data['timestamp'].dt.hour == timestamp.hour) &
        (file2_data['timestamp'].dt.minute == timestamp.minute)] #ใช้ DataFrame file2_data เพื่อค้นหาแถวที่ตรงกับ timestamp ที่ถูกปรับแล้วใน file1_data โดยเปรียบเทียบชั่วโมง (hour) และนาที (minute) ของ timestamp.
    if not matching_row.empty:
        new_data.at[index, 'indoor1'] = matching_row.iloc[0]['IndoorTemperature']
        unmatched_rows.remove(index)

# ลูปเพื่อจับคู่ในช่วงทุก 5 นาที
for index, row in file1_data.iterrows():
    print("!!!!!!!!!!!!!!!")
    timestamp = row['timestamp']
    minute = (timestamp.minute // 5) * 5  # ปัดเศษของค่านาทีให้เป็นเวลาที่หาร 5 ลงตัว
    timestamp = timestamp.replace(minute=minute)  # แทนค่านาทีใน timestamp ด้วยค่า minute ที่ถูกปรับแล้วเพื่อให้ timestamp เป็นช่วงทุก 5 นาที
    matching_row = file3_data[
        (file3_data['timestamp'].dt.day == timestamp.day) & (file3_data['timestamp'].dt.hour == timestamp.hour) &
        (file3_data['timestamp'].dt.minute == timestamp.minute)]
    if not matching_row.empty:
        new_data.at[index, 'outdoor1'] = matching_row.iloc[0]['Out1_Temp_Mean']
        # new_data.at[index, 'time'] = timestamp
        unmatched3_rows.remove(index)

# ลูปเพื่อจับคู่ในช่วงทุก 5 นาที
for index, row in file1_data.iterrows():
    timestamp = row['timestamp']
    print("***********")
    minute = (timestamp.minute // 5) * 5  # ปัดเศษของค่านาทีให้เป็นเวลาที่หาร 5 ลงตัว
    timestamp = timestamp.replace(minute=minute)  # แทนค่านาทีใน timestamp ด้วยค่า minute ที่ถูกปรับแล้วเพื่อให้ timestamp เป็นช่วงทุก 5 นาที
    matching_row = file3_data[
        (file3_data['timestamp'].dt.day == timestamp.day) & (file3_data['timestamp'].dt.hour == timestamp.hour) &
        (file3_data['timestamp'].dt.minute == timestamp.minute)]
    if not matching_row.empty:
        new_data.at[index, 'outdoor2'] = matching_row.iloc[0]['Out2_Temp_Mean']
        # new_data.at[index, 'time2'] = timestamp
        unmatched2_rows.remove(index)



# บันทึก DataFrame ใหม่ที่มีคอลัมน์ Out1_Temp_Mean เพิ่มเข้าไป
new_data.to_csv(
    "D:\\Prowu\\data\\adnormal\\real12.csv",
    index=False)








