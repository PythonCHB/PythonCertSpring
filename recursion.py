"""
Demonstrate recursion with print statements
Similar to factorial in Downey, PySD sect. 6.9, p. 70
"""

def rsum_p(prefix, n):
    print '%sEntering rsum with n = %s' % (prefix, n)
    if n == 0:
        sum = n  # base case
    else:
        sum = n + rsum_p(prefix + ' ', n-1) # make progress toward base
    print '%sn = %s, return sum = %s' % (prefix, n, sum)
    return sum


print rsum_p('', 4)
