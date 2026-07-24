# Bangladeshi Taka Note Detection API

A YOLOv11-based object detection system that identifies Bangladeshi Taka
currency notes from an image, served through a FastAPI REST API and
containerized with Docker.
## Project Structure

taka-note-detector/
├── app/
│ ├── inference.py # detection pipeline
│ └── main.py # FastAPI app
├── models/best.pt # trained YOLOv11 weights
├── test_images/ # sample test images
├── demo_inference.py
├── Dockerfile
├── requirements.txt
└── README.md

## Local Setup
```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## API Usage
POST `/predict` with a form-data field named `file` (JPEG/PNG).

Example:
```bash
curl -X POST "http://localhost:8000/predict" -F "file=@test_images/note1.jpg;type=image/jpeg"
```

## Docker
```bash
docker build -t bangladeshi-taka-detection-api .
docker run -d -p 8000:8000 --name taka-api bangladeshi-taka-detection-api
```

## Deployment
Live API: <your public URL here after bonus task>

## Tech Stack
YOLOv11 (Ultralytics), FastAPI, Uvicorn, Docker