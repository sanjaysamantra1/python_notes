import calendar
from datetime import date

def get_first_last_day(year=None, month=None):
    today = date.today()
    year = year or today.year
    month = month or today.month

    first_day = date(year, month, 1)
    last_day = date(year, month, calendar.monthrange(year, month)[1])

    return first_day, last_day


# --- Usage ---
first_day, last_day = get_first_last_day(2026, 8)
print(first_day)  # 2026-08-01
print(last_day)   # 2026-08-31

# Defaults to current month if nothing passed
first_day, last_day = get_first_last_day()
print(first_day, last_day)