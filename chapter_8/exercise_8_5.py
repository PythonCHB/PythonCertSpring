#! /usr/bin/python
#
# From: http://greenteapress.com/thinkpython/html/thinkpython009.html
# Encapsulate this code in a function named count, and generalize it so that it accepts the
# string and the letter as arguments.

def count ( word, sought ) :
    """This function counts the number of occurances of a letter in a word"""

    c = 0
    for letter in word:
        if letter == sought :
            c = c + 1
    return c

if __name__ == "__main__" :
    def test_count ( word, sought, expected ) :
        """This function tests the count function"""
        r = count ( word, sought )
        if r == expected :
            print "count %s %s returned %d as expected" % ( word, sought, r )
        else :
            print "Count %s %s FAILED.  Returned %d expected %d" % ( word, sought, r, expected )

    test_count ("apple", "a", 1)
    test_count ("apple", "p", 2 )
    test_count ("apple", "e", 1 )
    test_count ("Mississippi", "s", 4 )
    test_count ("Wisconsin", "e", 0 )

