import time

import math

name = None

while not name :
    name = input ("Enter your name: ")

print ("hello, {}!".format(name))


age = int(input ("Enter your age: "))
hight = float(input ("Enter your height in meters: "))

if (name[0].islower()):
    name = name.capitalize()

print ("hello m*****f**ker {}, your age is {}, and your height is {} meters".format(name, age, hight))

if age < 18:
    print ("You are a minor and your age is {}".format(age))
elif age == 18:
    print ("You are exactly 18 years old, welcome to adulthood!")  
else:
    print ("You are an adult and your age is {}".format(age))
print ("Thank you for using the age checker, {}".format(name))

time.sleep(2)

num = float(input("enter anynumber in your mind: " ))

print (round(num))
print (abs(num))
print (math.ceil(num))
print (math.floor(num))
print (math.sqrt(num))
print (math.pow(num, 2))

time.sleep(8)

z = float (input("Enter tha firtst number: "))
x = float (input("Enter the second number: "))
c = float (input("Enter the third number: "))

print ("i will find the biggest number between them!")

time.sleep(4)
print ("loading...")
time.sleep(10)

print ("the biggest number is: ", max(z, x, c))

time.sleep(2)

print ("i will put them in the list and sort them")

if z > x and z > c and x > c:
    print ("the sorted list is: ", [c, x, z])
elif z > x and z > c and c > x:
    print ("the sorted list is: ", [x, c, z])   
elif x > z and x > c and z > c:
    print ("the sorted list is: ", [c, z, x])
elif x > z and x > c and c > z:
    print ("the sorted list is: ", [z, c, x])
elif c > z and c > x and z > x:
    print ("the sorted list is: ", [x, z, c])
elif c > z and c > x and x > z:
    print ("the sorted list is: ", [z, x, c])
    
time.sleep(5)
print ("quistion time!")
print ("who is the stupid programmer?")
time.sleep(2)
print("u have 5 seconds to answer")
 

for answer in range(5, 0, -1):
    print(answer)
    time.sleep(1)
input("Enter your answer: ")

time.sleep(2)

print ("the answer is: nalonary san!")

time.sleep(5)

food = ["pizza", "burger", "pasta", "salad"]

dick = input("Enter your favorite food: ")
food.append(dick) 
food.sort() 
# Add the new favorite food to the end of the list

for x in food:
    print(x)

item = input("tell me what's food do u want to add: ")
position = int(input("Enter the position where you want to add it (0 to {}): ".format(len(food))))
food.insert(position, item)  # Insert the new food at the specified position

food.remove(input("tell me what food you don't like: "))
print("Here is the updated food list:")
for x in food:
    print(x)

def display_name():
    pussy = "hazet"
    print (pussy)

display_name()
pussy ="nalonary"
print(pussy)


def hit(*fucks):
    darb = 1
    for i in fucks:
        darb *= i
    return darb
print(hit(1,2,3,4))

def over(*nekah):
    kesma = nekah[0]
    for i in nekah[1:]:
        kesma /= i
    return kesma
print (over(20,5))

def say_hi(*people):
    for person in people:
        print(f"Hi {person}!")

say_hi("Ahmed", "Sara", "Ziad")

def show_info(**data):
    for key, value in data.items():
        print(f"{key} = {value}")

show_info(name="Nalonary", age=17)

def tagroba(**akwards):
    print("hellooo", end=" ")
    for key, value in akwards.items():
        print (value,key,  end=" ")
tagroba (first="nalonary", last="the ai developer", middle="san")
