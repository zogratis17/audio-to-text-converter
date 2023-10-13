import speech_recognition as sr

def audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)  # Read the entire audio file
        
        try:
            text = recognizer.recognize_google(audio)  # Use Google Speech Recognition
            return text
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service: {e}")

# Example usage
audio_file = r"PATH OF THE FILE HAS TO BE ENTERED HERE"
text = audio_to_text(audio_file)
print("Transcription:", text)
