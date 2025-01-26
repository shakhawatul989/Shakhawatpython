import math

# Define functions for basic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def square(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def exponentiate(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error: Cannot take square root of a negative number."
    return math.sqrt(a)

def meters_to_kilometers(meters):
    return meters / 1000

# Display menu options
def show_menu():
    print("Hey Shakhawat! Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (**)")
    print("6. Modulus (%)")
    print("7. Square Root (√)")
    print("8. Convert Meters to Kilometers")
    print("9. Exit")

# Get user choice
def get_choice():
    choice = input("Enter your choice (1/2/3/4/5/6/7/8/9): ")
    return choice

# Perform the calculation based on user choice
def calculate(choice):
    if choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
        # Get input numbers
        if choice != '7' and choice != '8':  # For square root and conversion, only one input
            num1 = float(input("Enter the first number: "))
            if choice != '7':  # Only get second number if it's not for square root
                num2 = float(input("Enter the second number: "))
        else:
            num1 = float(input("Enter the number: "))

        # Perform operation
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", square(num1, num2))
        elif choice == '6':
            print("Result:", modulus(num1, num2))
        elif choice == '7':
            print("Result:", square_root(num1))
        elif choice == '8':
            print(f"{num1} meters = {meters_to_kilometers(num1):.2f} kilometers")
        elif choice == '9':
            print("Exiting the calculator. Goodbye!")
            return False
    else:
        print("Invalid choice! Please try again.")
    return True

# Main program loop
while True:
    show_menu()
    user_choice = get_choice()
    if not calculate(user_choice):
        break
