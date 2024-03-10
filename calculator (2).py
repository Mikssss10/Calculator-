history = []

def add(x, y):
    result = x + y
    operation = "{0} + {1} = {2}".format(x, y, result)
    print_result(operation)
    return result

def sub(x, y):
    result = x - y
    operation = "{0} - {1} = {2}".format(x, y, result)
    print_result(operation)
    return result

def mul(x, y):
    result = x * y
    operation = "{0} * {1} = {2}".format(x, y, result)
    print_result(operation)
    return result

def div(x, y):
    if y == 0:
        print("Cannot divide by zero")
    else:
        result = x / y
        operation = "{0} / {1} = {2}".format(x, y, result)
        print_result(operation)
    return result

def print_result(operation):
    print("Result:", operation)
    history.append(operation)

def display_history():
    print("History:")
    for operation in history:
        print(operation)

while True:
    print("Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show History")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '6':
        break

    elif choice == '5':
        display_history()

    elif choice in {'1', '2', '3', '4'}:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            add(num1, num2)
        elif choice == '2':
            sub(num1, num2)
        elif choice == '3':
            mul(num1, num2)
        elif choice == '4':
            div(num1, num2)

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")