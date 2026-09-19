from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import io
import timm
import torch
from PIL import Image
from torchvision import transforms

app = FastAPI()

# เปิด CORS เพื่อให้หน้าเว็บยิง API ข้ามมากลางคันได้ (กรณีรันคนละพอร์ตตอน dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# โหลดโมเดล ResNet-50 ที่เทรนเสร็จแล้วมารอไว้
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = timm.create_model("resnet50", pretrained=False, num_classes=1)
model.load_state_dict(
    torch.load("models/resnet50_road_risk.pth", map_location=device)
)
model.to(device)
model.eval()

# Transform สำหรับรูปที่จะเอามาทาย
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

#respone file html
@app.get("/")
async def read_index():
    return FileResponse("../frontEnd/index.html")

#รับไฟล์จากส่วนหน้าบ้าน
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