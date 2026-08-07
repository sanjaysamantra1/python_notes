class Employee:
    company = "ABC Technologies"

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_info(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", self.company)

    def calculate_bonus(self):
        return self.salary * 0.05


# Developer inherits Employee
class Developer(Employee):

    def __init__(self, emp_id, name, salary, programming_language):
        super().__init__(emp_id, name, salary)
        self.programming_language = programming_language

    def write_code(self):
        print(self.name, "is writing", self.programming_language, "code")

    # Method overriding
    def calculate_bonus(self):
        return self.salary * 0.10


# Manager also inherits Employee
class Manager(Employee):

    def __init__(self, emp_id, name, salary, team_size):
        super().__init__(emp_id, name, salary)
        self.team_size = team_size

    def conduct_meeting(self):
        print(self.name, "is conducting a team meeting")

    # Method overriding
    def calculate_bonus(self):
        return self.salary * 0.15


# Multilevel inheritance
class SeniorDeveloper(Developer):

    def __init__(
        self,
        emp_id,
        name,
        salary,
        programming_language,
        experience
    ):
        super().__init__(
            emp_id,
            name,
            salary,
            programming_language
        )

        self.experience = experience

    def review_code(self):
        print(self.name, "is reviewing code")