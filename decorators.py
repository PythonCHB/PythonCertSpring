#! /usr/bin/env python
#
# This script gives some examples of decorators

import time

def time_it( function, *args ) :
    def wrapped_funct( *args ) :
        start_time = time.time()
        function ( args )
        print "function:", function.__name__, "took", time.time() - start_time, \
              "to execute"
    return wrapped_funct

@time_it
def a_very_complicated_function( *args ) :
    """This is a very complicated function that takes a long time to execute"""
    print "Starting execution"
    time.sleep(4)
    print "Ending execution"


class Jeffs_class ( object ) :
    def class_method (self, a ) :
        """This is an example of a class method"""
        print "In class_method: a=",a

    @staticmethod  # This is a built in function, see
                # http://docs.python.org/2/library/functions.html#staticmethod
    def static_method ( a ) :
        """This is an example of a class method that has been converted to a
static method"""
        print "In static_method: a=",a

if __name__ == "__main__" :
    a_very_complicated_function( 1, 2, 3 )
    j = Jeffs_class()
    j.class_method( 6 )

    Jeffs_class.static_method ( 14 )

    try :
        Jeffs_class.class_method( 22.3 )
    except TypeError, e :
        print "TypeError exception was raised",e
    Jeffs_class.class_method(j, 12.5 )   # DO NOT DO THIS - IT IS NOT "pythonic"

    j.static_method( (2+3j) )
    Jeffs_class().static_method("Dammed Vikings")

    

    

