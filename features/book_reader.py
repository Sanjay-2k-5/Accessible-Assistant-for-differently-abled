import cv2
import pytesseract
import numpy as np
import base64
import io
import pyttsx3
from PIL import Image

# Optional: Update if Tesseract path not set
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this with your path

def capture_and_extract_text():
    """Capture image from the webcam and extract text using Tesseract."""
    cap = cv2.VideoCapture(0)  # Open laptop camera

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return None

    while True:
        ret, frame = cap.read()  # Capture frame
        if not ret:
            print("Error: Failed to capture image.")
            break

        cv2.imshow("Press 'Space' to Capture, 'Esc' to Exit", frame)  # Show camera feed

        key = cv2.waitKey(1) & 0xFF
        if key == 32:  # Press Spacebar to capture
            break
        elif key == 27:  # Press Esc to exit
            cap.release()
            cv2.destroyAllWindows()
            return None

    cap.release()
    cv2.destroyAllWindows()

    # Convert OpenCV image (BGR) to PIL image (RGB)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img_rgb)

    # Extract text using Tesseract
    extracted_text = pytesseract.image_to_string(pil_img)
    return extracted_text

def process_base64_image(image_base64):
    """Decode base64 image, save it, preprocess, and extract text using Tesseract."""
    try:
        if "," in image_base64:
            image_base64 = image_base64.split(",")[1]

        image_bytes = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        # ✅ Save the captured image (optional, for debugging)
        image.save("muthu.png")

        # Convert to OpenCV format
        open_cv_image = np.array(image)
        open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)

        # ✅ Preprocessing starts here:
        gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
        denoised = cv2.fastNlMeansDenoising(gray, h=30)

        # Optional: Thresholding (make it pure black-and-white for better OCR sometimes)
        # _, thresh = cv2.threshold(denoised, 127, 255, cv2.THRESH_BINARY)

        # Now use Tesseract
        extracted_text = pytesseract.image_to_string(denoised, lang="eng")
        extracted_text = extracted_text.strip()

        print("[INFO] Extracted text:", extracted_text or "[No text found]")
        return extracted_text if extracted_text else None

    except Exception as e:
        print("❌ [ERROR] Failed to process image:", e)
        return None
def text_to_speech(text):
    """Convert extracted text to speech."""
    if not text:
        print("⚠️ [WARNING] No text to read.")
        return

    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)
        engine.say(text)
        engine.runAndWait()
        print("[INFO] Text-to-speech completed.")
    except Exception as e:
        print("❌ [ERROR] Failed in text-to-speech:", e)