class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print(f"My Name is {abc.name} I am {abc.age} years old.")

p1 = Person("Virat Kohli", 36)
p1.greet()