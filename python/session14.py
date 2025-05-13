#collections 
#collections is a library which has the functions which helps us to collect or count the data
#counter 
#counter is going to count how many times a particular word or data is repeated
import collections
list1=[1,5,2,4,6,6,5,3,4,2,3,1]
print(collections.Counter(list1))
#calendar 
#calendar library is used to display the calender of paticular months or the whole year
import calendar
a=calendar.calendar(2004)
print(a)
b=calendar.calendar(12,2010)
print(b)
#time library
import time
#it has a delay function or make us wait for some time
c=1
"""while c<=8:
    print(c)
    c=c+1
    time.sleep(11)"""
import datetime
g=datetime.datetime.now()
print(g)
#strft time helps us to extract the particular thing such as weekday, week number, month, year, etc using abbreviations
print(g.strftime('%a'))
print(g.strftime('%b'))
print(g.strftime('%B'))
print(g.strftime('%d'))
print(g.strftime('%M'))
print(g.strftime('%H'))
print(g.strftime('%S'))
print(g.strftime('%m'))
print(g.strftime('%w'))
print(g.strftime('%y'))

#----------------------------------------------Math libary-------------------------------------------------------------
#math library has math functions like factorial, square function and many more..................
import math
#min(), max(), pow(), sqrt(0, ceil(),
x=min(1, 1, 3)
print(x)
y=(max(1, 2, 3))
print(y)
print(math.pow(3, 2))
print(math.sqrt(64))
