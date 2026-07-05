print("Mayank Malik")
print("o----")
print(" ||||")

print("=" * 10)

# ask the year we were born and then calculate and then print out of the age of the input user in the terminal

birthyear = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birthyear

if(age<0):
    print("Incorrent Input.")
elif(age==0):
    print("Congrats on having a baby this year.")
else:
    print(f"You are {age} years old.")

# covnerting the user entered weight in pounds to kilograms and printing it on terminal


weight_pounds = float(input("Enter your weight(in pounds): "))
weight_kg = weight_pounds * 0.4535924

print(f"Your weight in Kilograms is: {weight_kg}")

