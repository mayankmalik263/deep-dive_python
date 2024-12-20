# correct email = mayankmalik@gmail.com
# correct password = 123456

email = input("Enter your email: ")
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