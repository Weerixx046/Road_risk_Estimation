import os
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import io
import timm
import torch
from PIL import Image
from torchvision import transforms
import gdown

app = FastAPI()

# เปิด CORS เพื่อให้หน้าเว็บยิง API ข้ามมากลางคันได้
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📌 ตั้งค่าเส้นทางและดาวน์โหลดโมเดลจาก Google Drive อัตโนมัติถ้ายังไม่มีในเครื่อง
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "resnet50_road_risk.pth")
GOOGLE_DRIVE_FILE_ID = "1Gh9giAaGAOmHYheMcNBfHaF8nKEnuMTz"

os.makedirs(MODEL_DIR, exist_ok=True)

if not os.path.exists(MODEL_PATH):
    print("⏳ กำลังดาวน์โหลดไฟล์โมเดลจาก Google Drive...")
    url = f"https://drive.google.com/uc?id={GOOGLE_DRIVE_FILE_ID}"
    gdown.download(url, MODEL_PATH, quiet=False)
    print("✅ ดาวน์โหลดโมเดลสำเร็จ!")

# โหลดโมเดล ResNet-50 ที่ดาวน์โหลดมาเสร็จแล้วมารอไว้
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = timm.create_model("resnet50", pretrained=False, num_classes=1)
model.load_state_dict(
    torch.load(MODEL_PATH, map_location=device)
)
model.to(device)
model.eval()

# Transform สำหรับรูปที่จะเอามาทาย
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Response file html
@app.get("/")
async def read_index():
    return FileResponse("frontEnd/index.html")

# รับไฟล์จากส่วนหน้าบ้าน
@app.post("/api/predict")
async def predict_risk(file: UploadFile = File(...)):
    # 1. อ่านไฟล์ภาพที่ผู้ใช้อัปโหลดเข้ามา
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    # 2. แปลงภาพเป็น Tensor แล้วยิงเข้าโมเดล
    image_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(image_tensor)
        score = float(output.squeeze().item())

    # ปัดเศษไม่ให้ทศนิยมยาวเกินไป
    score = round(score, 2)

    # 3. ส่งผลลัพธ์กลับไปในรูปแบบ JSON Response
    return {"success": True, "filename": file.filename, "risk_score": score}