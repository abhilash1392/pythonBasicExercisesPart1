"""12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module."""
import calendar

y=int(input('Enter the year: '))
m=int(input('Enter the month: '))

print('The calendar for this month and year is: ')
print(calendar.month(y,m))

