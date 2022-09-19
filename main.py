from math import *

# Assiment 1

print("Hello User")
name = input("name")
age = int(input("age"))
address = input("address")
number = [0,1,2,3,4,5,6,7,8,9]

for i in number :
    con = str(i) in name
    if con:
        print("Error")
        break
if not con :
    result = name

if type(age) is int:
    result2 = age
else:
    print("Error")

if name == "":
    print("Error")
elif age == "":
    print("Error")

print(f"Hello Mr/Ms {name} age {age} located in {address} thanks for beening one of our community, Enjoy")

# Assiment 2

num1 = float(input("number 1: "))
operator = input("operator: ")
num2 = float(input("number 2: "))
result = ""
if operator == "+":
    result = (num1 + num2)
elif operator == "-":
    result = (num1 - num2)
elif operator == "*":
    result = (num1 * num2)
elif operator == "/":
    result = (num1 / num2)
elif operator == "%":
    result = (num1 % num2)
elif operator == "^":
    result = (pow(num1, num2))
else:
    print("error")

op2 = input("Extra choices:"
            "1_Rounded the number"
            "2_Floor the number"
            "3_Exit: ")
if op2 == "1":
    print(round(result))
elif op2 == "2":
    print(floor(result))
elif op2 == "3":
    print(result)
else: print("Error")

# Assiment 3

numbers = []
conter = 0
while conter < 5:
    data = int(input("Get 5 numbers: "))
    numbers.append(data)
    conter += 1

op3 = input("Extra choices:"
            "1_max"
            "2_min: ")

if op3 == "1":
    print(max(numbers))
else:
    print(min(numbers))














