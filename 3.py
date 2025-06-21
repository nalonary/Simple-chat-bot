
while True :
    name = input("Enter your name: ")
    if name.isalpha():
        print("Welcome, " + name + "!")
        break
    else:
        print("Please enter a valid name containing only letters.")

phone_number = input("Enter your phone number: ")
while True:
    if phone_number.isdigit() and len(phone_number) == 10:
        print("Your phone number is valid.")
        break
    else:
        print("Please enter a valid 10-digit phone number.")
        phone_number = input("Enter your phone number: ")

for i in phone_number:
    if i == "_":
        continue
    print(i, end=" ")
print()  # Print a newline after the phone number output


food = ["pizza", "burger", "pasta", "salad"]
drinks = ["tea" , "orange juce" , "water"]
desserts =["om ali" , "basbosa" , "chocolate"]
akl = [food, drinks, desserts]

print(akl[1][2])

student = ["nalonary", "17" , "male"]

print(student.count("nalonary"))  # Count occurrences of "nalonary"                                                     
print(student.index("17"))  # Find the index of "17" in the list
print(student[0:2])  # Print the first two elements of the list

if "nalonary" in student:
    print("nalonary is in the student list.")



import tkinter as tk
from tkinter import messagebox, filedialog

# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("تجربه كل عناصر واججه tk")
root.geometry("600x700")
root.configure(bg="#1E6CD1")

# دالة رسالة
def say_hello():
    messagebox.showinfo("رسالة", f"أهلاً يا نالوناري 😎")

# دالة لإظهار النص المُدخل
def show_entry():
    label_result.config(text="أنت كتبت: " + entry.get())

# دالة لتحديد ملف
def choose_file():
    file_path = filedialog.askopenfilename()
    label_file.config(text="الملف المختار:\n" + file_path)

# 🟦 1. عنوان (Label)
label = tk.Label(root, text="ده العنوان", font=("Arial", 18), fg="black", bg="#3fce22")
label.pack(pady=10)

# 🔲 2. زر (Button)
btn = tk.Button(root, text="اتكا عليا👋", command=say_hello, bg="lightgreen", font=("Arial", 14))
btn.pack(pady=10)

# 🟨 3. إدخال نص (Entry)
entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=10)

# 🔲 4. زر لعرض النص
btn_show = tk.Button(root, text="ده الي حضرتك كتبته✍️", command=show_entry)
btn_show.pack(pady=5)

# 🟧 5. نص النتيجة
label_result = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
label_result.pack(pady=5)

# 🟥 6. مربع نص كبير (Text)
text = tk.Text(root, height=5, width=50)
text.insert(tk.END, "هنا يمكنك كتابة ملاحظاتك...📝")
text.pack(pady=10)

# 🟩 7. زر لاختيار ملف
btn_file = tk.Button(root, text="اختر ملف 📂", command=choose_file)
btn_file.pack(pady=5)

label_file = tk.Label(root, text="", bg="#f0f0f0")
label_file.pack(pady=5)

# 🟦 8. Checkbox (Checkbutton)
is_checked = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="أنا موافق ✅", variable=is_checked, font=("Arial", 12), bg="#f0f0f0")
checkbox.pack(pady=5)

# 🟪 9. اختيار من مجموعة (Radiobutton)
chosen_option = tk.StringVar()
radio1 = tk.Radiobutton(root, text="خيار 1", variable=chosen_option, value="خيار 1", bg="#f0f0f0")
radio2 = tk.Radiobutton(root, text="خيار 2", variable=chosen_option, value="خيار 2", bg="#f0f0f0")
radio1.pack()
radio2.pack()

# 🟫 10. قائمة منسدلة (OptionMenu)
options = ["Python", "Java", "C++", "NalonaryLang"]
selected = tk.StringVar(value="اختر لغة")
dropdown = tk.OptionMenu(root, selected, *options)
dropdown.pack(pady=10)

# 🟨 11. إطار (Frame)
frame = tk.Frame(root, bg="lightblue", padx=10, pady=10)
frame.pack(pady=10)
tk.Label(frame, text="داخل إطار", bg="lightblue").pack()

# 🟧 12. Canvas (للرسم)
canvas = tk.Canvas(root, width=100, height=100, bg="white")
canvas.create_oval(10, 10, 90, 90, fill="red")  # دائرة
canvas.pack(pady=10)

# 🟦 تشغيل الواجهة
root.mainloop()

   

    