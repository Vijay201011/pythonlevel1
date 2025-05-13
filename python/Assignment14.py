#1. Write a Python script to display the various Date Time formats -
'''a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week'''

#2. Write a Python program to determine whether a given year is a leap year.
#3.  Write a Python program to subtract five days from the current date.
#4.  Write a Python program to select all the Sundays in a specified year.
import datetime
b=datetime.datetime.now()
print(b)
print(b.strftime('y'))
print(b.strftime('b'))
print(b.strftime('U'))
print(b.strftime('w'))
print(b.strftime('U'))
print(b.strftime('d'))
print(b.strftime('A'))
print(b.strftime(''))
print(b.strftime(''))
print(b.strftime(''))



def is_leap_year(year):
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year = int(input("Enter a year: "))


if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")





f=datetime.datetime.now()
current_date = datetime.date.today()

new_date = current_date - datetime.timedelta(days=5)

print(f"Current date: {current_date}")
print(f"Date after subtracting 5 days: {new_date}")




