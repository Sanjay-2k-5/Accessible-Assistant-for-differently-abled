import os
import cv2
import base64
import numpy as np
import mediapipe as mp
from keras_facenet import FaceNet
from sklearn.metrics.pairwise import cosine_similarity

# Init models
embedder = FaceNet()
detector = mp.solutions.face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.7)
KNOWN_DIR = "known_faces_facenet"
os.makedirs(KNOWN_DIR, exist_ok=True)

def decode_image(image_base64):
    header, encoded = image_base64.split(",", 1)
    data = base64.b64decode(encoded)
    np_arr = np.frombuffer(data, np.uint8)
    return cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

def load_known_embeddings():
    faces, names = [], []
    for file in os.listdir(KNOWN_DIR):
        path = os.path.join(KNOWN_DIR, file)
        img = cv2.imread(path)
        if img is not None:
            resized = cv2.resize(img, (160, 160))
            emb = embedder.embeddings([resized])[0]
            faces.append(emb)
            names.append(file.split('.')[0])
    return np.array(faces), names

def recognize_face(image_base64):
    frame = decode_image(image_base64)
    results = detector.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.detections:
        for det in results.detections:
            bbox = det.location_data.relative_bounding_box
            h, w, _ = frame.shape
            x, y = int(bbox.xmin * w), int(bbox.ymin * h)
            w_box, h_box = int(bbox.width * w), int(bbox.height * h)
            face = frame[y:y+h_box, x:x+w_box]
            face_resized = cv2.resize(face, (160, 160))
            embedding = embedder.embeddings([face_resized])[0].reshape(1, -1)
            known_embeddings, known_names = load_known_embeddings()

            if len(known_embeddings) == 0:
                return "No known faces"

            sims = cosine_similarity(known_embeddings, embedding)
            idx = np.argmax(sims)
            return known_names[idx] if sims[idx] > 0.6 else "Unknown"
    return "No Face Detected"

def save_face(image_base64, name):
    frame = decode_image(image_base64)
    results = detector.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if results.detections:
        for det in results.detections:
            bbox = det.location_data.relative_bounding_box
            h, w, _ = frame.shape
            x, y = int(bbox.xmin * w), int(bbox.ymin * h)
            w_box, h_box = int(bbox.width * w), int(bbox.height * h)
            face_crop = frame[y:y+h_box, x:x+w_box]
            cv2.imwrite(os.path.join(KNOWN_DIR, f"{name}.jpg"), face_crop)
            return True
    return False
