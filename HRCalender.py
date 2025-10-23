import datetime

m, d, y = map(int, input().split())

date_obj = datetime.date(y, m, d)

print(date_obj.strftime("%A").upper())
