#! /usr/bin/python
#
# Use the algorithm found by The mathematician Srinivasa Ramanujan which is an
# infinite series that can be used to generate a numerical approximation of pi

import math


k = 0
series_sum = 0.0
while True :
    k4_factorial = math.factorial( 4 * k )
    numerator = k4_factorial * ( 1103 + 26390 * k )
    denominator = math.factorial(k)**4 * 396 ** (4 * k )
    term = float( numerator ) / ( denominator )
    if abs(term) < 1.0E-15 :
        break
    series_sum += term
    k += 1

pi = 9801.0 / ( 2 * math.sqrt(2.0) * series_sum )

print "It took ", k, "iterations.  pi = ", pi, "The reference value is ", math.pi, "The error is ", pi - math.pi
