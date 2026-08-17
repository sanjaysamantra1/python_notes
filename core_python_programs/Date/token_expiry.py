from datetime import datetime, timedelta

expiry = datetime.now() + timedelta(minutes=30)
is_expired = datetime.now() > expiry
print(is_expired)