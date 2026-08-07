class Student:
    school = "DPS"  # Class property

    def __init__(self, name, age):
        self.name = name  # Object property
        self.age = age    # Object property


student1 = Student("Rahul", 15)
student2 = Student("Priya", 16)

print(student1.name)    # Rahul
print(student2.name)    # Priya

print(student1.school)  # DPS
print(student2.school)  # DPS