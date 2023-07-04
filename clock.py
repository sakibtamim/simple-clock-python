import datetime

date = datetime.datetime.now()
print("It's ", date)
print(date.year)
print(date.month)
print(date.strftime("%A"))
print(date.day)
print(date.ctime())
print(date.hour)