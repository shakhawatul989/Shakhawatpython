def kilograms_to_grams(kilograms):
    return kilograms * 1000

def miles_to_kilometers(miles):
    return miles / 0.621371

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def liters_to_gallons(liters):
    return liters * 0.264172

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def show_menu():
    print("\n--- Unit Converter Menu ---")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Miles")
    print("3. Celsius to Fahrenheit")
    print("4. Kilograms to Pounds")
    print("5. Kilograms to Grams")
    print("6. Miles to Kilometers")
    print("7. Fahrenheit to Celsius")
    print("8. Liters to Gallons")
    print("9. Pounds to Kilograms")
    print("10. Exit")

# The rest of the logic would remain the same. You can use a similar pattern for the new conversions.
import math

def exponentiate(a, b):
    return a ** b

def square_root(a):
    return math.sqrt(a)

def modulo(a, b):
    return a % b

def factorial(a):
    if a < 0:
        return "Error: Factorial is not defined for negative numbers."
    return math.factorial(int(a))

def show_menu():
    print("Hey Shakhawat! Welcome to the Enhanced Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (x^y)")
    print("6. Square Root (√x)")
    print("7. Modulo (%)")
    print("8. Factorial (!)")
    print("9. Exit")

def calculate(choice):
    if choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
        num1 = float(input("Enter the first number: "))

        if choice == '1':
            num2 = float(input("Enter the second number: "))
            print("Result:", add(num1, num2))
        elif choice == '2':
            num2 = float(input("Enter the second number: "))
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            num2 = float(input("Enter the second number: "))
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            num2 = float(input("Enter the second number: "))
            print("Result:", divide(num1, num2))
        elif choice == '5':
            num2 = float(input("Enter the exponent: "))
            print("Result:", exponentiate(num1, num2))
        elif choice == '6':
            print("Result:", square_root(num1))
        elif choice == '7':
            num2 = float(input("Enter the second number: "))
            print("Result:", modulo(num1, num2))
        elif choice == '8':
            print("Result:", factorial(num1))
        elif choice == '9':
            print("Exiting the calculator. Goodbye!")
            return False
    else:
        print("Invalid choice! Please try again.")
    return True

