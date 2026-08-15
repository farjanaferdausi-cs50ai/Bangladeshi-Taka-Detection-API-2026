"""
main.py
-------
FastAPI application that serves the Bangladeshi Taka Note Detection model.

Endpoints:
    GET  /health   - simple health check (useful for Docker/cloud platforms)
    POST /predict  - accepts an image file, returns detections as JSON
"""

import logging

from fastapi import FastAPI, File, HTTPException, UploadFile

from app.inference import predict_image
from app.schemas import PredictResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Bangladeshi Taka Note Detection API",
    description="YOLOv11-based object detection API for Bangladeshi currency notes.",
    version="1.0.0",
)

ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/png", "image/jpg"}


@app.get("/health")
def health_check():
    """Basic liveness check used by Docker/cloud platforms."""
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
async def predict(file: UploadFile = File(...)):
    """
    Run detection on a single uploaded image and return the results as JSON.
    """
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=415,
            detail=(
                f"Unsupported file type: {file.content_type}. "
                "Please upload a JPEG or PNG image."
            ),
        )

    image_bytes = await file.read()
    if not image_bytes:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    try:
        detections = predict_image(image_bytes)
    except Exception as exc:
        logger.exception("Inference failed")
        raise HTTPException(status_code=500, detail=f"Inference failed: {exc}")

    return PredictResponse(
        filename=file.filename,
        num_detections=len(detections),
        detections=detections,
    )
