import datetime, sys

from prototype import App

a=App()
date = a.first_line.split()[-1:][0]
print(date)
utc=datetime.datetime.strptime(date, "%Y-%m-%d")

time_in_second=(utc-datetime.datetime(1970, 1, 1)).total_seconds()
print(time_in_second)