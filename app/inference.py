"""
inference.py
------------
Core inference pipeline for the Bangladeshi Taka Note Detection model.
Loads the YOLOv11 weights trained in Phase-1 and runs object detection
on a single image, returning class names, confidence scores, and
bounding box coordinates.
"""

import io
import os
from typing import List, Dict, Any

from PIL import Image
from ultralytics import YOLO

# Path to the Phase-1 trained weights. Can be overridden with an
# environment variable so the same code works locally and in Docker.
MODEL_PATH = os.getenv("MODEL_PATH", "models/best.pt")
CONFIDENCE_THRESHOLD = float(os.getenv("CONFIDENCE_THRESHOLD", "0.4"))

# Load the model once, when this module is imported, instead of on
# every request -- this is the single most important performance
# decision in this file.
model = YOLO(MODEL_PATH)


def predict_image(image_bytes: bytes, conf: float = CONFIDENCE_THRESHOLD) -> List[Dict[str, Any]]:
    """
    Run detection on a single image.

    Args:
        image_bytes: Raw bytes of the uploaded image (JPEG/PNG).
        conf: Confidence threshold used to filter out weak detections.

    Returns:
        A list of detections. Each detection is a dict with:
            - class_name: str
            - confidence: float
            - bbox: {x1, y1, x2, y2} in pixel coordinates
    """
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    results = model.predict(source=image, conf=conf, verbose=False)
    result = results[0]

    detections: List[Dict[str, Any]] = []
    for box in result.boxes:
        cls_id = int(box.cls[0])
        class_name = model.names[cls_id]
        confidence = float(box.conf[0])
        x1, y1, x2, y2 = box.xyxy[0].tolist()

        detections.append(
            {
                "class_name": class_name,
                "confidence": round(confidence, 4),
                "bbox": {
                    "x1": round(x1, 2),
                    "y1": round(y1, 2),
                    "x2": round(x2, 2),
                    "y2": round(y2, 2),
                },
            }
        )

    return detections