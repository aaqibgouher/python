import datetime

# get current datetime
# here now will return a date obj, which u can directly print also
# and d has lots of method
d = datetime.datetime.now()
print(d.year)
print(d.strftime("%d %b, %Y @ %I:%M %p")) # 23 May, 2020 @ 4:05 PM

# with custom date create a date obj
d = datetime.datetime(2020, 5, 2)
print(d)