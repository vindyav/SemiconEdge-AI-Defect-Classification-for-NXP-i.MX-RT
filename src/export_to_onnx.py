import torch
from model import MobileNetV3Small

# Load trained model
model = MobileNetV3Small(num_classes=8)
model.load_state_dict(torch.load("trained_model.pth", map_location="cpu"))
model.eval()

# Dummy input for ONNX export
dummy_input = torch.randn(1, 1, 128, 128)

# Export to ONNX
torch.onnx.export(
    model,
    dummy_input,
    "models/baseline_model.onnx",
    opset_version=13,
    input_names=["input"],
    output_names=["output"],
    dynamic_axes=None
)

print("ONNX export successful. Model ready for NXP eIQ.")
