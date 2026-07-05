# problem 1

for i in range(0,11):
    print(i)

# problem 2

for i in range(1,21):
    if(i % 2 == 0):
        print(i)
    else:
        pass

# problem 3
total = 0
s = [5,321,33,1,2,3] # sample list

for i in s:
    total = total + i

print(f"the total of all the elements in the is: {total}")

# problem 4

n = int(input("Enter the number: "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

# problem 5
count = 0
string_1 = input("Enter the word: ")

for i in string_1:
    if(i == 'a' or i == 'e' or i == 'i'or i == 'o' or i == 'u'):
        count = count + 1
    else:
        continue
print(f"The number of vowels are: {count}")

# problem 6

for j in range(1,6):
    print('*'*j)

# problem 7 (Mini Project)

import random
# list_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

x = random.choice(range(1,21))

guess = int(input("Guess the number(1-20): "))

while(guess != x):
    if(guess < x):
        print("Too low")
        guess = int(input("Guess the number(1-20): "))
    elif(guess > x):
        print("Too high")
        guess = int(input("Guess the number(1-20): "))

print(f"You guessed it! The number is {guess}")
