#! /usr/bin/python
#
# This program finds palidromic words
# http://greenteapress.com/thinkpython/html/thinkpython007.html

DEBUG = False      # True if you wish to debug the string functions

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]


def is_palindrome ( word ) :
    """A word is *not* a palindrome if the last character and the first character
are different.  A word *is* a palindrom if the first and last characters are the
same and the middle letters are a palindrome"""
    if len(word) <= 1 :
        return True
    elif first(word) != last(word) :
        return False
    else :
        return is_palindrome ( middle ( word ) )
        
if DEBUG :
    while True :
        word = raw_input("Enter a word >> ")
        print "First letter is ", first(word)
        print "last letter is ", last(word)
        print "middle letter is ", middle(word)
        
def test ( word ) :
    print word, "is", "not" if not is_palindrome( word) else "", "a palindrome"


test("noon")
test("redivider")
test("Jeffrey")
