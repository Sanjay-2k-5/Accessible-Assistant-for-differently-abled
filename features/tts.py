import pyttsx3

def speak(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Optional: Customize voice properties (rate, volume, voice)
    engine.setProperty('rate', 150)      # Speed of speech (default is around 200)
    engine.setProperty('volume', 1.0)    # Volume (0.0 to 1.0)

    # Speak the given text
    engine.say(text)
    engine.runAndWait()
