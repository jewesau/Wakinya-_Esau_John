# Assignment Two: Division with error handling

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        print("Cannot divide by zero. Try again.")
    else:
        print(f"Result: {result}")
        break
