# Functions for calculator operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Modulus by zero is not allowed"
    return a % b

# Input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition =", add(num1, num2))
print("Subtraction =", subtract(num1, num2))
print("Multiplication =", multiply(num1, num2))
print("Division =", divide(num1, num2))
print("Modulus =", modulus(num1, num2))