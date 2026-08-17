from datetime import date, timedelta

month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

first_date = date(year, month, 1)

if month == 12:
    next_month = date(year + 1, 1, 1)
else:
    next_month = date(year, month + 1, 1)

last_date = next_month - timedelta(days=1)

print("First date:", first_date)
print("Last date:", last_date)