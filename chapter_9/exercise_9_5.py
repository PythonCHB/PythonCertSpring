#! /usr/bin/python
# -*- coding: utf-8 -*-
#
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once. How many words are there that use all the vowels aeiou? How about
# aeiouy?

TEST = False

def uses_all ( word, required ) :
    """uses all returns True if word uses all of the characters in string"""

    for c in required :
        if c not in word :
            return False       # A required letter isn't used
    return True

if TEST :
    def test_uses_all ( word, required, expected ) :
        r = uses_all ( word, required )
        if r == expected :
            print "The word %s and the required letters %s work" % ( word, required)
        else :
            print "The word %s and the required letters %s FAIL expected was %s returned was %s" % (
                word, required, str(r), str(expected) )

    test_uses_all ( "apple", "aple", True )
    test_uses_all ( "pear",  "aple", False )
    test_uses_all ( "apple", "peal", True )

else :
    required = raw_input("Enter the required letters")
    fin = open("words.txt", "r")
    uses_all_ctr = 0
    for line in fin :
        word = line.strip()
        if uses_all ( word, required ) :
            uses_all_ctr = uses_all_ctr + 1
            print "%s uses only %s" % (word, required )
    
        
    print "There are %d words that use all the characters %s" % (
         uses_all_ctr, required )

    fin.close()
    

                                                                  
