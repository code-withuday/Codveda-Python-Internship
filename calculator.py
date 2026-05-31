def add(a , b):
    return a + b

def subtract(a , b):
    return a - b

def multiply(a , b):
    return a * b

def divide(a , b):
    if(b == 0):
        return "cannot divided by zero"

    return a / b

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("choose opreation: "))

if(choice == 1):
    print("Result =", add(num1,num2))

elif(choice == 2):
    print("Result =",subtract(num1,num2))

elif(choice == 3):
    print("Result =",multiply(num1,num2))

elif(choice == 4):
    print("Result =",divide(num1,num2))

else:
    print("Invalid choice")