import cv2
import base64
import numpy as np
import mediapipe as mp

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands()

# Store appliance states
appliance_states = {}

# Map finger counts to appliance names
finger_to_appliance = {
    1: "Light",
    2: "Fan",
    3: "TV",
    4: "AC",
    5: "Heater"
}

def decode_base64_image(base64_string):
    img_data = base64_string.split(',')[1]
    img_bytes = base64.b64decode(img_data)
    img_np = np.frombuffer(img_bytes, dtype=np.uint8)
    return cv2.imdecode(img_np, cv2.IMREAD_COLOR)

def detect_finger_count(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    finger_count = 0
    if result.multi_hand_landmarks and result.multi_handedness:
        for idx, hand_landmarks in enumerate(result.multi_hand_landmarks):
            lm = hand_landmarks.landmark
            hand_label = result.multi_handedness[idx].classification[0].label  # 'Left' or 'Right'

            fingers = [0, 0, 0, 0, 0]

            # Thumb logic differs for left vs right hand
            if hand_label == "Right":
                fingers[0] = 1 if lm[mp_hands.HandLandmark.THUMB_TIP].x < lm[mp_hands.HandLandmark.THUMB_IP].x else 0
            else:
                fingers[0] = 1 if lm[mp_hands.HandLandmark.THUMB_TIP].x > lm[mp_hands.HandLandmark.THUMB_IP].x else 0

            # Other fingers (same for both hands)
            fingers[1] = 1 if lm[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < lm[mp_hands.HandLandmark.INDEX_FINGER_PIP].y else 0
            fingers[2] = 1 if lm[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < lm[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y else 0
            fingers[3] = 1 if lm[mp_hands.HandLandmark.RING_FINGER_TIP].y < lm[mp_hands.HandLandmark.RING_FINGER_PIP].y else 0
            fingers[4] = 1 if lm[mp_hands.HandLandmark.PINKY_TIP].y < lm[mp_hands.HandLandmark.PINKY_PIP].y else 0

            finger_count = sum(fingers)
            break  # Only process first hand
    return finger_count

    return finger_count

def toggle_appliance(frame):
    finger_count = detect_finger_count(frame)
    if(finger_count):
    # Determine appliance name
        appliance_name = finger_to_appliance.get(finger_count, "Unknown Appliance")

        if appliance_name not in appliance_states:
            appliance_states[appliance_name] = False
        appliance_states[appliance_name] = not appliance_states[appliance_name]

        return finger_count, appliance_name, appliance_states[appliance_name]
