#! /usr/bin/env python
#
# Exercise 16-6   Write a function called mul_time that takes a Time object and
# a number and returns a new Time object that contains the product of the
# original Time and the number.
# Then use mul_time to write a function that takes a Time object that
# represents the finishing time in a race, and a number that represents the
# distance, and returns a Time object that represents the average pace
# (time per mile).
#
# By number, I assume that Downey means a floating number, because
# V=T/D = T * 1/D

import increment_using_int_exercise_16_5 as TI
import numbers

def mul_time( time, number ) :
    """Multiply Time time by number"""
    assert isinstance(time, TI.Time)
    assert isinstance(number, numbers.Number)

    seconds = TI.time2int(time)
    seconds *= number
    t = TI.int2time(seconds)
    return t

def str2time( s ) :
    """This function converts a string in the form HH:MM:SS into a Time type"""

    time_list = s.split(":")
    hours = int(time_list[0])
    minutes = int(time_list[1])
    seconds = int(time_list[2])
    if hours < 0 or minutes < 0 or seconds < 0 or \
        minutes > 59 or seconds > 59 :
        raise ValueError

    time = TI.Time()
    time.hours = hours
    time.minutes = minutes
    time.seconds = seconds
    return time
    
        
    

if __name__ == "__main__" :
    while True :
        s = raw_input("Enter duration of the race in format HH:MM:SS ")
        try :
            t = str2time(s)
        except ValueError, e :
            print "You entered an invalid value for the time\nUse HH:MM:NN.  The\
 numbers must be greater or equal to 0 and minutes and seconds must be less than\
 60"
        else :
            break   # we have a valid value, so escape from the loop

    while True :
        try :
            d = float(raw_input("Enter the distance of the race "))
            if d <= 0.0 :
                raise ValueError
        except ValueError, e:
            print "The distance must be a valid float point number > 0.0 "
        else :
            break   # we have a valid value, so escape from the loop

    v = mul_time ( t, 1.0/d )
    print "The average pace is",
    TI.print_time(v)
    
            

