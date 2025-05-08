
import datetime
import os
import sys
import time
import webbrowser
import pyautogui
import pyttsx3 #!pip install pyttsx3
import speech_recognition as sr
import json
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random
import numpy as np
import psutil 
import subprocess

from initilize_engine import initialize_engine, command,speak
from utils import cal_day  # Artık burada doğrudan çağırabiliyoruz
from wishMe import wishMe
from social_media import social_media
from open_close_app import openApp,closeApp
# from arayüz import arayüz  # ✅ arayüz.py dosyasını içe aktar

# def send_text_command():
#     """Kullanıcının metin girişini alıp execute_command fonksiyonunu çalıştırır."""
#     user_input = text_entry.get()
#     text_entry.delete(0, "end")  # Giriş kutusunu temizle
#     threading.Thread(target=execute_command, args=(user_input,)).start()

# def start_listening():
#     """Sesli komutları dinleyip execute_command fonksiyonunu çalıştırır."""
#     threading.Thread(target=execute_command).start()

# # ✅ Arayüzü başlatmadan önce fonksiyonları tanımladık!
# root, chat_display, text_entry = arayüz(send_text_command, start_listening)

# query = text_entry if text_entry else command().lower()



def browsing(query):
    # def send_text_command():
    #     """Kullanıcının metin girişini alıp execute_command fonksiyonunu çalıştırır."""
    #     user_input = text_entry.get()
    #     text_entry.delete(0, "end")  # Giriş kutusunu temizle
    #     threading.Thread(target=execute_command, args=(user_input,)).start()

    # def start_listening():
    #     """Sesli komutları dinleyip execute_command fonksiyonunu çalıştırır."""
    #     threading.Thread(target=execute_command).start()

    # root, chat_display, text_entry = arayüz(send_text_command, start_listening)

    # def execute_command(input_text=None):
    #     aranacak = input_text if input_text else command().lower()
    #     chat_display.insert(tk.END, f"You: {aranacak}\n")
    #     return aranacak

    if 'google' in query:
        speak("Boss, what should i search on google..")
        s = command().lower()
        

        # Path to Opera browser (adjust based on your system)
        opera_path = "Opera_tarayıcı.lnk"

        try:
            os.startfile(opera_path)
            webbrowser.open(f"https://www.google.com/search?q={s}")
        except Exception as e:
            print(f"Tarayıcıyı açarken şu sıkıntı var:{e}")
    