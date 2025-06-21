# this is my first python script

first_name = "nalonary"
last_name = "san"
name = first_name + " " + last_name
print ("hello, {}!".format(name))

age = 16
age += 1
print("I am " + str(age) + " years old.")
print (type(age))

hight = 1.37
print ("I am " + str(hight) + " meters tall.")
print(type(hight))

human = True
print("Am I human? " + str(human))

sandy = patrick = 30

print("Sandy's age is " + str(sandy) + " and Patrick's age is " + str(patrick))

fuck = 10.5
fuck = str(fuck)
print (fuck)
mo =10.5
mo = int(mo)
print(mo)

print(name.find("o"))  # Corrected to find the character 'o' in the string
print(name.count("a"))  # Corrected to count the occurrences of 'a' in the string
print(name.upper())

print(name.lower())
print(name.title())
print(name.replace("n", "N"))  # Corrected to replace 'n' with 'N'
print(name.split("  "))  # Corrected to split the name by space  
print(name.startswith("n"))  # Corrected to check if the name starts with 'n'
print (name.upper())
print (name.isalpha())  # Corrected to check if the name contains only alphabetic characters

funkey_name = name[::-1]
website = "https://google.com"
website2 ="https://wekebidia.com"

slice = slice (8,-4)

print (website[slice])
print (website2[slice])


print (funkey_name)


row = None
column = None

while row is None or column is None:
    try:
        row_input = input("How many rows?: ")
        column_input = input("How many columns?: ")

        # نحاول نحولهم لـ float أولاً عشان نقدر نتحقق لو فيهم كسور
        if '.' in row_input or '.' in column_input:
            raise ValueError("Floats are not allowed.")

        row = int(row_input)
        column = int(column_input)

    except ValueError as e:
        print("❌ Invalid input:", e)
        row = None
        column = None

symbol = input("Enter the shape: ")

for i in range(row):
    for j in range(column):
        print(symbol, end=" ")
    print()
    

drinks = ["water", "juice", "soda", "tea", "coffee"]
breakfast = ["eggs", "toast", "pancakes", "cereal"]
dessert = ["cake", "ice cream", "fruit salad"]

def display_menu():
    print("\nWelcome to the Food and Drink Menu!")
    print("1. Drinks")
    print("2. Breakfast")
    print("3. Dessert")
    print("4. Exit")

def display_items(items):
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")
    print(f"{len(items)+1}. Return to Main Menu")  # اختيار للرجوع

def handle_category(items, category_name):
    while True:
        print(f"\n{category_name} Menu:")
        display_items(items)
        choice = input("Select an item by number (or return): ")

        try:
            choice = int(choice)
            if 1 <= choice <= len(items):
                print(f"You selected: {items[choice - 1]}")
            elif choice == len(items) + 1:
                break  # يرجع للقائمة الرئيسية
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Please select an option (1-4): ")
        
        if choice == '1':
            handle_category(drinks, "Drinks")
        elif choice == '2':
            handle_category(breakfast, "Breakfast")
        elif choice == '3':
            handle_category(dessert, "Dessert")
        elif choice == '4':
            print("Thank you for using the menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()

# This code is a simple menu-driven program that allows users to view different food and drink categories.

namee = input("Enter your name: ")

print (namee.capitalize())
first_namee = namee[0:5].upper()
last_namee = namee[2:].lower()

print (first_namee)
print (last_namee)

beka ="a3333333"
tho = "nalonary"
print("{1} is ai developer {0}".format(beka, tho))
print("{tho} is ai developer {beka}".format(beka="a3333333", tho="nalonary"))
beta3y ="{} is Ai developer {}"
print(beta3y.format(tho, beka))

namo = "nalonary san"
print("hello, {}!".format(namo))
print("hello, {:20}. nice to meet u ,master ".format(namo))
print("hello, {:<20}. nice to meet u ,master ".format(namo, "nalonary san"))
print("hello, {:>20}. nice to meet u ,master ".format(namo, "nalonary san"))
print("hello, {:^20}. nice to meet u ,master ".format(namo, "nalonary san"))
binary_name = ' '.join(format(ord(c), '08b') for c in namo)
print("This name in binary is:", binary_name)

numboor =50000
print("this name in binarry is {:b}".format(numboor))
print("this name in hex is {:x}".format(numboor))
print("this name in pi is {:3f}".format(numboor))
print("this name in pi is {:,}".format(numboor)) 
