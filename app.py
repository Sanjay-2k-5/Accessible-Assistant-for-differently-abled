from flask import Flask, render_template, jsonify, request
from features.book_reader import process_base64_image, text_to_speech
from features.object_detection import process_object_image
from features.gesture import decode_base64_image, toggle_appliance
from features.face_recognition import recognize_face, save_face

app = Flask(__name__)

# ------------------- Routes -------------------
@app.route('/tts')
def tts():
    return render_template('tts.html')

@app.route('/tts1')
def tts1():
    return render_template('tts1.html')

@app.route('/deaf')
def deaf_mode():
    return render_template('deaf.html')

@app.route('/gesture')
def control_appliance():
    return render_template('gesture.html')

@app.route('/stt')
def stt():
    return render_template('stt.html')

@app.route('/stt1')
def stt1():
    return render_template('stt1.html')

@app.route('/objectdetection')
def object_detection():
    return render_template('object_detection.html')

@app.route('/face')
def face_detection():
    return render_template('face_detection.html')


@app.route('/')
def home():
    return render_template('login.html')

@app.route('/volunteer')
def volunteer_mode():
    return render_template('volunteer.html')

@app.route('/index')
def indexmode():
    return render_template('index.html')

@app.route('/blind')
def blind_mode():
    return render_template('blind.html')

@app.route('/bookreader')
def bookreader_page():
    return render_template('bookreader.html')

# ------------------- API Routes -------------------

@app.route('/api/book-reader', methods=['POST'])
def book_reader_api():
    try:
        data = request.get_json()
        image_base64 = data.get('image')

        if not image_base64:
            return jsonify({'status': 'error', 'message': 'No image data received'}), 400

        extracted_text = process_base64_image(image_base64)
        if extracted_text:
            text_to_speech(extracted_text)
            return jsonify({'status': 'success', 'extracted_text': extracted_text})
        else:
            return jsonify({'status': 'error', 'message': 'Text extraction failed'}), 500

    except Exception as e:
        print("❌ [ERROR] Exception in /api/book-reader:", e)
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/object-detection', methods=['POST'])
def object_detection_api():
    try:
        data = request.get_json()
        image_base64 = data.get('image')

        if not image_base64:
            return jsonify({'status': 'error', 'message': 'No image data received'}), 400

        detected_objects = process_object_image(image_base64)
        
        if detected_objects:
            return jsonify({'status': 'success', 'objects': detected_objects})
        else:
            return jsonify({'status': 'error', 'message': 'No objects detected'}), 500
    except Exception as e:
        print(f"❌ [ERROR] Exception in /api/object-detection: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# ------------------- Gesture API Routes -------------------


@app.route('/api/gesture-control', methods=['POST'])
def gesture_control():
    try:
        data = request.get_json()
        image_base64 = data.get('image')

        if not image_base64:
            return jsonify({'status': 'error', 'message': 'No image data received'}), 400

        frame = decode_base64_image(image_base64)
        finger_count, appliance_name, appliance_status = toggle_appliance(frame)

        return jsonify({
            'status': 'success',
            'finger_count': finger_count,
            'appliance_name': appliance_name,
            'appliance_status': 'ON' if appliance_status else 'OFF'
        })

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/api/add-face', methods=['POST'])
def add_face():
    data = request.get_json()
    name = data.get("name", "").strip()
    image = data.get("image", "")
    if not name or not image:
        return jsonify({"status": "error", "message": "Missing name or image"}), 400
    success = save_face(image, name)
    if success:
        return jsonify({"status": "success", "message": f"Added {name} successfully!"})
    else:
        return jsonify({"status": "error", "message": "No face found!"}), 400

@app.route('/api/live-face-recognition', methods=['POST'])
def recognize():
    data = request.get_json()
    image = data.get("image", "")
    if not image:
        return jsonify({"status": "error", "message": "No image provided"}), 400
    name = recognize_face(image)
    return jsonify({"status": "success", "name": name})

# ------------------- Main -------------------
if __name__ == '__main__':
    app.run(debug=True)
