#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use the datetime module to write a program that gets the current date and prints
# the day of the week.
# http://docs.python.org/2/library/datetime.html#datetime-date
#

import datetime

DOW_trans_table = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

def get_day_of_week ( t ) :
    if not isinstance( t, datetime.date ) :
        raise ValueError ("t is not a date type in get_day_of_week")
    dow = t.weekday()
    return DOW_trans_table[ dow ]




if __name__ == "__main__" :
    today = datetime.date.today()
    current_week_day = get_day_of_week ( today )
    print current_week_day
# Write a program that takes a birthday as input and prints the user’s age and
# the number of days, hours, minutes and seconds until their next birthday.
    bday_str = raw_input("Enter birthday as dd/mm/yyyy ")
    day, month, year = bday_str.split("/")
    bday = datetime.date(int(year), int(month), int(day) )
    duration = bday - today
    print duration
    

