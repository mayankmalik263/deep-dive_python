# correct email = mayankmalik@gmail.com
# correct password = 123456

email = input("Enter your email: ")
if '@' in email:
    password = input("Enter your password: ")
    if email == "mayankmalik@gmail.com" and password == "123456":
            print("Welcome to your account")
    elif email == "mayankmalik@gmail.com" and password != "123456":
            print("Invalid password")
            password = input("Enter your password again: ")
            if password == "123456":
                print("Welcome to your account")
            else:
                print("Invalid password again!")
    else:
            print("Invalid email or password")
else:
    print("Invalid email")
    
# WHILE LOOPS

# Where are loops used?
#loops are basically used (irl) to repeat a task multiple times without writing the same code again and again.
# for e.g : in a website there are different products shown on the home page, like the list of smartphones, laptops, etc.
# so, the display of the contents of each product are in a certain way which we can call containers, and we can use loops to display the contents of each container.
i = 1
n = int(input("Enter a number: "))
while (i<11):
    print(n, "x", i, "=", n*i)
    i +=1

# GUESSING GAME PROGRAM

import random

j = random.randint(1, 100)
n = int(input("Guess a number between 1 and 100: "))
counter = 1
while n != j:
    if n < j:
        print("Too low")
    else:
        print("Too high")
    n = int(input("Guess again: "))
    counter += 1
    
print("You guessed it right!")
print("You took",counter,"Attempts")