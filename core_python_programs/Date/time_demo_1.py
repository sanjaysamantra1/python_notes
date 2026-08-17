from datetime import time

t = time(14, 30, 15, 500000)  # hour, min, sec, microsecond
print(t)                       # 14:30:15.500000
print(t.hour, t.minute, t.second, t.microsecond)
print(t.isoformat())           # 14:30:15.500000
print(time.fromisoformat("14:30:15"))