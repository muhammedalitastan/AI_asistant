import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

FILE_NAME = "daily.json"

def save_entry():
    date = date_entry.get().strip()
    text = text_area.get("1.0", tk.END).strip()
    
    if not date or not text:
        messagebox.showerror("Hata", "Lütfen tarih ve metin alanlarını doldurun!")
        return
    
    try:
        datetime.strptime(date, "%d-%m-%Y")  #%d-%m-%Y
    except ValueError:
        messagebox.showerror("Hata", "Tarihi 'DD-MM-YYYY' formatında girin!")
        return
    
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    
    data[date] = text
    
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    messagebox.showinfo("Başarılı", "Günlük kaydedildi!")
    text_area.delete("1.0", tk.END)

def load_entry():
    date = date_entry.get().strip()
    
    if not date:
        messagebox.showerror("Hata", "Lütfen bir tarih girin!")
        return
    
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data = json.load(f)
        text_area.delete("1.0", tk.END)
        text_area.insert("1.0", data.get(date, "Bu tarihe ait giriş bulunamadı."))
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showerror("Hata", "Henüz günlük kaydı yok!")

def run_diary_app():
    global root, date_entry, text_area
    root = tk.Tk()
    root.title("Günlük Uygulaması")
    root.geometry("400x400")

    tk.Label(root, text="Tarih (DD-MM-YYYY):").pack()
    date_entry = tk.Entry(root)
    date_entry.pack()

    text_area = tk.Text(root, height=10, width=40)
    text_area.pack()

    tk.Button(root, text="Kaydet", command=save_entry).pack()
    tk.Button(root, text="Yükle", command=load_entry).pack()

    root.mainloop()

run_diary_app()


































# import tkinter as tk
# from tkinter import messagebox
# import json
# from datetime import datetime

# FILE_NAME = "daily.json"

# def save_entry():
#     date = date_entry.get().strip()
#     text = text_area.get("1.0", tk.END).strip()
    
#     if not date or not text:
#         messagebox.showerror("Hata", "Lütfen tarih ve metin alanlarını doldurun!")
#         return
    
#     try:
#         datetime.strptime(date, "%Y-%m-%d")  # Tarih formatını doğrula
#     except ValueError:
#         messagebox.showerror("Hata", "Tarihi 'YYYY-MM-DD' formatında girin!")
#         return
    
#     try:
#         with open(FILE_NAME, "r", encoding="utf-8") as f:
#             data = json.load(f)
#     except (FileNotFoundError, json.JSONDecodeError):
#         data = {}
    
#     data[date] = text
    
#     with open(FILE_NAME, "w", encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=4)
    
#     messagebox.showinfo("Başarılı", "Günlük kaydedildi!")
#     text_area.delete("1.0", tk.END)

# def load_entry():
#     date = date_entry.get().strip()
    
#     if not date:
#         messagebox.showerror("Hata", "Lütfen bir tarih girin!")
#         return
    
#     try:
#         with open(FILE_NAME, "r", encoding="utf-8") as f:
#             data = json.load(f)
#         text_area.delete("1.0", tk.END)
#         text_area.insert("1.0", data.get(date, "Bu tarihe ait giriş bulunamadı."))
#     except (FileNotFoundError, json.JSONDecodeError):
#         messagebox.showerror("Hata", "Henüz günlük kaydı yok!")

# # Arayüz oluşturma
# root = tk.Tk()
# root.title("Günlük Uygulaması")
# root.geometry("400x400")

# tk.Label(root, text="Tarih (YYYY-MM-DD):").pack()
# date_entry = tk.Entry(root)
# date_entry.pack()

# text_area = tk.Text(root, height=10, width=40)
# text_area.pack()

# tk.Button(root, text="Kaydet", command=save_entry).pack()
# tk.Button(root, text="Yükle", command=load_entry).pack()

# root.mainloop()