# Name: 

"""
Quiz  Week 3

On this sheet, write down the output produced by executing this module
"""

def fsum(n):
    sum = 0
    for i in range(n):
        sum = sum + i
        print i, sum
    return sum

def rsum(n):
    if n == 0:
        sum = n
    else:
        sum = n + rsum(n-1)
    print n, sum
    return sum

print fsum(5)
print
print rsum(4)
    
    
