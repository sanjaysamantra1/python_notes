# ============================================================
# Employee Programs - Python
# ============================================================

employees = [
    {"eId": 101, "name": "sanjay", "sal": 5000, "gender": "male"},
    {"eId": 104, "name": "geeta", "sal": 8000, "gender": "female"},
    {"eId": 103, "name": "sameer", "sal": 7000, "gender": "male"},
    {"eId": 102, "name": "sita", "sal": 9000, "gender": "female"},
    {"eId": 105, "name": "deepak", "sal": 8000, "gender": "male"}
]


# ============================================================
# 1. Sort employees in ascending order by employee ID
# ============================================================

employees_by_id = sorted(employees, key=lambda emp: emp["eId"])

print("\n1. Employees sorted by ID:")
for emp in employees_by_id:
    print(emp)


# ============================================================
# 2. Sort employees in ascending order by name
# ============================================================

employees_by_name = sorted(employees, key=lambda emp: emp["name"])

print("\n2. Employees sorted by name:")
for emp in employees_by_name:
    print(emp)


# ============================================================
# 3. Find the employee with the highest salary
# ============================================================

highest_paid_employee = max(employees, key=lambda emp: emp["sal"])

print("\n3. Employee with highest salary:")
print(highest_paid_employee)


# ============================================================
# 4. Filter employees whose salary is between 6000 and 8000
# ============================================================

filtered_employees = [
    emp
    for emp in employees
    if 6000 <= emp["sal"] <= 8000
]

print("\n4. Employees with salary between 6000 and 8000:")
for emp in filtered_employees:
    print(emp)


# ============================================================
# 5. Increase salary of every employee by 10%
# ============================================================

employees_with_increment = [
    {
        **emp,
        "sal": emp["sal"] * 1.10
    }
    for emp in employees
]

print("\n5. Employees after 10% salary increment:")
for emp in employees_with_increment:
    print(emp)


# ============================================================
# 6. Add "comp": "ibm" to every employee
# ============================================================

employees_with_company = [
    {
        **emp,
        "comp": "ibm"
    }
    for emp in employees
]

print("\n6. Employees with company:")
for emp in employees_with_company:
    print(emp)


# ============================================================
# 7. Add department information to each employee
# ============================================================

employees_for_dept = [
    {
        "eId": 101,
        "name": "sanjay",
        "sal": 5000,
        "gender": "male"
    },
    {
        "eId": 104,
        "name": "reena",
        "sal": 8000,
        "gender": "female"
    }
]

departments = [
    {"eId": 101, "dept": "sales"},
    {"eId": 104, "dept": "marketing"}
]


# Create lookup dictionary
dept_lookup = {
    dept["eId"]: dept["dept"]
    for dept in departments
}

employees_with_dept = [
    {
        **emp,
        "dept": dept_lookup.get(emp["eId"])
    }
    for emp in employees_for_dept
]

print("\n7. Employees with department:")
for emp in employees_with_dept:
    print(emp)


# ============================================================
# 8. Print occurrence of each element
# ============================================================

numbers = [10, 20, 30, 40, 50, 10, 30, 50]

occurrences = {}

for num in numbers:
    occurrences[num] = occurrences.get(num, 0) + 1

print("\n8. Occurrence of each element:")
print(occurrences)

# Output:
# {10: 2, 20: 1, 30: 2, 40: 1, 50: 2}


# ============================================================
# 9. Group employees by name
# ============================================================

employees_for_grouping = [
    {"eId": 101, "name": "sanjay", "sal": 5000},
    {"eId": 102, "name": "alok", "sal": 6000},
    {"eId": 103, "name": "sanjay", "sal": 7000},
    {"eId": 104, "name": "alok", "sal": 8000},
    {"eId": 105, "name": "deepak", "sal": 9000}
]

grouped_by_name = {}

for emp in employees_for_grouping:

    name = emp["name"]

    if name not in grouped_by_name:
        grouped_by_name[name] = []

    grouped_by_name[name].append(emp)

print("\n9. Employees grouped by name:")
print(grouped_by_name)


# ============================================================
# 10. Find total salary of all male employees
# ============================================================

total_male_salary = sum(
    emp["sal"]
    for emp in employees
    if emp["gender"] == "male"
)

print("\n10. Total salary of male employees:")
print(total_male_salary)

# sanjay = 5000
# sameer = 7000
# deepak = 8000
#
# Total = 20000


# ============================================================
# 11. Count employees by gender
# ============================================================

gender_count = {}

for emp in employees:

    gender = emp["gender"]

    gender_count[gender] = gender_count.get(gender, 0) + 1

print("\n11. Employee count by gender:")
print(gender_count)

# Output:
# {'male': 3, 'female': 2}