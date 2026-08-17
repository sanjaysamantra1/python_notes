# Capturing the Exception Object
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)

except ZeroDivisionError as e:
    print("Error occurred:", e)