#! /usr/bin/env python
#
#
# Write a function called most_frequent that takes a string and prints the
# letters in decreasing order of frequency. Find text samples from several
# different languages and see how letter frequency varies between languages.
# Compare your results with the tables at
# http://en.wikipedia.org/wiki/Letter_frequencies.

def make_histogram( text ) :
    """This function returns a dictionary with single letters as keys and a
count of the number of occurances in text as values"""
    d={}
    for c in text :
        if c != "\r" and c != '\n' :
            d[c] = d.get(c, 0) + 1
    return d

def sort_dict( d ) :
    """This functions returns a list of tuples which is sorted by count"""
    t = []
    for c in d.keys() :
        t.append ( (d[c], c ) )
    t.sort()
    r = []
    for c in t :
        r.append( (c[1],c[0] ) )
    return r


text = file("words.txt","r").read() # Read the entire file words.txt as a
                                    # single string
d = make_histogram( text )
sorted_list = sort_dict( d )
for c in sorted_list :
    print c[0],":",c[1]
