class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print(f"My Name is {self.name} I am {self.age} years old.")

p1 = Person("Virat Kohli", 25)
p1.greet()