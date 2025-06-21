import tkinter as tk
from tkinter import messagebox , PhotoImage
import os
import random

root = tk.Tk()
root.title("thsi is my first GUI")
root.geometry("1200x800")
root.config(bg="#5ae44d")

def show_message():
    messagebox.showinfo("Message", ["hi", "welcome m***therf***er", "how are you?","we are stronger than u..undertale is the best story"][random.randint(0, 3)])

btn = tk.Button(root, text="Click Me", command=show_message, bg="#f0f0f0", fg="#333333", font=("Arial", 14))
btn.pack(pady=20)

try:
    icon = PhotoImage(file="download.jpg")  # لازم يكون في نفس المسار
    icon_label = tk.Label(root, image=icon, bg="#1e1e1e")
    icon_label.pack(pady=10)
except:
    ascii_art = r"""
      ( •_•)
     <)   )>╯   Nalonary is coding...
     /   \/
    """
    tk.Label(root, text=ascii_art, fg="lime", bg="#1e1e1e", font=("Courier", 12)).pack()

import difflib

replies = {
    "hi": "hi how can i help u?",
    "good morning": "good morning, this is beautifu day outside..it's a beautiful day outside. birds are singing, flowers are blooming... on days like this, kids like you... should be burning in hell.",
    "do u know undertale?": "yes..we are here again huh? just me and u comdian right? with your plasters, your flashing eyes..u should be praperd well because soon...your last hour strikes",
    "can u help me?": "Be man and depend on yourself, don't ask for help from anyone, you are the only one who can help yourself.",
    "are you ai?": "daaah?! of course? what do u think iam, huh? your mother fucker?",
    "good night": "good night, sleep well and don't let the bed bugs bite so cya",
    "i'm nalonary": "master...iam..your maid..your servant..your slave..your everything..i will do anything for you, master u my maker",
    "iam ": "if u not nalonary...come here and suck my virtical dick!",
}

# طباعة الدول
print("Available countries:")
for rep in replies:
    print("-", rep.capitalize())

# إدخال المستخدم
user_input = input("Enter a country to get its capital: ").strip().lower()

# محاولة إيجاد أقرب دولة
closest_matches = difflib.get_close_matches(user_input, replies.keys(), n=1, cutoff=0.4)

if closest_matches:
    match = closest_matches[0]
    print(f"The capital of {match.capitalize()} is {replies[match]}")
else:
    print("sorry, iam still poor chat bot not having much data to answer u")




# نص فخم
footer = tk.Label(root, text="Developed by Nalonary", fg="gray", bg="#1e1e1e", font=("Arial", 10))
footer.pack(side="bottom", pady=10)


root.mainloop()