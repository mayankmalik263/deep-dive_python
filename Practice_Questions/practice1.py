# problem 1

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}, you are {age} years old!")

# problem 2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum = num1 + num2
if(num1>num2):
    diff = num1-num2
else:
    diff = num2-num1
prod = num1*num2
div = int(num1/num2)

print(f"sum = {sum}")
print(f"difference = {diff}")
print(f"product = {prod}")
print(f"division = {div}")

# problem 3

# C = (F − 32) × 5/9
# F = C × 9/5 + 32

C = int(input("Enter the temp(in celsius): "))
F = (C * 9/5) + 32
print(f"the temp {C} in Fahrenheit is: {F}")

# problem 4
count = 0
s = input("Give me a sentence: ")
for i in s:
    if(i == " "):
        pass
    else:
        count = count + 1
print(f"Total number of characters(excluding spaces) in the string is: {count}")

# Micro Project

name_1 = input("Enter the name: ")
age_1 = int(input("Enter your age: "))
fav_lang = input("Enter your fav programming language: ")
birth_year = 2025 - age_1

print(f"Hello {name_1}, you were born in {birth_year} and you love {fav_lang}!")