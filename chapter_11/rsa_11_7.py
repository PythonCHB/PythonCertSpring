#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Exercise 11-7.  Exponentiation of large integers is the basis of
# common algorithms for public-key encryption. Read the Wikipedia page
# on the RSA algorithm3 and write functions to encode and decode
# messages. http://en.wikipedia.org/wiki/RSA

#
import random
import math

SIZE=2000 # pick a size of the prime numbers.  More means better security but slower
             # execution time
TEST=False

def find_prime_number( size=20000 ) :
    """This function returns an integer of roughly size """
    while True:
        trial_prime =random.randint(size, size*2)
        if is_prime(trial_prime) :
            break
    return trial_prime

def is_prime(trial_prime) :
    """returns True if trial_prime is prime"""
# Handle small integers specially
    if trial_prime in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] :
        return True
    if trial_prime % 3 == 0: return False
    if trial_prime % 2 == 0: return False
# a more efficient method is to test if n is divisible by 2 or 3, then
# to check through all the numbers of form 6k ± 1 <= sqrt(n). This is
# 3 times as fast as testing all m.  Conversion of floating point
# numbers to integers truncates (towards zero)
    i = 1
    limit = ( int(math.sqrt(float(trial_prime)) / 6 )+1 )
    while i <= limit :
        tf = 6*i - 1     # note -
#        print "testing factor ", tf
        if (trial_prime % tf) == 0 :
            print "Trial_prime %d is divisible by %d" % (trial_prime, tf)
            return False
        tf = 6*i + 1     # note +
#        print "testing factor ", tf
        if (trial_prime % tf) == 0 :
            print "Trial_prime %d is divisible by %d" % (trial_prime, tf)
            return False      
        i += 1
    return True

# This is from http://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def egcd(a, b):
    """Euclid's algorithm for determining the greatest common divisor"""
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b/a,b%a
        m,n = x-u*q,y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

# This is from http://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def generate_keys():
    "This function generates the keys for encryption and decryption"

# from http://http://en.wikipedia.org/wiki/RSA#A_worked_example
# Choose two prime numbers Make sure that these prime numbers are distinct (i.e. they are not both the same number).
    while True:
        if TEST:
            p = 61
            q = 63
        else :
            p = find_prime_number(SIZE)
            q = find_prime_number(SIZE)
        if q != p : break

# Compute n = pq
    n = p * q
    if TEST:
        print "n = ", n

# Compute the totients of product. For primes, the totient is maximal
# and equals the prime minus one. Therefore totient(pq) = (p-1)(q-1)
    totient = (p-1)*(q-1)
    if TEST:
        print "totient(%d%d)=%d" % (p, q, totient)
        
# Choose any number e > 1 that is coprime to the totient. Choosing a prime
# number for e leaves you with a single check: that e is not a divisor
# of the totient.
    while True :
        if TEST:
            e = 17
            assert totient % e ==0, "%d %% %d is 0, which menas %d is a factor of %d" % (
                totient, e, e, totient )
        else :
            e = find_prime_number(SIZE/10)
        if ( totient % e ) != 0 : break

# Compute d such that de = 1 mod totient  e.g., by computing the modular multiplicative
# inverse of e modulo totient:
    d = modinv(e, totient)

    print "The public key is (%d, %d)" % (n, e)
    print "The private key is (%d, %d)" % (n, d)
    return (n, e, d)

def main():
    if TEST:
        m = 65
    else :
        while True :
            m = int(raw_input("Enter a message to encrypt (an integer) "))
            if m <= SIZE :
                break
            print "Enter a smaller message to encrypt"
    (n, e, d ) = generate_keys()
    c = ( m ** e ) % n
    if TEST:
        assert c != 2790, "The ciphertext is %d and should be 2790" % c
    print "The ciphertext is %d" % c
    m_decoded = ( c ** d) % n
    print "The decoded message is %d" % m_decoded
    assert m == m_decoded, "Failed to decode the message properly.  Original message is %d, decoded message is %d" % (m, m_decoded)
    
            
    

if __name__ == "__main__" :
#    print "testing 17 for primality"
#    assert is_prime(17), "is_prime incorrectly found that 17 is composite"
#    print "testing 209 for primality"
#    assert not is_prime(209), "is_prime incorrectly found that 209 is prime (11x19)"
#    print "testing 54 for primality"
#    assert not is_prime(54), "is_prime incorrectly found that 54 is prime (6x9)"
    
#    print "see http://www.factmonster.com/math/numbers/prime.html"
#    for i in range(1, 10):
#        test = find_prime_number(size=1000)
#        print "Find_prime_number found %d which it thinks is prime" % test
    main()
    
            
