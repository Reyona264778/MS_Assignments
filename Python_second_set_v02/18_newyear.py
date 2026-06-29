from datetime import datetime

now = datetime(2026, 6, 29, 3, 44, 10)
new_year = datetime(2027, 1, 1, 0, 0, 0)

diff = new_year - now

print(f"{diff} days {diff.hour}:{diff.minute}:{diff.seconds}")