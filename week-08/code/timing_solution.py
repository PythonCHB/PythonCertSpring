#!/usr/bin/env python

"""
timing example, with a couple faster versions....
"""

def primes_stupid(N):
    """
    a really simple way to compute the first N prime numbers
    """
    primes = [2]
    i = 3
    while len(primes) < N:
        for j in range(2, i): # the "/2" is an optimization -- no point in checking even numbers
            if not i % j: # it's not prime
                break
        else:
            primes.append(i)
        i += 1

    return primes

def primes_stupid_2(N):
    """
    a slightly less simple way to compute the first N prime numbers
    """
    primes = [2]
    i = 3
    while len(primes) < N:
        for j in range(2, i): # the "/2" is an optimization -- no point in checking even numbers
            if not i % j: # it's not prime
                break
        else:
            primes.append(i)
        i += 2 # no reason to check the even numbers

    return primes

def primes_stupid_3(N):
    """
    a slightly less simple way to compute the first N prime numbers
    """
    primes = [2]
    i = 3
    while len(primes) < N:
        for j in range(2, i/2): # no point in checking up to more than half the value
            if not i % j: # it's not prime
                break
        else:
            primes.append(i)
        i += 2 # no reason to check the even numbers

    return primes



def primes_stupid_4(N):
    """
    yet antoher improvement
    """
    primes = [2]
    i = 3
    while len(primes) < N:
        for j in primes: # only have to check if divisible by primes less than the current value
            if not i % j: # it's not prime
                break
        else:
            primes.append(i)
        i += 2 # no reason to check the even numbers

    return primes


if __name__ == "__main__":
    import timeit

    print "running the timer:"
    run_time = timeit.timeit("primes_stupid(100)",
                             setup="from __main__ import primes_stupid",
                             number=500) # default: 1000000
    print "it took: %f seconds"%run_time

    print "running the timer on primes_stupid_2:"
    run_time = timeit.timeit("primes_stupid_2(100)",
                             setup="from __main__ import primes_stupid_2",
                             number=500) # default: 1000000
    print "it took: %f seconds"%run_time

    print "running the timer on primes_stupid_3:"
    run_time = timeit.timeit("primes_stupid_3(100)",
                             setup="from __main__ import primes_stupid_3",
                             number=500) # default: 1000000
    print "it took: %f seconds"%run_time

    print "running the timer on primes_stupid_4:"
    run_time = timeit.timeit("primes_stupid_4(100)",
                             setup="from __main__ import primes_stupid_4",
                             number=500) # default: 1000000
    print "it took: %f seconds"%run_time

