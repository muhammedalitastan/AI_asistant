import tkinter as tk
from tkinter import scrolledtext
import threading
from initilize_engine import command, speak
from social_media import social_media
from open_close_app import openApp, closeApp
from condition import condition
from Browsing import browsing
from wishMe import wishMe
from utils import cal_day
import subprocess
import json
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from arayüz import arayüz


def send_text_command():
    """Kullanıcının metin girişini alıp execute_command fonksiyonunu çalıştırır."""
    user_input = text_entry.get()
    text_entry.delete(0, "end")  # Giriş kutusunu temizle
    threading.Thread(target=execute_command, args=(user_input,)).start()

def start_listening():
    """Sesli komutları dinleyip execute_command fonksiyonunu çalıştırır."""
    threading.Thread(target=execute_command).start()

root, chat_display, text_entry = arayüz(send_text_command,start_listening)

def load_schedule():
    with open("schedule.json", "r", encoding="utf-8") as file:
        return json.load(file)

def schedule1():
    schedule_data = load_schedule()
    day = cal_day().lower()
    speak("Boss, today's schedule is")
    if day in schedule_data:
        speak(schedule_data[day])
    else:
        speak("Boss, I couldn't find a schedule for today.")

process = None
process2=None

def openSchedule():
    global process
    if process is None:
        process = subprocess.Popen(["python", "schedule3.py"])

def closeSchedule():
    global process
    if process is not None:
        process.terminate()
        process = None

def openDaily():
    global process2
    if process2 is None:
        process2 = subprocess.Popen(["python", "günlük.py"])

def closeDaily():
    global process2
    if process is not None:
        process2.terminate()
        process2 = None   

        
             



def execute_command(input_text=None):
    query = input_text if input_text else command().lower()
    chat_display.insert(tk.END, f"You: {query}\n")
    
    
    if any(word in query for word in ['facebook', 'discord', 'whatsapp', 'instagram']):
        social_media(query)
    elif "volume up" in query or "increase volume" in query:
        speak("Volume increased")
    elif "volume down" in query or "decrease volume" in query:
        speak("Volume decreased")
    elif "mute the sound" in query:
        speak("Volume muted")
    elif "open calculator" in query or "open notepad" in query or "open paint" in query:
        openApp(query)
    elif "close calculator" in query or "close notepad" in query or "close paint" in query:
        closeApp(query)
    elif "open schedule" in query:
        openSchedule()
    elif "close schedule" in query:
        closeSchedule()
    elif "tell me today work" in query:
        schedule1()
    elif any(word in query for word in ["what", "who", "how", "hi", "thanks", "hello"]):
        padded_sequences = pad_sequences(tokenizer.texts_to_sequences([query]), maxlen=20, truncating='post')
        result = model.predict(padded_sequences)
        tag = label_encoder.inverse_transform([np.argmax(result)])
        for i in data['intents']:
            if i['tag'] == tag:
                response = np.random.choice(i['responses'])
                chat_display.insert(tk.END, f"JARVIS: {response}\n")
                speak(response)
    # elif "open google" in query or "open edge" in query:
    #     browsing(query)
    elif "open google" in query or "open edge" in query:
        browsing(query)
    elif "open daily" in query or "open daily note" in query:
        openDaily()
    elif "close daily" in query:
        closeDaily()        
    elif "system condition" in query:
        speak("Checking the system condition")
        condition()
    elif "exit" in query:
        root.quit()
    return query
       

def start_listening():
    threading.Thread(target=execute_command).start()

def send_text_command():
    user_input = text_entry.get()
    text_entry.delete(0, tk.END)
    threading.Thread(target=execute_command, args=(user_input,)).start()

# Load AI Model
data = json.load(open("intents.json"))
model = load_model("chat_model.h5", compile=False)
tokenizer = pickle.load(open("tokenizer.pkl", "rb"))
label_encoder = pickle.load(open("label_encoder.pkl", "rb"))

# # GUI Setup
# root = tk.Tk()
# root.title("JARVIS - AI Assistant")
# root.geometry("500x600")

# chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
# chat_display.pack(pady=10)

# text_entry = tk.Entry(root, width=50)
# text_entry.pack(pady=5)

# send_button = tk.Button(root, text="Send", command=send_text_command, width=15, height=2)
# send_button.pack()

# listen_button = tk.Button(root, text="Listen", command=start_listening, width=15, height=2)
# listen_button.pack()

# exit_button = tk.Button(root, text="Exit", command=root.quit, width=15, height=2)
# exit_button.pack(pady=5)

wishMe()
speak("Hello, I'm JARVIS")

root.mainloop()
