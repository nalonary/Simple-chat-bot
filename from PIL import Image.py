from PIL import Image
import numpy as np

# الأحرف المستخدمة لتمثيل الألوان (كل ما راح لليمين = أفتح)
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)  # علشان تحافظ على الشكل النسبي
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")  # تحويل لصورة رمادية

def pixels_to_ascii(image):
    pixels = np.array(image).astype(int)  # ← التحويل هنا
    ascii_str = ""
    for row in pixels:
        for pixel in row:
            ascii_str += ASCII_CHARS[pixel * len(ASCII_CHARS) // 256]
        ascii_str += "\n"
    return ascii_str



def convert_image_to_ascii(path):
    try:
        image = Image.open(path)
    except Exception as e:
        print(f"Unable to open image. Error: {e}")
        return

    image = resize_image(image)
    image = grayify(image)

    ascii_art = pixels_to_ascii(image)
    print(ascii_art)

# 🔻 غيّر المسار ده لمسار الصورة بتاعتك
image_path = "pic.jpg"

convert_image_to_ascii(image_path)
