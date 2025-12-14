 🧑‍🦯 Accessible Assistant

An assistant designed to support blind, deaf, mute, and all users. Integrates computer vision, speech technologies, and assistive interfaces to make digital interaction accessible for everyone.

 🚀 Features

 For Blind Users 👁️
- Object Detection (YOLOv8 + OpenCV)
- Real-time Book Reader (OCR + Text-to-Speech)
- Voice Commands & Navigation

 For Deaf Users 👂
- Speech-to-Text (STT) for live transcription
- Real-time conversation support

 For Mute Users 🗣️
- Text-to-Speech (TTS) for communication
- Simple typing → automatic voice output

 For General Users 👨‍💻
- General-purpose assistant features
- Volunteer support system

 Additional Functionalities
- Gesture-controlled appliances (MediaPipe + OpenCV)
- Face Recognition (FaceNet)

**Volunteer System:** Users can request nearby volunteers for help (ongoing).

 🏗️ Tech Stack

- **Frontend:** HTML, Tailwind CSS, JavaScript
- **Backend:** Python (Flask)
- **AI/ML:** OpenCV, YOLOv8, MediaPipe, FaceNet, Tesseract OCR
- **Speech Tools:** pyttsx3, SpeechRecognition, Web Speech API

 🚦 Installation

git clone https://github.com/MUTHU0029/accessible-assistant.git
cd accessible-assistant
pip install -r requirements.txt
python app.py

 📚 Usage

Blind Mode: Select Blind → Use object detection & book reader

Deaf Mode: Select Deaf → Speech → Text transcription

Mute Mode: Select Mute → Type and convert to speech

Normal Mode: Access all features + volunteer support

 📝 License

This project is licensed under the MIT License – free to use and modify.
