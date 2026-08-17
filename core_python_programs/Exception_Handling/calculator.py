def divide_numbers():
    try:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        result = number1 / number2

    except ValueError:
        print("Error: Please enter valid numbers")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

    else:
        print("Result:", result)

    finally:
        print("Calculator operation completed")


divide_numbers()