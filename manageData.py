import json
import os
import pandas as pd
# 1. กำหนด Path ของไฟล์ CSV และโฟลเดอร์รูปภาพ
csv_file_path = "data/labeled_images.csv"  
img_dir = "data/images"

# 2. ตรวจสอบว่ามีไฟล์ CSV อยู่จริงไหมก่อนอ่าน
if os.path.exists(csv_file_path):
  df = pd.read_csv(csv_file_path)
  
  df["temp_file_num"] = (
    df["image"].apply(lambda x: os.path.basename(str(x)).split("-")[-1])
    .str.extract(r"(\d+)")
    .astype(int)
  )
  #เรียงชื่อ file
  df = df.sort_values(by="temp_file_num", ascending=True)

  # 3. วนลูปดึงข้อมูล และจับคู่กันระหว่า xxxx.jpg กับ score
  dataset_pairs = []
  for index, row in df.iterrows():

    # แปลงตัวเลขจาก temp_file_num ให้เป็นรูปแบบ 0001.jpg (เติม 0 ข้างหน้าให้ครบ 4 หลัก)
    file_num = int(row["temp_file_num"])
    row_image = f"{file_num:04d}.jpg"

    raw_risk = str(row["risk_score"])

    # แกะตัวเลขจาก JSON string
    extracted_num = 0
    try:
      cleaned_str = raw_risk.replace('""', '"')
      data = json.loads(cleaned_str)
      if isinstance(data, list) and len(data) > 0:
        extracted_num = data[0].get("number", 0)
    except:
      extracted_num = 0

    # เก็บข้อมูลที่จับคู่กันแล้ว
    dataset_pairs.append(
      { "image_name": row_image, "score": extracted_num}
    )
# 3. แปลงเป็น DataFrame ใหม่ที่สะอาดพร้อมใช้งานหรือบันทึก
  clean_df = pd.DataFrame(dataset_pairs)
  print(clean_df)
  output_csv_path = "train_dataset.csv"
  clean_df.to_csv(output_csv_path, index=False, encoding="utf-8")
else:
  print(
      f"⚠️ ไม่พบไฟล์ CSV ที่ path: {csv_file_path} กรุณาตรวจสอบชื่อไฟล์อีกครั้งครับ"
  )