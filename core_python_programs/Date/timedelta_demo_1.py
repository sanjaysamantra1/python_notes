from datetime import datetime, timedelta

delta = timedelta(days=5, hours=3, minutes=30)
print(delta)              # 5 days, 3:30:00
print(delta.days)         # 5
print(delta.seconds)      # 12600 (seconds beyond full days)
print(delta.total_seconds())  # 444600.0

now = datetime.now()
future = now + timedelta(weeks=2)
past = now - timedelta(days=10)

# Difference between two datetimes returns a timedelta
diff = future - past
print(diff.days)          # ~24

# Comparisons
print(future > now)       # True

# Multiplying / dividing a timedelta
double_delta = delta * 2
half_delta = delta / 2