aldowal = {"masr":"Cairo", "usa": "Washington, D.C.", "france": "Paris", "germany": "Berlin", "italy": "Rome", "japan": "Tokyo", "canada": "Ottawa", "brazil": "Brasília"}

aldowal.update({"spain": "Madrid", "china": "Beijing"})
print (aldowal["masr"])
print (aldowal.get("usa"))
print (aldowal.keys())
print (aldowal.values())
print (aldowal.items())

for keys,values in aldowal.items():
   print(keys,values)




example = {"fork" , "spoon" , "knife"}

dishes = {"plate", "bowl"}
#example.update(dishes)

dinner = example.union(dishes)

example.add("plate")
example.remove("knife")

for x in dinner:
    print(x)


hates = {"femboys" , "girls" , "humans" ,"friends"}
loves = {"friends" ,"servants" ,"power" ,"fake feelings"}

print (hates.difference(loves))
print (loves.difference(hates))
print (loves.union(hates))
print (loves.intersection(hates))
print (loves.symmetric_difference(hates))   



import difflib

capitals = {
    "egypt": "Cairo",
    "usa": "Washington, D.C.",
    "france": "Paris",
    "germany": "Berlin",
    "italy": "Rome",
    "japan": "Tokyo",
    "canada": "Ottawa",
    "brazil": "Brasília",
}

# طباعة الدول
print("Available countries:")
for country in capitals:
    print("-", country.capitalize())

# إدخال المستخدم
user_input = input("Enter a country to get its capital: ").strip().lower()

# محاولة إيجاد أقرب دولة
closest_matches = difflib.get_close_matches(user_input, capitals.keys(), n=1, cutoff=0.4)

if closest_matches:
    match = closest_matches[0]
    print(f"The capital of {match.capitalize()} is {capitals[match]}")
else:
    print("Sorry, I don't know that country.")


def hello(first_name, last_name, age):
    print ("hello " + first_name + " " + last_name)
    print(f"Hello, {first_name} {last_name}!")
    print("You are "+ str(age) +" years old.")
    print("Have a nice day!")
    
hello("Nalonary", "san", 20)

def division(num_1, num_2):
    return num_1 / num_2
k = float(input("Enter the first number: "))
l = float(input("Enter the second number: "))
x =division(k,l)
print(f"The result of dividing {k} by {l} is: {round(x, 2)}")

def hello(first_name, middle, last_name):
    print("hello " + first_name + " " + middle + " " + last_name)

hello(middle="san", first_name="nalonary", last_name="femboy")

print(abs(round(float(input("Enter a number: ")))))


import random

x =random.randint(0,6)
y=random.random()
print(x)
print (y)

my_list=["paper","rock","scissors"]
z=random.choice(my_list)
print(z)

cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
random.shuffle(cards)
print("Shuffled cards:", cards)

try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError as e:
    print(e)
    print("Error: Cannot divide by zero.")
except ValueError as e:
    print (e)
    print("Error: Please enter valid integers.")
except TypeError as e:
    print(e)
    print("Error: Invalid type for division.")
except ImportError as e:
    print(e)
    print("Error: Required module not found.")
except KeyboardInterrupt as e:
    print(e)
    print("Error: Operation interrupted by user.")
except Exception as e:
    print(e)
    print("An unexpected error occurred.")
else:
    print("Division completed successfully.")
    print ("Result:", result)
finally:
    print("what ever happens, this will always execute because nalonar")

import os

path = "C:\\Users\\moham\\Desktop\\nana"
if os.path.exists(path):
    print("The file exists.")
    if os.path.isfile(path):
        print("It is a file.")
    elif os.path.isdir(path):
        print("It is a directory.")
else:
    print("The file does not exist.")    

import sys

try:
    text = "\n OMG!, this is so sexy girl or femboy idk!"
    with open("fax.txt", "a+", encoding="utf-8", errors="ignore") as file:
        file.write(text)
        file.seek(0)
        content = file.read()
        sys.stdout.buffer.write(content.encode('utf-8', errors='ignore'))
        print("\nFile closed?", file.closed)
except FileNotFoundError as e:
    print(e)
    print("Error: The file was not found.")
except IOError as e:
    print(e)
    print("Error: An I/O error occurred.")
except Exception as e:
    print(e)
    print("An unexpected error occurred.")
else:
    print("File read successfully.")
finally:
    print("This block always executes, because nalonary is here.")


import shutil
#copyfile= shutil.copyfile("fax.txt", "copy_fax.txt")
#copy=shutil.copy("fax.txt", "copy_fax.txt")
shutil.copy2("fax.txt", "copy_fax.txt")



