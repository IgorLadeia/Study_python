from datetime import datetime
from datetime import date

"""
datetime 
"""
print("datetime ")
print(datetime.now())
print(datetime.today())
print(datetime.time(datetime.now()))
print(datetime.date(datetime.now()))
print(datetime.ctime(datetime.now()))

x = datetime.now()
print(x.day)
print(x.month)
print(x.year)
print(x.hour)
print(x.minute)
print(x.second)

"""
date
"""
print()
print()
print("date")

y = date(2002, 12, 31)
y = y.replace(day=26)
print(y)
week_day = y.weekday()
print("where Monday is 0 and Sunday is 6")
week_day2 = y.isoweekday()
print("where Monday is 1 and Sunday is 7")
print(week_day , week_day2)

calen = y.isocalendar()
print("devolve uma tupla com o numero da semana  ano e numero do dia")
for i in calen:
    print(i)

d1 = date(2002, 12, 4).isoformat()
d2 = date(2002, 12, 4).ctime()

print(d1 , " " , d2)


