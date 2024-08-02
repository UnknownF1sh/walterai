import speech_recognition
import whisper


whisp = whisper.load_model("tiny")


recognizer = speech_recognition.Recognizer()

def Listener(dur):
    
    with speech_recognition.Microphone() as mic:
        
        recognizer.adjust_for_ambient_noise(source=mic, duration=dur,)
        print("Listening...")
        audio = recognizer.listen(mic)
    
    return audio

whisp_aud = Listener(0.2)

result = whisp.transcribe(audio=whisp_aud)["text"]
print(result)
