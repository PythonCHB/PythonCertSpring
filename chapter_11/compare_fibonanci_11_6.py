#! /usr/bin/env python
#
#
# Exercise 6   Run this version of fibonacci and the original with a range of
# parameters and compare their run times.
import time

def original_fibonacci (n):
    if n == 0:
        return 0
    elif  n == 1:
        return 1
    else:
        return original_fibonacci(n-1) + original_fibonacci(n-2)

known = {0:0, 1:1}
def memoized_fibonacci ( n ):
    if n in known:
        return known[n]

    res = memoized_fibonacci(n-1) + memoized_fibonacci(n-2)
    known[n] = res
    return res


def time_function ( function, iterations, argument ) :
    """This function times how long it takes to execute function function, when
given *arguments arguments, and looping over iterations iterations to build up
the time for a very fast function"""
    start_time = time.time()
    for i in range(iterations) :
# Execute the function, throw away the result.  We're only interested in how
# long it takes to run
        _ = function( argument )
    diff = time.time() - start_time
    print function.__name__, " took %f seconds" % diff

if __name__ == "__main__" :
    n = int ( raw_input("Enter the argument of the fibonacci function ") )
    count = int ( raw_input ("Enter the number of iterations to test over " ) )
    time_function ( original_fibonacci, count, n )
    time_function ( memoized_fibonacci, count, n )
