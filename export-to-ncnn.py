"""
Use NCNN on Raspberry Pi:
Out of all the model export formats supported by Ultralytics, NCNN delivers the best
inference performance when working with Raspberry Pi devices because NCNN is highly
optimized for mobile/ embedded platforms (such as ARM architecture).

Convert Model to NCNN and Run Inference:
"""

from ultralytics import YOLO

# Load a YOLO26n PyTorch model
model = YOLO("yolo11n.pt")

# Export the model to NCNN format
model.export(format="ncnn")  # creates 'yolo11n_ncnn_model'

# Load the exported NCNN model
#ncnn_model = YOLO("yolo11n_ncnn_model")