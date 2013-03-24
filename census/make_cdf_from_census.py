#! /usr/bin/env python
#
import csv
import Cdf
import matplotlib.pyplot as pyplot

c = csv.reader(open("2011-income-distribution.csv", "rb"))
lv = []   # list of (value,frequency) pairs
header = c.next()       # skip the header
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


    
