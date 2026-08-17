class Person:
  def __init__(self, name, age, add):
    self.name = name
    self.age = age
    self.add = add

  def __str__(self):
    return f"{self.name} {self.age} {self.add}"

p1 = Person("Virat Kohli", 36, "Bangalore")
print(p1)