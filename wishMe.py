import datetime
import time
from initilize_engine import speak
from utils import cal_day  # Yeni modülden import ettik

def wishMe():
    hour = int(datetime.datetime.now().hour)
    t = time.strftime("%I:%M %p")
    day = cal_day()

    if (hour >= 0) and (hour <= 12) and ('AM' in t):
        speak(f"Good Morning Muhammed Ali How are you, are you fine?, it's {day} and the time is {t}")
    elif (hour >= 12) and (hour <= 16) and ('PM' in t):
        speak(f"Good afternoon Muhammed Ali How are you, are you fine?, it's {day} and the time is {t}")
    else:
        speak(f"Good evening Muhammed Ali How are you, are you fine?, it's {day} and the time is {t}")
