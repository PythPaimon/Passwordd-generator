import tkinter as tk
from tkinter import messagebox
import random
import string

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
root.config(bg="#141414")

radioframe = tk.Frame(root, width=200, height=200, bg="#141414")
radioframe.pack(side=tk.TOP)

# Tworzenie zmiennej StringVar dla przycisków radiowych
selected_value = tk.StringVar()
selected_value.set("litery")  # Domyślna wartość

# Tworzenie przycisków radiowych i przypisanie zmiennej
radio1 = tk.Radiobutton(radioframe, text="Litery", variable=selected_value, value="litery", bg="#141414", fg="White")
radio1.pack(padx=10, pady=10)
radio2 = tk.Radiobutton(radioframe, text="Litery i cyfry", variable=selected_value, value="litery i cyfry", bg="#141414", fg="White")
radio2.pack(padx=10, pady=10)
radio3 = tk.Radiobutton(radioframe, text="Litery, cyfry i znaki specjalne", variable=selected_value, value="litery, cyfry i znaki specjalne", bg="#141414", fg="White")
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

labelentry = tk.Frame(root, width=200, height=20, bg="#141414")
labelentry.pack(padx=10, pady=10)

entry = tk.Entry(labelentry, width=5)
entry.pack(side=tk.RIGHT)

label = tk.Label(labelentry, text="Liczba znaków", bg="#141414", fg="White")
label.pack(side=tk.LEFT)

buttonframe = tk.Frame(root, width=200, height=200, bg="#141414")
buttonframe.pack(padx=10, pady=10)

button = tk.Button(buttonframe, text="Generuj", command=generuj_haslo, bg="#141414", fg="White")
button.pack(padx=10, pady=10)

textframe = tk.Frame(root, width=60, height=30, bg="#141414")
textframe.pack(padx=10, pady=10)

text = tk.Text(textframe, height=10, width=40)
text.pack(padx=10, pady=10)

root.mainloop()
