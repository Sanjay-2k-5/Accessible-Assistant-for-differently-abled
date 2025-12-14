import cv2
import base64
import numpy as np
from io import BytesIO
from ultralytics import YOLO

# Load the YOLOv8 model (make sure the model path is correct)
model_path = "yolov8s.pt"
model = YOLO(model_path)

# Decode base64 image
def decode_base64_image(base64_string):
    # Remove the prefix (data:image/jpeg;base64,)
    img_data = base64_string.split(',')[1]
    img_bytes = base64.b64decode(img_data)
    img_np = np.frombuffer(img_bytes, dtype=np.uint8)
    img = cv2.imdecode(img_np, flags=cv2.IMREAD_COLOR)
    return img

# Process the object detection image
def process_object_image(base64_image):
    try:
        # Decode the base64 image
        image = decode_base64_image(base64_image)

        # Perform object detection using the YOLO model
        results = model.predict(image, imgsz=640, device="cuda")

        # Extract detected objects and class names
        detected_objects = []
        for result in results:
            boxes = result.boxes
            for box in boxes:
                cls = int(box.cls[0].item())  # Class ID
                label = model.names[cls] if cls in model.names else f"ID {cls}"
                detected_objects.append(label)

        return detected_objects
    except Exception as e:
        print(f"Error in object detection: {e}")
        return []

