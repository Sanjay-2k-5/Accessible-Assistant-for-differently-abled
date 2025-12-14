# ♿ Accessible Assistant for Differently Abled

An AI-powered assistive system designed to support visually impaired, hearing impaired, and speech impaired individuals by leveraging Computer Vision, Speech Processing, and Deep Learning technologies. This project aims to enhance accessibility and inclusivity by providing real-time assistance through an intelligent web-based interface.

## 🌟 Key Features

### 👁️ Assistance for Visually Impaired
- Object Detection using YOLOv8
- Face Recognition
- Book Reader (text extraction with audio output)
- Audio-based navigation support

### 🧏 Assistance for Hearing Imppaired
- Speech-to-Text (STT)
- Gesture Recognition
- Visual text-based interaction

### 🗣️ Assistance for Speech Impaired
- Text-to-Speech (TTS)
- Gesture-based communication
- Web-based interaction interface

## 🛠️ Technologies Used
- Python
- Flask (Web Framework)
- OpenCV
- YOLOv8 (Ultralytics)
- Speech Recognition
- Text-to-Speech (TTS)
- HTML, CSS, JavaScript
- Computer Vision & Deep Learning

## 📁 Project Structure
Accessible-Assistant-for-differently-abled/
├── app.py
├── features/
│   ├── object_detection.py
│   ├── face_recognition.py
│   ├── gesture.py
│   ├── book_reader.py
│   ├── stt.py
│   └── tts.py
├── templates/
│   ├── index.html
│   ├── blind.html
│   ├── deaf.html
│   ├── volunteer.html
│   ├── gesture.html
│   ├── object_detection.html
│   ├── stt.html
│   └── tts.html
├── static/
│   └── js/
│       └── app.js
├── README.md
└── requirements.txt

## 🚀 How to Run the Project

1. Clone the repository  
git clone https://github.com/Sanjay-2k-5/Accessible-Assistant-for-differently-abled.git  
cd Accessible-Assistant-for-differently-abled  

2. Create a virtual environment (recommended)  
python -m venv venv  
source venv/bin/activate  (macOS / Linux)  
venv\Scripts\activate  (Windows)  

3. Install dependencies  
pip install -r requirements.txt  

4. Download YOLOv8 model  
Download yolov8s.pt from:  
https://github.com/ultralytics/ultralytics  
Place the file in the project root directory.  
The model file is not included in the repository to keep it lightweight.

5. Run the application  
python app.py  

Open browser and go to:  
http://127.0.0.1:5000  

## 🎯 Use Cases
- Helps blind users identify objects and read books
- Converts speech into text for hearing-impaired users
- Enables speech-impaired users to communicate via text and gestures
- Provides an inclusive human–computer interaction system

## 🧠 Future Enhancements
- Mobile application support
- Multi-language speech recognition
- Cloud-based AI inference
- Improved gesture recognition accuracy
- IoT device integration
- Voice-controlled navigation

## 👨‍💻 Author
Sanjay  
GitHub: https://github.com/Sanjay-2k-5  

## 📜 License
This project is developed for educational and research purposes. You are free to use, modify, and distribute this project with proper credit.

## ⭐ Acknowledgements
- YOLOv8 – Ultralytics
- OpenCV Community
- Flask Documentation
- Open-source contributors and libraries
