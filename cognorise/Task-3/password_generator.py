import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Length must be greater than zero. Please try again.")
            return
        
        password = generate_password(length)
        generated_password_label.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter a valid integer for the length.")


root = tk.Tk()
root.title("Password Generator")


font_style = ("Arial", 16)

length_label = tk.Label(root, text="Enter the desired length of the password:", font=font_style)
length_label.pack()

length_entry = tk.Entry(root, font=font_style)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password, font=font_style)
generate_button.pack()

generated_password_label = tk.Label(root, text="", font=font_style)
generated_password_label.pack()


root.mainloop()
