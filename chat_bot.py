import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import json
import os
from rapidfuzz import process
from datetime import datetime

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ================ replies ================
data_file = "bot_memory.json"
if not os.path.exists(data_file):
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump({
            "hi": "hi how can I help you?",
            "good morning": "Good morning! This is a beautiful day outside.",
            "do u know undertale?": "Yes..we are here again huh? Just me and you, comedian right?",
            "can u help me?": "Sure, what do you need help with?",
            "are you ai?": "Yes, but I'm just a chat bot... a simple one."
        }, f, indent=4)

with open(data_file, "r", encoding="utf-8") as f:
    replies = json.load(f)

if not os.path.exists(data_file):
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump({}, f)
else:
    # this to make sure everything here work
    try:
        with open(data_file, "r+", encoding="utf-8") as f:
            pass
    except PermissionError:
        messagebox.showerror("Permission Error", u can't run this file because there is a problem.")
        exit()

# ================ learn and answer ================
def get_response(user_input):
    user_input = user_input.lower()
    result = process.extractOne(user_input, replies.keys(), score_cutoff=90)
    if result:
        match, _, _ = result
        return replies[match]
    return None

def save_new_reply(question, answer):
    replies[question.lower()] = answer
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(replies, f, indent=4)

def log_message(sender, message):
    with open("chat_log.txt", "a", encoding="utf-8") as log:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        log.write(f"{timestamp} {sender}: {message}\n")

# ================ the GUI ================
root = tk.Tk()
root.title("Nalonary's simple chat bot")
root.geometry("1500x800")
root.iconbitmap("pic.ico")

# ================ themes and BGs ================
bg_images = {
    "Classic": "bg_classic.jpg",
    "Dark Mode": "bg_dark.jpg",
    "Anime Pink": "bg_pink.jpg",
    "Cyber Glitch": "bg_glitch.jpg",
    "Default": "background.jpg"
}
current_theme = "Default"
bg_image = ImageTk.PhotoImage(Image.open(bg_images[current_theme]).resize((1500, 800)))
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ================ avatar for bot ================
avatar_img = ImageTk.PhotoImage(Image.open("bot_avatar.png").resize((100, 100)))
avatar_label = tk.Label(root, image=avatar_img, bg="#122654")
avatar_label.place(x=20, y=20)

# ================ chat items ================
label = tk.Label(root, text="how can I help u today?", font=("Georgia", 30), fg="white", bg="#000000")
label.place(x=550, y=50)

chat_display = tk.Text(root, font=("Arial", 14), width=110, height=22, bg="#1e1e1e", fg="#00ffcc")
chat_display.place(x=150, y=150)
chat_display.insert(tk.END, "Bot: hi how can I help u today?\n")

entry = tk.Entry(root, font=("Arial", 14), width=110, bg="#0d0d0d", fg="white")
entry.place(x=150, y=700)

# ================ send button ================
def send():
    user_input = entry.get().strip()
    if not user_input:
        messagebox.showwarning("Warning", "Please enter a message.")
        return

    chat_display.insert(tk.END, f"You: {user_input}\n")
    log_message("You", user_input)
    entry.delete(0, tk.END)

    response = get_response(user_input)
    if response:
        chat_display.insert(tk.END, f"Bot: {response}\n")
        log_message("Bot", response)
    else:
        chat_display.insert(tk.END, "Bot: I don't know how to respond to that.\n")
        log_message("Bot", "I don't know how to respond to that.")
        if messagebox.askyesno("Teach Me", "Do you want to teach me a reply for this?"):
            new_answer = simpledialog.askstring("New Reply", f"What should I reply to: {user_input}")
            if new_answer:
                save_new_reply(user_input, new_answer)
                chat_display.insert(tk.END, "Bot: Thanks! I learned something new.\n")
                log_message("Bot", "Thanks! I learned something new.")

send_button = tk.Button(root, text="Send", font=("Arial", 14), command=send)
send_button.place(x=1250, y=700)

# ================ footer for nalonary (the developer) ================
footer = tk.Label(root, text="Developed by Nalonary", fg="#FFFFFF", bg="#1e1e1e", font=("Arial", 10))
footer.pack(side="bottom", pady=10)

# ================themes choose ================
def switch_theme():
    choice = simpledialog.askstring(
        "Choose Theme",
        "choose theme:\n1. Classic\n2. Dark Mode\n3. Anime Pink\n4. Cyber Glitch\n5. Default"
    )
    if not choice:
        return

    theme = {
        "1": "Classic",
        "2": "Dark Mode",
        "3": "Anime Pink",
        "4": "Cyber Glitch",
        "5": "Default"
    }.get(choice.strip())

    if theme and theme in bg_images:
        update_theme(theme)
    else:
        tk.messagebox.showerror("something went wrong","error!")

def update_theme(theme_name):
    global bg_image
    if theme_name in bg_images:
        bg_image = ImageTk.PhotoImage(Image.open(bg_images[theme_name]).resize((1500, 800)))
        bg_label.config(image=bg_image)
        bg_label.image = bg_image

    if theme_name in ["Classic", "Default"]:
        label.config(bg="#000000", fg="white")
        chat_display.config(bg="#1e1e1e", fg="#00ffcc")
        entry.config(bg="#0d0d0d", fg="white")
        footer.config(bg="#1e1e1e", fg="white")
    elif theme_name == "Dark Mode":
        label.config(bg="#111111", fg="#00ffff")
        chat_display.config(bg="#222222", fg="lime")
        entry.config(bg="#333333", fg="white")
        footer.config(bg="#111111", fg="#aaaaaa")
    elif theme_name == "Anime Pink":
        label.config(bg="#2aca7d", fg="#ff0400")
        chat_display.config(bg="#ffe6f0", fg="#c71585")
        entry.config(bg="#ffb6c1", fg="#000000")
        footer.config(bg="#ffccdd", fg="#800080")
    elif theme_name == "Cyber Glitch":
        label.config(bg="#0f001a", fg="#39ff14")
        chat_display.config(bg="#0d001a", fg="#ff00ff")
        entry.config(bg="#1a0033", fg="#00ffff")
        footer.config(bg="#0f001a", fg="#ff007f")

# theme change button
theme_button = tk.Button(root, text="Switch Theme", font=("Arial", 12), command=switch_theme, bg="#444444", fg="white")
theme_button.place(x=1350, y=50)

# ================ app turn on ================
root.mainloop()
