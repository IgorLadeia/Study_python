from datetime import date,datetime

igor = date(1997, 1, 31).isoformat()
igor1 = date(1997, 1, 31).strftime("%d/%m/%y")
igor2 = date(1997, 1, 31).strftime("%A %d. %B %Y")

print(igor1 , igor2)


print(datetime.fromisoformat('2011-11-04'))
#print(datetime.fromisoformat('20111104'))--- python 3.11
print(datetime.fromisoformat('2011-11-04T00:05:23'))
print(datetime.fromisoformat('2011-11-04T00:05:23'))
#print(datetime.fromisoformat('20111104T000523')) --- python 3.11
#print(datetime.fromisoformat('2011-W01-2T00:05:23.283')) --- python 3.11
print(datetime.fromisoformat('2011-11-04 00:05:23.283'))
print(datetime.fromisoformat('2011-11-04 00:05:23.283+00:00'))
print(datetime.fromisoformat('2011-11-04T00:05:23+04:00'))

