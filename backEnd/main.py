from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import io
import timm
import torch
import torch.nn as nn  # เพิ่ม import ตัวนี้สำหรับสร้าง Custom Head
from PIL import Image
from torchvision import transforms

MODEL_DIR = "../models/resnet50_road_risk.pt"
FONT_END_DIR = "../frontEnd/index.html"
app = FastAPI()

# เปิด CORS เพื่อให้หน้าเว็บยิง API ข้ามมากลางคันได้
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 1. โหลดโครงสร้างโมเดลให้ตรงกับตอนเทรน
model = timm.create_model("resnet50", pretrained=False, num_classes=0)
model.fc = nn.Sequential(
    nn.Flatten(),
    nn.Dropout(p=0.4),
    nn.Linear(model.num_features, 1)
)

# 2. โหลดน้ำหนักเข้าไป (เพิ่ม weights_only=False ป้องกัน Error ใน PyTorch เวอร์ชันใหม่)
model.load_state_dict(
    torch.load(MODEL_DIR, map_location=device, weights_only=False)
)
model.to(device)
model.eval()

# Transform สำหรับรูปที่จะเอามาทาย
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# รับ Request หน้าเว็บ
@app.get("/")
async def read_index():
    # ปรับ Path ให้เป็นการรันจาก Root Directory
    return FileResponse(FONT_END_DIR)

# รับไฟล์จากหน้าบ้านเพื่อประเมินความเสี่ยง
@app.post("/api/predict")
async def predict_risk(file: UploadFile = File(...)):
    # อ่านไฟล์ภาพที่ผู้ใช้อัปโหลดเข้ามา
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    # แปลงภาพเป็น Tensor แล้วยิงเข้าโมเดล
    image_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(image_tensor)
        score = float(output.squeeze().item())

    # ปัดเศษทศนิยม
    score = round(score, 2)

    return {"success": True, "filename": file.filename, "risk_score": score}