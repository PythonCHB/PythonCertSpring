#! /usr/bin/python
# -*- coding: utf-8 -*-
#
#
"""
Exercise 1   Write a function called print_time that takes a Time object and prints
it in the form hour:minute:second. Hint: the format sequence '%.2d' prints an
integer using at least two digits, including a leading zero if necessary.

Exercise 2  
Write a boolean function called is_after that takes two Time objects, t1 and t2,
and returns True if t1 follows t2 chronologically and False otherwise.
Challenge: don’t use an if statement.
"""

class Time :
    """A class that holds a time.  Attributes are hours, minutes, and seconds"""

    pass

def print_time( t ) :
    """A function to print out a time"""
    assert isinstance(t, Time)
    print "%d:%02d:%02d" % (t.hours, t.minutes, t.seconds )

def seconds( t ) :
    """A function to convert a time to seconds"""
    assert isinstance(t, Time)
    return ((t.hours * 60) + t.minutes) * 60 + t.seconds
    
def is_after(t1, t2) :
    assert isinstance(t1, Time)
    assert isinstance(t2, Time)
    s1 = seconds(t1)
    s2 = seconds(t2)
    return s2 > s1

def main() :
    t1 = Time()
    t1.hours = 34
    t1.minutes = 12
    t1.seconds = 11
    print_time(t1)

    t2 = Time()
    t2.hours = 34
    t2.minutes = 12
    t2.seconds = 14
    print_time(t2)
    print is_after(t1, t2), "should be True"

    t2.seconds = 10
    print_time(t2)
    print is_after(t1, t2), "should be False"

    t2.hours = 35
    print_time(t2)
    print is_after(t1, t2), "should be True"
    
    t2.hours = 34
    t2.minutes = 13
    print_time(t2)
    print is_after(t1, t2), "should be True"

    t2.minutes = 10
    print_time(t2)
    print is_after(t1, t2), "should be False"


if __name__ == "__main__" :
    main()
    
