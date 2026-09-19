import os
import re

img_dir = "data/images"  # โฟลเดอร์เก็บรูป

# ดึงรายชื่อไฟล์ทั้งหมดมาเรียงลำดับตามตัวเลข
def extract_num(filename):
  match = re.search(r"(\d+)", filename)
  return int(match.group(1)) if match else 0


if os.path.exists(img_dir):
    files = sorted(os.listdir(img_dir), key=extract_num)

    # วนลูปเปลี่ยนชื่อทีละไฟล์
    for filename in files:
        match = re.search(r"(\d+)", filename) #ค้นหาว่า พบชื่อไฟล์ไหม
        print(match)
        if match:
            num = int(match.group(1))
            ext = os.path.splitext(filename)[1]  # ดึงนามสกุลเดิม (เช่น .jpg, .png)

            old_path = os.path.join(img_dir, filename)
            new_filename = f"{num:04d}{ext}"  # แปลงเป็น 0001.jpg
            new_path = os.path.join(img_dir, new_filename)

            os.rename(old_path, new_path)
            print(f"เปลี่ยนชื่อ: {filename} --> {new_filename}")

    print("--- เปลี่ยนชื่อไฟล์เสร็จแล้ว ---")
else :
    print(f"หา path :{img_dir} ไม่เจอ ")