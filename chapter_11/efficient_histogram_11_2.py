#! /usr/bin/env python
#
#
# Dictionaries have a method called get that takes a key and a default value.
# If the key appears in the dictionary, get returns the corresponding value;
# otherwise it returns the default value. For example:
# >>> h = histogram('a')
# >>> print h
# {'a': 1}
# >>> h.get('a', 0)
# 1
# >>> h.get('b', 0)
# 0


def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0)+1
    return d

if __name__ == "__main__" :
    while True :
        s = raw_input("Enter a string ")
        h = histogram(s)
        print h
