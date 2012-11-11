#! /usr/bin/python
#
# Exercise 8.10
# From http://greenteapress.com/thinkpython/html/thinkpython009.html
# Write a one-line function that returns True if the input string is a palindrome
# False if not a palindrome

def is_palindrome(s) :
    return s==s[::-1]

if __name__ == "__main__" :
    def test_is_palindrome(s, expected ) :
        if is_palindrome(s) == expected :
            print "Correct for %s" % s
        else :
            print "FAILS for %s" % s

    test_is_palindrome ( "alula", True )
    test_is_palindrome ( "Jeff", False )
    test_is_palindrome ( "kinnikinnik", True )

    # Go to http://www.rinkworks.com/words/palindromes.shtml which has palindromic
    # phrases.  Does this one liner work for phrases?  How would you modify the 
    # function is_palindrome to work on phrases as well as words?
    test_is_palindrome ("I did, did I", True )
