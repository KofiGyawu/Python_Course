# Create a simple calculator that can perform basic arithmetic
# operations like addition, subtraction, multiplication, and division.

# Defining Operations
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Can be divided by zero"


def power(x, y):
    return x ** y


def calculator():
    print("select your choice of operation")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Power")

    # Take user Input
    selection = input("Enter your choice: ")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Perform Calculation (using conditional statements)
    if selection == '1':
        result = add(num1, num2)
    elif selection == '2':
        result = subtract(num1, num2)
    elif selection == '3':
        result = multiply(num1, num2)
    elif selection == '4':
        result = divide(num1, num2)
    elif selection == '5':
        result = power(num1, num2)
    else:
        result = "Invalid"

    # Print the results
    print(f"Result: {result}")


calculator()
