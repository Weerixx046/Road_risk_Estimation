import os
import pandas as pd

# 1. โหลดไฟล์ CSV ใหม่ และกำหนดโฟลเดอร์รูป
csv_file_path = "data/train_dataset.csv"
img_dir = "data/images"
df = pd.read_csv(csv_file_path)
if os.path.exists(img_dir) and os.path.exists(csv_file_path):
    f = pd.read_csv(csv_file_path)

    # 2. ดึงรายชื่อไฟล์จริงในโฟลเดอร์มาเก็บไว้เป็น Set
    local_files = set(os.listdir(img_dir))

    # 3. กรองเฉพาะแถวที่ image_name มีอยู่จริงในโฟลเดอร์
    matched_df = df[df["image_name"].isin(local_files)].copy()
    # 4. นับจำนวนและแสดงผล
    matched_count = len(matched_df)
    print(f"จำนวนไฟล์ที่ตรงกันระหว่าง CSV กับโฟลเดอร์จริง: {matched_count} ไฟล์")

    # (ทางเลือก) บันทึกทับไฟล์ CSV ใหม่เฉพาะตัวที่กรองแล้วว่ามีรูปอยู่จริงชัวร์ๆ
    matched_df.to_csv("train_dataset.csv", index=False, encoding="utf-8")
else:
    print("หาไฟล์ไม่เจอ")