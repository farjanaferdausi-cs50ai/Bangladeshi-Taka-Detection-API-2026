"""
demo_inference.py
------------------
Standalone script demonstrating a successful single-image inference run.
Run this file directly to satisfy Task 1's "script demonstrating
successful inference" requirement.
"""

import os
from app.inference import predict_image, model

IMAGE_PATH = "test_images/note2.jpg"  # change to any test image you have

with open(IMAGE_PATH, "rb") as f:
    image_bytes = f.read()

detections = predict_image(image_bytes)

print(f"Image: {IMAGE_PATH}")
print(f"Total detections: {len(detections)}\n")

for i, det in enumerate(detections, start=1):
    print(f"Detection {i}:")
    print(f"  Class      : {det['class_name']}")
    print(f"  Confidence : {det['confidence']}")
    print(f"  BBox       : {det['bbox']}")
    print()

base_name = os.path.splitext(os.path.basename(IMAGE_PATH))[0]
output_path = f"test_images/{base_name}_detected.jpg"

results = model.predict(source=IMAGE_PATH, conf=0.4, verbose=False)
results[0].save(filename=output_path)
print(f"Annotated image saved to {output_path}")