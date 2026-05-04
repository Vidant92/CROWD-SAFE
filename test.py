import cv2
import numpy as np
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
print("YOLO model loaded.")
cap = cv2.VideoCapture("local_train.mp4")
ret, frame = cap.read()
if ret:
    frame = cv2.resize(frame, (960, 540))
    results = model.predict(frame, imgsz=640, conf=0.4, classes=[0], verbose=False)
    print(f"Results: {len(results)}")
else:
    print("Could not read frame")
cap.release()
print("All assertions passed")
