class Employee:
    def __init__(self, name, age, add):
        self.name = name
        self.age = age
        self.add = add
    
emp1 = Employee('sanjay', 35, 'Bangalore')
print(f"Name: {emp1.name}  Age: {emp1.age}  Address: {emp1.add}")