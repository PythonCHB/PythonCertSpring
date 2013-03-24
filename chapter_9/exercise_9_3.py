#! /usr/bin/python
# -*- coding: utf-8 -*-
# Exercise 9.3  
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn’t use any of the forbidden
# letters.  Modify your program to prompt the user to enter a string of
# forbidden letters and then print the number of words that don’t contain any
# of them. Can you find a combination of 5 forbidden letters that excludes the
# smallest number of words?

TEST = False

def no_forbidden ( word, forbidden_set ) :
    """This function tests the word word to see if it contains any of the
characters in the forbidden set, which is also a string"""
    for c in word :
        if c in forbidden_set :
            return False
    return True


if TEST :
    def test_no_forbidden ( word, forbidden_set, expected ) :
        r = no_forbidden ( word, forbidden_set )
        if r == expected :
            print "word %s with forbidden set %s works" % ( word, forbidden_set )
        else :
            print "word %s with forbidden set %s FAILS returned %s expected %s" % ( word,
                forbidden_set, str(r), str(expected ) )

    test_no_forbidden ( "apple", "wksvQ", True )
    test_no_forbidden ( "apple", "wksva", False )
    test_no_forbidden ( "apple", "eksvQ", False )

else :
    forbidden_set = raw_input ("Enter a forbidden set of characters ")
    not_fb_ctr = 0
    lc = 0
    fin = open("words.txt", "r")
    for line in fin :
        word = line.strip()
        lc = lc + 1
        if no_forbidden ( word, forbidden_set ) :
            not_fb_ctr = not_fb_ctr + 1
    print "Out of %d words, %d did not contain any forbidden characters %s" % ( lc, not_fb_ctr, forbidden_set )

# if you use the 5 character forbidden set "aeiou" that will exclude all but 107 words

