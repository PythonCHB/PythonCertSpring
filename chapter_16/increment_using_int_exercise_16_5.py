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

Exercise 3
increment, which adds a given number of seconds to a Time object, can be written
naturally as a modifier.  Write a correct version of increment that doesn’t
contain any loops.

Exercise 5   Rewrite increment using time_to_int and int_to_time.
"""

TEST=1

class Time :
    """A class that holds a time.  Attributes are hours, minutes, and seconds"""

    pass

def print_time( t ) :
    """A function to print out a time"""
    assert isinstance(t, Time)
    print "%d:%02d:%02d" % (t.hours, t.minutes, t.seconds )

def time2int( t ) :
    """A function to convert a time to seconds"""
    assert isinstance(t, Time), "Argument to seconds is not an instance of Time"
    return ((t.hours * 60) + t.minutes) * 60 + t.seconds
    
def is_after(t1, t2) :
    assert isinstance(t1, Time)
    assert isinstance(t2, Time)
    s1 = time2int(t1)
    s2 = time2int(t2)
    return s2 > s1

def int2time( seconds ):
    """Convert an integer number of seconds to a Time"""
    time = Time()
    time.hours, secs = divmod(seconds,3600)
    time.minutes, time.seconds = divmod(secs, 60)
    print "In int2time, seconds is %d, time is" % seconds,
    print_time(time)
    return time
    
    
def increment ( time, secs ):
    """A function to increment time by seconds"""
    assert isinstance(time,Time),"first argument to increment is not an instance of Time"
    s1=time2int(time)
    s1 += secs
    time = int2time(s1)
    print "in increment", print_time(time)

    

def main() :
    if TEST :
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

        print  "Should be 00:02:04",
        print_time( int2time( 124 ))

        print "Should be 02:03:04",
        print_time( int2time( 7200+180+4 ))
        
        print "Should raise AssertionError"
        try :
            time2int(4)
        except AssertionError, (e):
            print "time2int threw an AssertionError %s as it should have" % e
        else :
            print "time2int DID NOT throw an AsserionError but it should have"

        print "Should be %d is %d" % (34*3600+12*60+11, time2int(t1) )
        
        print "Should be 34:12:15",
        increment(t1, 4)
        print_time(t1)

        print "Should be 35:14:17"
        increment(t1,3600+120+2)
        print_time(t1)
        
        

if __name__ == "__main__" :
    main()
    
