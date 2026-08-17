from datetime import datetime

now = datetime.now()

print(now.strftime("%Y-%m-%d"))              # 2026-08-17
print(now.strftime("%d/%m/%Y"))              # 17/08/2026
print(now.strftime("%B %d, %Y"))             # August 17, 2026
print(now.strftime("%A, %d %b %Y"))          # Monday, 17 Aug 2026
print(now.strftime("%H:%M:%S"))              # 14:30:00
print(now.strftime("%I:%M %p"))              # 02:30 PM
print(now.strftime("%Y-%m-%dT%H:%M:%S%z"))   # ISO-like with offset (aware dt only)