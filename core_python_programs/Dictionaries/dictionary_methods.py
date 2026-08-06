employee = {
    "name": "John",
    "age": 30,
    "city": "Bangalore",
    "salary": 50000
}


# 1. get()
# Get value using a key

print(employee.get("name"))
# John

print(employee.get("department", "Not Available"))
# Not Available


# 2. keys()
# Get all keys

print(employee.keys())
# dict_keys(['name', 'age', 'city', 'salary'])


# 3. values()
# Get all values

print(employee.values())
# dict_values(['John', 30, 'Bangalore', 50000])


# 4. items()
# Get all key-value pairs as tuples

print(employee.items())
# dict_items([
#   ('name', 'John'),
#   ('age', 30),
#   ('city', 'Bangalore'),
#   ('salary', 50000)
# ])


# 5. copy()
# Create a shallow copy of the dictionary

employee_copy = employee.copy()

print(employee_copy)
# {'name': 'John', 'age': 30, 'city': 'Bangalore', 'salary': 50000}


# 6. setdefault()
# Return value if key exists

print(employee.setdefault("name", "Unknown"))
# John

# If key doesn't exist, create it

employee.setdefault("department", "IT")

print(employee)
# {
#   'name': 'John',
#   'age': 30,
#   'city': 'Bangalore',
#   'salary': 50000,
#   'department': 'IT'
# }


# 7. update()
# Add/update multiple key-value pairs

employee.update({
    "salary": 60000,
    "experience": 5
})

print(employee)
# {
#   'name': 'John',
#   'age': 30,
#   'city': 'Bangalore',
#   'salary': 60000,
#   'department': 'IT',
#   'experience': 5
# }


# 8. pop()
# Remove a specific key and return its value

removed_salary = employee.pop("salary")

print(removed_salary)
# 60000


# 9. popitem()
# Remove and return the LAST inserted key-value pair

last_item = employee.popitem()

print(last_item)
# ('experience', 5)


# 10. fromkeys()
# Create a NEW dictionary using specified keys

fields = ("id", "email", "phone")

new_employee = dict.fromkeys(fields, "Not Provided")

print(new_employee)
# {
#   'id': 'Not Provided',
#   'email': 'Not Provided',
#   'phone': 'Not Provided'
# }


# 11. clear()
# Remove everything from dictionary

employee.clear()

print(employee)
# {}