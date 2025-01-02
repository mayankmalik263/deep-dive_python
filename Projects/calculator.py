def sum(num1,num2):
    print("The addition of the two numbers is:",num1+num2)

def sub(num1,num2):
    print("The subtraction of the two numbers is:",num1-num2)

def mul(num1,num2):
    print("The Multiplication of the two numbers is:",num1*num2)
    
def div(num1,num2):
    if num1 == 0 or num2 == 0:
        print("Division cannot be done either of the inputs is 0")
    else:
        print("The Division of the two numbers is:",num1/num2)

num1=float(input("Enter your first number: "))
num2=float(input("Enter your second number: "))
op=input("Enter the operator(+ - / * ): ")

if op == '+':
    sum(num1,num2)
elif op == '-':
    sub(num1,num2)
elif op == '/':
    div(num1,num2)
else:
    mul(num1,num2)