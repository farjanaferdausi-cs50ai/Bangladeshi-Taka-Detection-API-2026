<div align="center">

# 💵 **Bangladeshi Taka Note Detection API**


### AI-powered REST API that detects and classifies Bangladeshi Taka banknotes in real time

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![YOLOv11](https://img.shields.io/badge/YOLOv11-Ultralytics-8A2BE2?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)
</div>
<div align="center">

<img width="200" height="200" alt="Logo 1" src="https://github.com/user-attachments/assets/7ced81e1-f84b-4114-b97a-4b4b70007dd4" />

</div>

---

## 🎓 Assignment Info

**Module 17 Assignment:** Deployment of Bangladeshi Taka Note Detection Model Using REST API & Docker
**Submitted by:** **Farjana Ferdausi**

Google Documentation: https://docs.google.com/document/d/1IH_EtI-SlbTpMIsCFLNOwpb8l8MUcw1k/edit?usp=sharing&ouid=113725347256607058408&rtpof=true&sd=true

---

## 🌐 Live Demo

**🔗 Live Endpoint & Interactive Docs:**

Live API (Render): https://bangladeshi-taka-detection-api-2026-1.onrender.com/docs

Health check: https://bangladeshi-taka-detection-api-2026-1.onrender.com/health

Interactive docs: https://bangladeshi-taka-detection-api-2026-1.onrender.com/docs

---

## 📌 Overview

This project detects and classifies Bangladeshi Taka banknotes from an uploaded image. A custom-trained **YOLOv11** object detection model is served through a **FastAPI** backend and packaged with **Docker** for consistent, reproducible cloud deployment.

## ✨ Key Features

- 🔍 **Real-time detection** — returns bounding boxes and confidence scores for every note found
- 💴 **9 denominations supported** — 1, 2, 5, 10, 20, 50, 100, 500, and 1000 Taka
- ⚡ **Interactive API docs** — auto-generated Swagger UI at `/docs` and ReDoc at `/redoc`
- 🐳 **Fully containerized** — one command builds and runs the entire app anywhere (or use Docker Compose)
- ☁️ **Live on the cloud** — publicly testable endpoint, no local setup required

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|---|---|---|
| API Framework | FastAPI + Uvicorn | Request handling & routing |
| Object Detection | YOLOv11 (Ultralytics) | Banknote detection & classification |
| Image Processing | Pillow | Image decoding & annotation |
| Validation | Pydantic (`schemas.py`) | Typed request/response models |
| Containerization | Docker / Docker Compose | Reproducible, portable deployment |
| Cloud Hosting | Render | Free-tier web service hosting |

## 📁 Project Structure

```
Bangladeshi-Taka-Detection-API-2026/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app & routes
│   ├── inference.py      # YOLOv11 model loading & prediction logic
│   └── schemas.py        # Pydantic request/response models
├── models/
│   └── best.pt           # Trained YOLOv11 weights (Phase-1)
├── test_images/          # Sample images for testing
├── demo_inference.py     # Standalone single-image inference demo
├── Dockerfile
├── docker-compose.yml    # Optional one-command build + run
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### Option A — Run with Docker

```bash
# 1. Clone the repository
git clone https://github.com/farjanaferdausi-cs50ai/Bangladeshi-Taka-Detection-API-2026.git
cd Bangladeshi-Taka-Detection-API-2026

# 2. Build the image
docker build -t taka-api .

# 3. Run the container
docker run -d -p 8000:8000 --name taka-api taka-api
```

### Option B — Run with Docker Compose

```bash
docker compose up --build   # build the image and start the container
docker compose down         # stop and remove it
```

Visit **http://localhost:8000/docs** to try it out.

### Option C — Run locally with Python

```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## 📡 API Reference

### Health Check
`GET /health`
```json
{ "status": "ok" }
```

### Predict
`POST /predict`

| Field | Type | Description |
|---|---|---|
| `file` | form-data | Image file (`.jpg`, `.jpeg`, `.png`) |

**Example request:**
```bash
curl.exe -X POST "http://localhost:8000/predict" -F "file=@test_images/note2.jpg;type=image/jpeg"
```

**Example response:**
```json
{
  "filename": "note2.jpg",
  "num_detections": 1,
  "detections": [
    {
      "class_name": "500 Taka",
      "confidence": 0.5037,
      "bbox": {
        "x1": 20.34,
        "y1": 66.78,
        "x2": 1497.89,
        "y2": 795.69
      }
    }
  ]
}
```
### Batch Testing All Sample Images

```powershell
Get-ChildItem -Path test_images\* -Include *.jpg,*.jpeg,*.png | ForEach-Object {
    Write-Host "Testing:" $_.Name
    curl.exe -s -X POST "http://127.0.0.1:8000/predict" -F "file=@$($_.FullName);type=image/jpeg"
    Write-Host ""
}
```

## 📊 Accuracy Notes

Evaluated on 333 held-out validation images, the model reached **87.2% precision, 92.6% recall, 96.5% mAP50, and 95.7% mAP50-95** — strong, consistent performance across all nine trained denominations. Per-class mAP50-95 is highest for 2 Taka (99.2%) and lowest for 10 Taka (84.6%), most likely because 10 Taka's colour palette and layout are visually closest to its neighbouring small-denomination notes. Confidence scores typically exceed 0.90 for a clean, well-lit, single-note image, and fall noticeably for blurred photos, extreme angles, poor lighting, or multi-note frames, since every training image was a single, centered banknote. Note: 200 Taka is **not** one of the nine trained classes, so it is expected to be misclassified if tested.

## 👩‍💻 Author

**Farjana Ferdausi**

**AI Engineering Fellow — Google Cloud Gen AI Academy (Cohort 3) | Agentic AI · RAG · Gemini · ADK · BigQuery MCP · Cloud Run | AI Intern @ CodeAlpha | Former HR Professional (14+ yrs)**

---
<div align="center">Built with YOLOv11 · FastAPI · Docker</div>
