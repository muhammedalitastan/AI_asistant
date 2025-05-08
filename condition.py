
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

def condition():
    usage = str(psutil.cpu_percent())
    speak(f"CPU is at {usage} percentage")
    print(f"CPU is at {usage} percentage")
    battery = psutil.sensors_battery()
    percentage = battery.percent
    speak(f"Boss our system have {percentage} percentage battery")
    print(f"Boss our system have {percentage} percentage battery")

    if percentage>=80:
        speak("Boss we could have enough charging to continue our recording")
        print("Boss we could have enough charging to continue our recording")
    elif percentage>=40 and percentage<=75:
        speak("Boss we should connect our system to charging point to charge our battery")
        speak("Boss we should connect our system to charging point to charge our battery")


    else:
        speak("Boss we have very low power, please connect to charging otherwise recording should be off...")
        speak("Boss we have very low power, please connect to charging otherwise recording should be off...")
