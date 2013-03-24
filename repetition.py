"""
Demonstrate for, while, and recursion on the same problem
"""

def fact_for(n):
    fact = 1
    for i in range(n):
        fact *= i+1   # same as fact = fact*(i+1)
    return fact

def fact_while(n):
    fact = 1
    while n > 0:
        fact *= n     # same as fact = fact*n
        n -= 1        # same as n = n - 1, must make progress 
    return fact

def fact_recurse(n):
    if n == 0:
        return 1                    # base case
    else:
        return n*fact_recurse(n-1)  # recurse on smaller argument

print 'fact_for(3)     %s' % fact_for(3)
print 'fact_while(3)   %s' % fact_while(3)
print 'fact_recurse(3) %s' % fact_recurse(3)

# show typical errors: no progress in while, no smaller arg in recurse
# show debugger

