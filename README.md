<<div align="center">

# 💵 Bangladeshi Taka Note Detection API

### AI-powered REST API that detects and classifies Bangladeshi Taka banknotes in real time

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![YOLOv11](https://img.shields.io/badge/YOLOv11-Ultralytics-8A2BE2?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)

</div>

---

## 🎓 Assignment Info

**Module 17 Assignment:** Deployment of Bangladeshi Taka Note Detection Model Using REST API & Docker
**Submitted by:** Farjana Ferdausi
GitHub Link : https://github.com/farjanaferdausi-cs50ai/Bangladeshi-Taka-Detection-API-2026

Google Documentation: 


---

## 🌐 Live Demo

**🔗 Live Endpoint & Interactive Docs:**  https://bangladeshi-taka-detection-api-2026.onrender.com
---

## 📌 Overview

This project detects and classifies Bangladeshi Taka banknotes from an uploaded image. A custom-trained **YOLOv11** object detection model is served through a **FastAPI** backend and packaged with **Docker** for consistent, reproducible cloud deployment.

## ✨ Key Features

- 🔍 **Real-time detection** — returns bounding boxes and confidence scores for every note found
- 💴 **7 denominations supported** — 10, 20, 50, 100, 200, 500, and 1000 Taka
- ⚡ **Interactive API docs** — auto-generated Swagger UI at `/docs` and ReDoc at `/redoc`
- 🐳 **Fully containerized** — one command builds and runs the entire app anywhere
- ☁️ **Live on the cloud** — publicly testable endpoint, no local setup required

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|---|---|---|
| API Framework | FastAPI + Uvicorn | Request handling & routing |
| Object Detection | YOLOv11 (Ultralytics) | Banknote detection & classification |
| Image Processing | OpenCV / Pillow | Image decoding & annotation |
| Containerization | Docker | Reproducible, portable deployment |
| Cloud Hosting | Render | Free-tier web service hosting |

## 📁 Project Structure

```
Bangladeshi-Taka-Detection-API-2026/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app & routes
│   └── inference.py     # YOLOv11 model loading & prediction logic
├── models/
│   └── best.pt          # Trained YOLOv11 weights
├── test_images/         # Sample images for testing
├── Dockerfile
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### Option A — Run with Docker (recommended)

```bash
# 1. Clone the repository
git clone https://github.com/farjanaferdausi-cs50ai/Bangladeshi-Taka-Detection-API-2026.git
cd Bangladeshi-Taka-Detection-API-2026

# 2. Build the image
docker build -t bangladeshi-taka-detection-api .

# 3. Run the container
docker run -d -p 8000:8000 --name taka-api bangladeshi-taka-detection-api
```

Visit **http://localhost:8000/docs** to try it out.

### Option B — Run locally with Python

```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## 📡 API Reference

### Health Check
`GET /`
```json
{ "message": "API is working!" }
```

### Predict
`POST /predict`

| Field | Type | Description |
|---|---|---|
| `file` | form-data | Image file (`.jpg`, `.jpeg`, `.png`) |

**Example request:**
```bash
curl.exe -X POST "http://localhost:8000/predict" -F "file=@test_images/note1.jpg;type=image/jpeg"
```

**Example response:**
```json
{
  "filename": "note1.jpg",
  "total_detections": 1,
  "detections": [
    {
      "class_id": 3,
      "confidence": 0.95,
      "bbox": { "x1": 12.4, "y1": 58.2, "x2": 480.6, "y2": 452.9 }
    }
  ]
}
```
*(replace with your own actual `/predict` output)*

### Batch Testing All Sample Images

```powershell
Get-ChildItem -Path test_images\* -Include *.jpg,*.jpeg,*.png | ForEach-Object {
    Write-Host "Testing:" $_.Name
    curl.exe -s -X POST "http://127.0.0.1:8000/predict" -F "file=@$($_.FullName);type=image/jpeg"
    Write-Host ""
}
```

## 📊 Accuracy Notes

[Write 4–5 lines here based on your own test results: which notes were detected correctly, the typical confidence range, and which conditions — blur, low light, tilted angle — reduced accuracy.]

## 👩‍💻 Author

**Farjana Ferdausi**
Aspiring AI & ML Engineering — Ostad (Batch-6), Bangladesh.
Also studying AI Engineering & Data Science at CodeBasics, India.
AI Intern at CodeAlpha, India.

---
<div align="center">Built with YOLOv11 · FastAPI · Docker</div>
