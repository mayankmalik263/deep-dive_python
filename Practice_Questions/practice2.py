# problem 1

num_1 = int(input("Enter the number: "))
if(num_1 % 2 == 0):
    print(f"The number {num_1} is an even number.")
else:
    print(f"The number {num_1} is an odd number.")

# problem 2

marks = int(input("Enter your marks to get the grade: "))

if(marks>=90):
    print("Your grade is A")
elif(marks>=75 and marks<90):
    print("Your grade is B")
elif(marks>=50 and marks<75):
    print("Your grade is C")
elif(marks<50):
    print("Your grade is F")

# problem 3

year = int(input("Enter the year: "))

if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("it is a leap year")
else:
    print("it is not a leap year")

# problem 4 (Mini Project)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

op = input("Select the operation (+,-,*,/): ")

if(op == "+"):
    print(f"Summation of {num1} & {num2} is: {num1 + num2}")
elif(op == "-"):
    print(f"Substraction of {num1} & {num2} is: {abs(num1 - num2)}")
elif(op == "*"):
    print(f"Multiplication of {num1} & {num2} is: {num1 * num2}")
elif(op == "/"):
    print(f"Division of {num1} & {num2} is: {round(num1 / num2, 2)}")