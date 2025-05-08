import tkinter as tk
from tkinter import scrolledtext

def arayüz(send_text_command,start_listening):
    
    root = tk.Tk()
    root.title("JARVIS - AI Assistant")
    root.geometry("500x600")

    chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
    chat_display.pack(pady=10)

    text_entry = tk.Entry(root, width=50)
    text_entry.pack(pady=5)

    send_button = tk.Button(root, text="Send", command=send_text_command, width=15, height=2)
    send_button.pack()

    listen_button = tk.Button(root, text="Listen", command=start_listening, width=15, height=2)
    listen_button.pack()

    exit_button = tk.Button(root, text="Exit", command=root.quit, width=15, height=2)
    exit_button.pack(pady=5)

    return root, chat_display, text_entry
