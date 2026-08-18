# app/schemas.py
#
# Pydantic request/response models for the Bangladeshi Taka Note Detection API.
# Added for the Module 17 resubmission, following the response-schema pattern
# covered in the Module 19 "optimizing AI/ML APIs" class.
#
# Usage in app/main.py:
#   from app.schemas import PredictResponse
#
#   @app.post("/predict", response_model=PredictResponse)
#   async def predict(file: UploadFile = File(...)):
#       ...
#       detections = predict_image(image_bytes)
#       return PredictResponse(
#           filename=file.filename,
#           num_detections=len(detections),
#           detections=detections,
#       )

from pydantic import BaseModel
from typing import List


class BBox(BaseModel):
    """Pixel bounding box of one detected note, in the original image's coordinates."""
    x1: float
    y1: float
    x2: float
    y2: float


class Detection(BaseModel):
    """A single detected banknote."""
    class_name: str      # e.g. "500 Taka"
    confidence: float    # 0.0 - 1.0
    bbox: BBox


class PredictResponse(BaseModel):
    """Full response returned by POST /predict."""
    filename: str
    num_detections: int
    detections: List[Detection]
