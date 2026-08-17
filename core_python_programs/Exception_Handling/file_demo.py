try:
    with open("./data.txt.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("The file does not exist")

except PermissionError:
    print("You don't have permission to access this file")

finally:
    print("File operation completed")