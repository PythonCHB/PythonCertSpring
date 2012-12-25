#! /usr/bin/env python
#
# rotate_csv.py
# This python program takes a csv file and rotates in either clockwise (+) or
# counter clockwise (-)  - a transpose.
# For example a file with 3 rows and 30 columns would become a file of 3 columns
# and thirty rows.
# This is from StackOverflow,
# http://stackoverflow.com/questions/4869189/how-to-pivot-data-in-a-csv-file
import csv
import Cdf
import matplotlib.pyplot as pyplot

c = csv.reader(open("2011-income-distribution.csv", "rb"))
lv = []   # list of (value,frequency) pairs
header = c.next()       # Bypass the header
for r in c :
    lv.append((float(r[0]),float(r[-1])))     # append a tuple of frequency, value to the list
cdf = Cdf.MakeCdfFromItems(lv)
xs, ps = cdf.Render()
xmax = max(xs)
pyplot.plot(xs, ps, linewidth=3)
pyplot.axis([0.9, xmax*1.1, 0.0, 1.0])
pyplot.title('CDF')
pyplot.xlabel('income')
pyplot.ylabel('probability, CDF(x)')
pyplot.show()


    
