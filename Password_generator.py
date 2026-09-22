import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showwarning(
                "Invalid Length",
                "Password length should be at least 4."
            )
            return

        characters = ""

        # Character options
        if uppercase_var.get():
            characters += string.ascii_uppercase

        if lowercase_var.get():
            characters += string.ascii_lowercase

        if numbers_var.get():
            characters += string.digits

        if symbols_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showwarning(
                "No Characters Selected",
                "Please select at least one character type."
            )
            return

        password = ''.join(random.choice(characters) for _ in range(length))

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid password length."
        )


def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard."
        )
    else:
        messagebox.showwarning(
            "No Password",
            "Generate a password first."
        )


def clear_password():
    password_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    length_entry.insert(0, "12")



# Main Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x500")
root.resizable(False, False)
root.configure(bg="#f2f2f2")

# Title
title_label = tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 24, "bold"),
    bg="#f2f2f2",
    fg="#222222"
)
title_label.pack(pady=(25, 5))


subtitle_label = tk.Label(
    root,
    text="Create a strong and secure password",
    font=("Arial", 11),
    bg="#f2f2f2",
    fg="#555555"
)
subtitle_label.pack(pady=(0, 20))

# Password Length
length_frame = tk.Frame(root, bg="#f2f2f2")
length_frame.pack(pady=10)

length_label = tk.Label(
    length_frame,
    text="Password Length:",
    font=("Arial", 12),
    bg="#f2f2f2"
)
length_label.grid(row=0, column=0, padx=10)

length_entry = tk.Entry(
    length_frame,
    width=10,
    font=("Arial", 12),
    justify="center"
)
length_entry.grid(row=0, column=1, padx=10)
length_entry.insert(0, "12")

# Character Options
options_label = tk.Label(
    root,
    text="Select Character Types",
    font=("Arial", 13, "bold"),
    bg="#f2f2f2"
)
options_label.pack(pady=(20, 10))


uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)


uppercase_check = tk.Checkbutton(
    root,
    text="Uppercase Letters (A-Z)",
    variable=uppercase_var,
    font=("Arial", 11),
    bg="#f2f2f2"
)
uppercase_check.pack(anchor="w", padx=140)

lowercase_check = tk.Checkbutton(
    root,
    text="Lowercase Letters (a-z)",
    variable=lowercase_var,
    font=("Arial", 11),
    bg="#f2f2f2"
)
lowercase_check.pack(anchor="w", padx=140)

numbers_check = tk.Checkbutton(
    root,
    text="Numbers (0-9)",
    variable=numbers_var,
    font=("Arial", 11),
    bg="#f2f2f2"
)
numbers_check.pack(anchor="w", padx=140)

symbols_check = tk.Checkbutton(
    root,
    text="Symbols (!@#$...)",
    variable=symbols_var,
    font=("Arial", 11),
    bg="#f2f2f2"
)
symbols_check.pack(anchor="w", padx=140)


# Password Output
output_label = tk.Label(
    root,
    text="Generated Password",
    font=("Arial", 13, "bold"),
    bg="#f2f2f2"
)
output_label.pack(pady=(25, 8))


password_entry = tk.Entry(
    root,
    width=38,
    font=("Arial", 13),
    justify="center"
)
password_entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#f2f2f2")
button_frame.pack(pady=25)


generate_button = tk.Button(
    button_frame,
    text="Generate Password",
    command=generate_password,
    font=("Arial", 11, "bold"),
    padx=15,
    pady=8
)
generate_button.grid(row=0, column=0, padx=5)


copy_button = tk.Button(
    button_frame,
    text="Copy",
    command=copy_password,
    font=("Arial", 11, "bold"),
    padx=15,
    pady=8
)
copy_button.grid(row=0, column=1, padx=5)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_password,
    font=("Arial", 11, "bold"),
    padx=15,
    pady=8
)
clear_button.grid(row=0, column=2, padx=5)



root.mainloop()
