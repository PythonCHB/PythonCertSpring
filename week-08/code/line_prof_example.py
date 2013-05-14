#!/usr/bin/env python

"""
timing example -- set up for running with line_profiler

$ pip install line_profiler

$ kernprof.py -l -v line_prof_example.py 

"""

@profile
def primes_stupid(N):
    """
    a really simple way to compute the first N prime numbers
    """
    primes = [2]
    i = 3
    while len(primes) < N:
        for j in range(2, i): 
            if not i % j: # it's not prime
                break
        else:
            primes.append(i)
        i += 1

    return primes

primes_stupid(100)



