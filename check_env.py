import torch
import torchvision
import timm

print("Python Environment is ready!")
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA (GPU) available: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"Using GPU: {torch.cuda.get_device_name(0)}")
else:
    print("Using CPU (Make sure to install PyTorch with CUDA support if you have an NVIDIA GPU)")