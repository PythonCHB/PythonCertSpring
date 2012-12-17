#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Exercise 16-7.
# Write a class definition for a Date object that has attributes day, month and
# year. Write a function called increment_date that takes a Date object, date
# and an integer, n, and returns a new Date object that represents the day n
# days after date. Hint: “Thirty days hath September...” Challenge: does your
# function deal with leap years correctly? See wikipedia.org/wiki/Leap_year.

month_days_table = {0:0,    # Jan starts at 0
                    1:31,   # February - January has 31 days
                    2:59,   # March - February has 28 days except in leap years
                    3:90,   # April - March has 31 days
                    4:120,  # May - April has 30 days
                    5:151,  # June - May has 31 days
                    6:181,  # July - June has 30 days
                    7:212,  # August - July has 31 days
                    8:243,  # September - August has 31 days
                    9:273,  # October - September has 30 days
                    10:304, # November - October has 31 days
                    11:334, # December - November has 30 days
                    12:365} # January - December has 31 days
                    
                    
class Date( object ) :
    """This class has attributes day, month and # year."""
    pass

def create_date ( day, month, year ) :
    """This function creates a Date object with day month and year"""

    if not 0 <= month < 12 :
        raise ValueError,"Month is out of range"
    if not 0 < day <= 31 :  # This is a crude test, a better test would be to be
                            # aware of the number of days in a month
        raise ValueError,"Day is out of range"
    if 0 >= year :    # I am arbitrarily starting at the beginning of the
                            # Gregorian calendar
        raise ValueError,"Year is less than 0"
    date = Date()
    date.day = day
    date.month = month
    date.year = year
    return date

def is_leap_year ( year, gregorian=True ) :
    """Returns True if year is a leap year"""
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    if gregorian :
        if year % 400 == 0 :
            return True
        elif year % 100 == 0 :
            return False
        elif year % 4 == 0 :
            return True
        else :
            return False
    else :
        raise NotImplemented

def date_to_int ( date, gregorian=True ) :
    """This function converts a date of class Date to an integer, which is the
Julian Day"""
# See http://en.wikipedia.org/wiki/Julian_day for the "right" way to do this
# calculation
# See http://www.tondering.dk/claus/cal/julperiod.php which has a more detailed
# algorithm and which has open source C code which implements the algorithm
    assert isinstance(date, Date)
# Integer division in python is floor division which is what the description calls for
    a = (14-date.month)/12
    y = date.year + 4800 - a
    m = date.month + 12*a - 3
    if gregorian :
        jd = date.day + (153*m + 2)/5 + 365*y + y/4 - y/100 + y/400 - 34045
    else :
        jd = date.day + (153*m + 2 )/5 + 365 * y + y/4 - 32083
    return jd

def int_to_date ( jd, gregorian=True ) :
    """This function convertrs a Julian Day number, jd, into a month, day, year
for the Gregorian or Julian calendars"""
    if gregorian :
        a = jd + 32044
        b = (4 * a + 3) / 146097
        c = a - ( 146097 * b ) / 4         # parenthesis are for numerical stability
    else :
        a = None   # not in the algorithm description, but perhaps useful for catching errors
        b = 0
        c = jd + 32082
    d = (4 * c + 3 )/1461
    e = c - ( 1461 * d ) / 4        # parenthesis are for numerical stability
    m = (5 * e + 2 ) / 153
    day = e - (( 153 * m + 2 ) / 5 ) + 1
    month = m + 3 - 12 * (m/10)     # Parenthesis as called for by the algorithm
    year = 100 * b + d - 4800 + (m/10)
    date = create_date ( day, month, year )
    return date

def dates_equal ( date, check ) :
    """This function returns True if date and check are equal"""
    return check.day == date.day and check.month == date.month and \
               check.year == date.year


if __name__ == "__main__" :
    date = create_date(month=10, year=1582, day=15 )  # October 15th, 1582, the
                                                    # beginning of the Gregorian
                                                    # Calendar
    jd = date_to_int ( date, True )
# From the Julian Date Converter at the USNO, http://aa.usno.navy.mil/data/docs/JulianDate.php    
    assert jd == 2299525,"date to int calculation is wrong for 1582"
    check_date = int_to_date ( jd, True )
    assert dates_equal ( date, check_date)

    date = create_date(month=0, day=1, year=2000)  # January 1st 2000
    jd = date_to_int ( date, True )
    assert jd == 2451545,"date to int calculation is wrong for 2000"
    check_date = int_to_date ( jd, True )
    assert dates_equal ( date, check_date),"The check for Jan 1 2000 is wrong"

    date = create_date(day=15, month=9, year=1)
    jd = date_to_int ( date, False )
    assert jd == 1721710,"date to int calculation is wrong for AD 1 in the Julian calendar"
    check_date = int_to_date ( jd, True )
    assert dates_equal ( date, check_date),"The check for 15 October 1 AD is wrong"
    
