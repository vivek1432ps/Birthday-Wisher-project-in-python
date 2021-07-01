import datetime as dt


now = dt.datetime.now()
year = now.year
moth = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1999, month=4, day=29, hour=6)
print(date_of_birth)