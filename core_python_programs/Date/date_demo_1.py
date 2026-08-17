from datetime import date

d = date(2026, 8, 17)
today = date.today()

print(d.year, d.month, d.day)     # 2026 8 17
print(d.weekday())                # 0=Mon ... 6=Sun -> 0 (Monday)
print(d.isoweekday())             # 1=Mon ... 7=Sun -> 1
print(d.isoformat())              # 2026-08-17
print(d.isocalendar())            # (year, week_number, weekday)
print(d.replace(year=2027))       # 2027-08-17 (returns new object)
print(date.fromisoformat("2026-08-17"))
print(date.fromordinal(739000))   # date from proleptic Gregorian ordinal
print(d.toordinal())              # day count since 0001-01-01