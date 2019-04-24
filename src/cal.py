"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime


# Prompt user for current year
date = input("Enter month, or month and year: ")
list_date = date.split()


def get_date(month, year):
    c = calendar.TextCalendar(6)
    year = datetime.now().year
    if len(date) == 0:
        month = datetime.now().month
        c.prmonth(year, month)
        return c
    elif len(date) == 1:
        c.prmonth(year, int(date[0]))
        return c
    elif len(date) == 2:
        c.prmonth(int(date[1]), int(date[0]))
        return c
    else:
        print('invalid input, please enter [month] [year]')


print(get_date(list_date))
