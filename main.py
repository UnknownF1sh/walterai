# 1.8.2024 before you run the code make sure you have weabou.html downloaded too
import tkinter as tk
import ttkbootstrap as ttk
import speech_recognition
from walterwhite import gen_response

recognizer = speech_recognition.Recognizer()

def Listener(dur):
    
    with speech_recognition.Microphone() as mic:
        
        recognizer.adjust_for_ambient_noise(source=mic, duration=dur,)
        print("Listening...")
        audio = recognizer.listen(mic)

        text = recognizer.recognize_google(audio, language="en-US")
        text.lower()

    return text, audio

# Function definitions
def speak_function():
    try: 
        message, _ = Listener(0.2)
        print(message)
        response = gen_response(message=message)['message']['content']
        print(response)

    except speech_recognition.exceptions.UnknownValueError: print("Listener error!")

# Root setup
root = ttk.Window(themename="journal")
root.title("WalterGPT")
root.geometry("300x200")

# Load the PNG icon
icon = tk.PhotoImage(
    file="C:\\Users\\super\\OneDrive\\Plocha\\Python\\AI\\hackathon\\microphone.png"
)
root.iconphoto(False, icon)

#Speak button setup
speak_frame = tk.Frame(master=root)
speak_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame in the window

# Press to speak button
speak_button = ttk.Button(
    master=speak_frame,
    text="Press to speak",
    command=speak_function,
)
speak_button.pack(anchor="center")

root.mainloop()