from datetime import datetime

s = input()

if "AM" in s.upper() or "PM" in s.upper():
    # 12-hour → 24-hour
    t = datetime.strptime(s, "%I:%M:%S %p")
    print(t.strftime("%H:%M:%S"))
else:
    # 24-hour → 12-hour
    t = datetime.strptime(s, "%H:%M:%S")
    print(t.strftime("%I:%M:%S %p"))