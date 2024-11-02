import tkinter as tk
from tkinter import messagebox
import random
import string
from ttkbootstrap import Style

def error():
    messagebox.showerror("Błąd", "Błąd")

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

set1 = letters
set2 = letters + digits
set3 = letters + digits + special_chars

root = tk.Tk()
root.geometry("800x500")
root.title("Password Generator")
style = Style(theme="pulse")

radioframe = tk.Frame(root, width=200, height=200)
radioframe.pack(side=tk.TOP)

# Tworzenie zmiennej StringVar dla przycisków radiowych
selected_value = tk.StringVar()
selected_value.set("litery")  # Domyślna wartość

# Tworzenie przycisków radiowych i przypisanie zmiennej
radio1 = tk.Radiobutton(radioframe, text="Litery", variable=selected_value, value="litery")
radio1.pack(padx=10, pady=10)
radio2 = tk.Radiobutton(radioframe, text="Litery i cyfry", variable=selected_value, value="litery i cyfry")
radio2.pack(padx=10, pady=10)
radio3 = tk.Radiobutton(radioframe, text="Litery, cyfry i znaki specjalne", variable=selected_value, value="litery, cyfry i znaki specjalne")
radio3.pack(padx=10, pady=10)

def generuj_haslo():
    try:
        dlugosc = int(entry.get())  # Konwersja wartości z Entry na liczbę całkowitą
        if dlugosc <= 0:
            error()
            return

        if selected_value.get() == "litery":
            haslo = ''.join(random.choices(set1, k=dlugosc))
        elif selected_value.get() == "litery i cyfry":
            haslo = ''.join(random.choices(set2, k=dlugosc))
        else:  # "litery, cyfry i znaki specjalne"
            haslo = ''.join(random.choices(set3, k=dlugosc))

        text.insert('end', haslo + '\n')
    except ValueError:
        error()

label1frame = tk.Frame(root,width=200, height=10)
label1frame.pack(side=tk.LEFT)

entry1frame = tk.Frame(root, width=200, height=200)
entry1frame.pack(side=tk.RIGHT)

entry = tk.Entry(entry1frame, width=5)
entry.pack(side=tk.LEFT)

label = tk.Label(label1frame, text="Liczba znaków")
label.pack(padx=10, pady=10)

buttonframe = tk.Frame(root, width=200, height=200)
buttonframe.pack(padx=10, pady=10)

button = tk.Button(buttonframe, text="Generuj", command=generuj_haslo)
button.pack(padx=10, pady=10)

textframe = tk.Frame(root, width=60, height=30)
textframe.pack(padx=10, pady=10)

text = tk.Text(textframe, height=10, width=40)
text.pack(padx=10, pady=10)

root.mainloop()
