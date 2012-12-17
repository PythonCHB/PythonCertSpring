#! /usr/bin/env python
#
# Exercise 17-1   Write a __cmp__ method for Time objects. Hint: you can use
# tuple comparison, but you also might consider using integer subtraction.


class Time :
    """A class that holds a time.  Attributes are hours, minutes, and seconds"""

    def time_to_int( self ) :
# Look up Horner's rule for an efficient way to calculate polynomials        
        return (((self.hours*60) + self.minutes) * 60 ) + self.seconds

    def increment (self, secs ):
        """A function to increment time by seconds"""
        s1 = self.time_to_int()
        s1 += secs
        time = int2time(s1)
        return time

    def __cmp__ (self, other ):
        """The built-in function cmp has the same interface as the method __cmp__:
it takes two values and returns a positive number if the first is larger, a
negative number if the second is larger, and 0 if they are equal."""
        si = self.time_to_int()
        oi = other.time_to_int()
        return si - oi

    @staticmethod
    def int_to_time( seconds ):
        """This function converts the integer seconds to a time"""
        time = Time()
        time.hours, secs = divmod(seconds,3600)
        time.minutes, time.seconds = divmod(secs, 60)
        return time

    
    def __str__( self ) :
        """A function to print out a time"""
        return "%d:%02d:%02d" % (self.hours, self.minutes, self.seconds )
        

if __name__ == "__main__" :
    while True :
        s = int( raw_input("Enter the first number of seconds ") )
        o = int( raw_input("Enter the second number of seconds ") )
        st = Time.int_to_time(s)
        ot = Time.int_to_time(o)
        r= cmp(st, ot)
        if r > 0 :
            print str(st)," > ", str(ot)
        elif r == 0 :
            print str(st)," = ", str(ot)
        else :
            print str(st)," < ", str(ot)


