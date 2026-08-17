from datetime import date, time, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

# --- Creating dates/times ---
d = date(2026, 8, 17)
t = time(14, 30, 0)
dt = datetime(2026, 8, 17, 14, 30, 0)

today = date.today()
now = datetime.now()

print(today)   # 2026-08-17
print(now)     # 2026-08-17 14:30:12.123456

# --- Timezone-aware datetime ---
utc_now = datetime.now(timezone.utc)
ist_now = datetime.now(ZoneInfo("Asia/Kolkata"))
print(utc_now)   # 2026-08-17 09:00:12+00:00
print(ist_now)   # 2026-08-17 14:30:12+05:30

# --- Converting between timezones ---
utc_time = datetime(2026, 8, 17, 9, 0, tzinfo=timezone.utc)
ist_time = utc_time.astimezone(ZoneInfo("Asia/Kolkata"))
print(ist_time)  # 2026-08-17 14:30:00+05:30

# --- Formatting (datetime -> string) ---
print(now.strftime("%Y-%m-%d"))            # 2026-08-17
print(now.strftime("%d %b %Y, %I:%M %p"))  # 17 Aug 2026, 02:30 PM
print(now.strftime("%A"))                  # Sunday (day name)

# --- Parsing (string -> datetime) ---
parsed = datetime.strptime("17-08-2026", "%d-%m-%Y")
print(parsed)  # 2026-08-17 00:00:00

# --- ISO format (best for storage/APIs) ---
print(now.isoformat())                     # 2026-08-17T14:30:12.123456
print(datetime.fromisoformat("2026-08-17T14:30:00"))

# --- Date arithmetic with timedelta ---
tomorrow = today + timedelta(days=1)
last_week = today - timedelta(weeks=1)
print(tomorrow, last_week)

# Difference between two dates
d1 = date(2026, 1, 1)
d2 = date(2026, 8, 17)
diff = d2 - d1
print(diff.days)  # 228

# --- Comparing dates ---
print(d2 > d1)  # True

# --- Useful attributes ---
print(now.year, now.month, now.day, now.hour, now.weekday())
# weekday(): Monday=0 ... Sunday=6

# --- Common format codes ---
# %Y = 4-digit year   %y = 2-digit year
# %m = month (01-12)  %B = full month name   %b = short month name
# %d = day (01-31)    %A = full weekday      %a = short weekday
# %H = hour (24h)     %I = hour (12h)        %p = AM/PM
# %M = minute         %S = second