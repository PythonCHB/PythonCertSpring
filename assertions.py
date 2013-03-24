"""
Precondition, postcondition, invariant

A while-loop can be derived by filling in this template
with blocks S and T and condition P
that establish invariant I and postcondition I and not P

    S
    # pre: I
    while (P):
        # I
        T
    # post: I and not P
"""

def quotient(n, d):
    """
    Divide n by d, integer division by repeated subtraction
    n: dividend, d: divisor, q: quotient, r: remainder
    The definition of integer division is: n == q*d + r and r < d
    """
    assert n >= 0 and d > 0        # function precondition
    r = n    
    q = 0
    # assert n == q*d + r            # loop precondition 
    while (r >= d):
        # assert n == q*d + r        # loop invariant
        r = r - d
        q = q + 1
    # assert n == q*d + r and r < d  # postcondition
    return q

print '9/3 %s' % quotient(9,3)
print '8/3 %s' % quotient(8,3)
print '3/3 %s' % quotient(3,3)
print '2/3 %s' % quotient(2,3)

# what happens if preconditions are violated?
