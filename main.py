import os
import io
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
import timm
import torch
from torchvision import transforms
import gdown

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "resnet50_road_risk.pth1")
ONNX_PATH = os.path.join(MODEL_DIR, "resnet50_road_risk.onnx")
GOOGLE_DRIVE_FILE_ID = "11Vff0R2iX3i2Z3JneXSYMY42Tr7mvwvr"
os.makedirs(MODEL_DIR, exist_ok=True)

# 1. โหลดโมเดลจาก Google Drive มาเก็บไว้ที่ Host (ถ้ายังไม่มี)
if not os.path.exists(MODEL_PATH):
    print("⏳ กำลังดาวน์โหลดไฟล์โมเดลจาก Google Drive ลง Host...")
    url = f"https://drive.google.com/uc?id={GOOGLE_DRIVE_FILE_ID}"
    gdown.download(url, MODEL_PATH, quiet=False)
    print("✅ ดาวน์โหลดโมเดลลง Host สำเร็จ!")

# 2. แปลงไฟล์ .pth บน Host ให้เป็น .onnx เพื่อให้เบราว์เซอร์นำไปรันบนเครื่องผู้ใช้ได้
if not os.path.exists(ONNX_PATH):
    print("⏳ กำลังแปลงโมเดลเป็น ONNX (แบบรวมไฟล์เดียว)...")
    device = torch.device("cpu")
    model = timm.create_model("resnet50", pretrained=False, num_classes=1)
    model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
    model.eval()

    dummy_input = torch.randn(1, 3, 224, 224)
    
    # เพิ่มการบังคับ export แบบไม่แยก external data (เก็บบันทึกในไฟล์เดียว)
    torch.onnx.export(
        model, 
        dummy_input, 
        ONNX_PATH, 
        input_names=['input'], 
        output_names=['output'],
        export_params=True,
        do_constant_folding=True,
        dynamo=False # บังคับใช้ exporter ตัวเก่าเพื่อไม่ให้แยกไฟล์ data
    )
    print("✅ แปลงโมเดลเป็น ONNX สำเร็จ!")
# ส่งหน้าเว็บ HTML
@app.get("/")
async def read_index():
    return FileResponse("frontEnd/index.html")

# ส่งไฟล์โมเดล (.onnx) ที่เก็บอยู่บน Host ให้เบราว์เซอร์ของผู้ใช้ดาวน์โหลดไปรันที่เครื่องตัวเอง
@app.get("/api/model")
async def get_model():
    if os.path.exists(ONNX_PATH):
        return FileResponse(ONNX_PATH, media_type="application/octet-stream", filename="resnet50_road_risk.onnx")
    return JSONResponse({"success": False, "error": "Model not found on host"}, status_code=404)