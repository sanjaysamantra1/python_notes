# Declare variables and check their data types
age = 25
print(age, "-", type(age))

price = 99.99
print(price, "-", type(price))


name = "Python"
print(name, "-", type(name))

is_active = True
print(is_active, "-", type(is_active))

fruits = ["Apple", "Mango", "Orange"]
print(fruits, "-", type(fruits))

colors = ("Red", "Green", "Blue")
print(colors, "-", type(colors))

numbers = range(1, 6)
print(numbers, "-", type(numbers))

unique_numbers = {1, 2, 3, 4}
print(unique_numbers, "-", type(unique_numbers))

fixed_set = frozenset([1, 2, 3, 4])
print(fixed_set, "-", type(fixed_set))

student = {"id": 101, "name": "Sanjay"}
print(student, "-", type(student))

byte_data = b"Hello"
print(byte_data, "-", type(byte_data))

byte_array = bytearray(b"Hello")
print(byte_array, "-", type(byte_array))

memory_view = memoryview(b"Hello")
print(memory_view, "-", type(memory_view))

value = None
print(value, "-", type(value))