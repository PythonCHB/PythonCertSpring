#! /usr/bin/env python
#
# Exercise 11-7.  Exponentiation of large integers is the basis of common
# algorithms for public-key encryption. Read the Wikipedia page on the RSA
# algorithm3 and write functions to encode and decode messages.
# http://en.wikipedia.org/wiki/RSA_(algorithm)

import random

DEBUG_IS_PRIME=True

def is_prime ( n ) :
    """Returns True if n is a prime number"""
    for x in range(2, n):
        if n % x == 0:
            return False
    else :
# loop fell through without finding a factor
        return True

if DEBUG_IS_PRIME :
    assert is_prime(7)
    assert not is_prime(6)
    assert not is_prime(323)   # 17 x 19
    assert is_prime(99981599)   # From http://arachnoid.com/prime_numbers/index.html
    print "passed all tests"

def pick_random_prime_number () :
   """This function returns a random integer which is prime"""
   while True :
       n = random.randint(1,1000000)   # For real cryptographic applications, should be
                                       # nuch larger
       if is_prime(n) :
           return n



def encode_decode ( message, public_key, private_key, modulus ) :
    p = pick_random_prime_number()
    q = pick_random_prime_number()
    
