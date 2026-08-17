from datetime import date

today = date.today()
christmas = date(today.year, 12, 25)

# If Christmas has already passed this year
if today > christmas:
    christmas = date(today.year + 1, 12, 25)

days_left = (christmas - today).days

print("Today:", today)
print("Christmas:", christmas)
print("Days left for Christmas:", days_left)