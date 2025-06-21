import torch

torch

try:
    if torch.cuda.is_available():
        print("CUDA is available. PyTorch is using CUDA.")
    else:
        print("CUDA is NOT available. PyTorch is installed but not using CUDA.")
except ImportError:
    print("PyTorch is NOT installed.")

print(torch.cuda.get_device_name(0))