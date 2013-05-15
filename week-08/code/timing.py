#!/usr/bin/env python

"""
timing example
"""

# @profile
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

if __name__ == "__main__":
    import timeit


    print "running the timer on primes_stupid:"
    run_time = timeit.timeit("primes_stupid(100)",
                             setup="from __main__ import primes_stupid",
                             number=500) # default: 1000000
    print "it took: %f seconds"%run_time
    primes_stupid(100)



