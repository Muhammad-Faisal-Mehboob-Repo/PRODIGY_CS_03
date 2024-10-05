import tkinter as tk
from tkinter import messagebox
import re

class PasswordStrengthChecker:
    def __init__(self, master):
        self.master = master
        master.title("Password Strength Checker")

        self.label = tk.Label(master, text="Enter your password:")
        self.label.pack()

        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()
        self.password_entry.bind("<KeyRelease>", self.check_password)

        self.criteria_frame = tk.Frame(master)
        self.criteria_frame.pack()

        self.length_label = tk.Label(self.criteria_frame, text="✓ At least 8 characters")
        self.length_label.grid(row=0, column=0)

        self.uppercase_label = tk.Label(self.criteria_frame, text="✓ At least 1 uppercase letter")
        self.uppercase_label.grid(row=1, column=0)

        self.lowercase_label = tk.Label(self.criteria_frame, text="✓ At least 1 lowercase letter")
        self.lowercase_label.grid(row=2, column=0)

        self.number_label = tk.Label(self.criteria_frame, text="✓ At least 1 number")
        self.number_label.grid(row=3, column=0)

        self.special_char_label = tk.Label(self.criteria_frame, text="✓ At least 1 special character")
        self.special_char_label.grid(row=4, column=0)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def check_password(self, event):
        password = self.password_entry.get()
        self.reset_labels()
        length_check = len(password) >= 8
        uppercase_check = bool(re.search(r'[A-Z]', password))
        lowercase_check = bool(re.search(r'[a-z]', password))
        number_check = bool(re.search(r'[0-9]', password))
        special_char_check = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
        if length_check:
            self.length_label.config(fg="green")
        if uppercase_check:
            self.uppercase_label.config(fg="green")
        if lowercase_check:
            self.lowercase_label.config(fg="green")
        if number_check:
            self.number_label.config(fg="green")
        if special_char_check:
            self.special_char_label.config(fg="green")
        if all([length_check, uppercase_check, lowercase_check, number_check, special_char_check]):
            self.result_label.config(text="Strong: Your password meets all the criteria.", fg="green")
        elif length_check and (uppercase_check + lowercase_check + number_check + special_char_check) >= 3:
            self.result_label.config(text="Medium: Your password is decent, but could be stronger.", fg="orange")
        else:
            self.result_label.config(text="Weak: Your password does not meet the required criteria.", fg="red")

    def reset_labels(self):
        self.length_label.config(fg="black")
        self.uppercase_label.config(fg="black")
        self.lowercase_label.config(fg="black")
        self.number_label.config(fg="black")
        self.special_char_label.config(fg="black")
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordStrengthChecker(root)
    root.mainloop()
