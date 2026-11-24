import torch
from torchvision.models.detection import (
    fasterrcnn_resnet50_fpn,
    FasterRCNN_ResNet50_FPN_Weights
)
from PIL import Image
from torchvision.transforms import functional as F

model = fasterrcnn_resnet50_fpn(
    weights=FasterRCNN_ResNet50_FPN_Weights.DEFAULT
)
model.eval()

img = Image.open("image.jpg").convert("RGB")
result = model([F.to_tensor(img)])

print("Detected Objects:")
print(result[0]["labels"])
