# Name: 

"""
Quiz  Week 6

On this sheet, write down the output from each print statement in this module.

If different orderings of items in the printed output are possible,
just write down one of the correct orders.

If executing the print statement would raise an exception,
just write ERROR 
"""

gertrude = 'a rose is a rose is a rose'

def freq(line):
    histo = {}
    for word in line.split():
        if word not in histo:
            histo[word] = 1
        else:
            histo[word] += 1
    return histo

histo = freq(gertrude)

print histo

print histo['is'], histo['a']

for word in histo:
    print word

print histo.keys()

print histo.values()

print histo['violet']

