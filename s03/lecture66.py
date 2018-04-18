from datetime import datetime

delta = datetime.now() - datetime(1900, 12, 31)
print(delta.days)

delta = datetime.now() - datetime(1984, 3, 16)
print(delta.days)

now = datetime.now()
print(now)

whenever = datetime.strptime("2017-12-31", "%Y-%m-%d")
print(whenever)

print(whenever.strftime("%Y"))