from datetime import datetime, timezone
from zoneinfo import ZoneInfo

utc_time = datetime(2026, 8, 17, 9, 0, tzinfo=timezone.utc)

ist_time = utc_time.astimezone(ZoneInfo("Asia/Kolkata"))
ny_time  = utc_time.astimezone(ZoneInfo("America/New_York"))
ti
print(ist_time)   # 2026-08-17 14:30:00+05:30
print(ny_time)    # 2026-08-17 05:00:00-04:00

# Convert local machine time to UTC
local_now = datetime.now().astimezone()   # attaches system's local tz
utc_now = local_now.astimezone(timezone.utc)