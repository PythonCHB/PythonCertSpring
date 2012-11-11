#! /usr/bin/python
#
# Exercise 8.7
# From http://greenteapress.com/thinkpython/html/thinkpython009.html
# The function in the book as two errors in it.

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    
    i = 0
    j = len(word2)-1    # First error: the index of the last character in a string
                        # is the length - 1

    while j >= 0:       # Second error: the index of the first character in a
                        # string is 0
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1

    return True

if __name__ == "__main__" :
    def test_is_reverse ( word_1, word_2, expected ) :
        r = is_reverse ( word_1, word_2 )
        if r == expected :
    # We have to convert r to a string because it is a boolean
            print "%s and %s are the expected value %s" % ( word_1, word_2, str(r) )
        else :
            print "%s and %s FAIL! Expected value is %s actual value is %s" % (
                word_1, word_2, str(expected), str(r) )


    test_is_reverse( "pots", "stop", True )
    test_is_reverse( "Pots", "stop", False )   
    test_is_reverse( "pots", "Stop", False )    # The first fixed version would not return the correct result for this test
    test_is_reverse( "poTs", "stop", False )
    test_is_reverse( "pots", "Wisconsin", False )

