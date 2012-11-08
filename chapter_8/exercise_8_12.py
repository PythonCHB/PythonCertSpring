#! /usr/bin/python
# -*- coding: utf-8 -*-
#
# Exercise 8.12
# ROT13 is a weak form of encryption that involves “rotating” each letter in a
# word by 13 places. To rotate a letter means to shift it through the alphabet,
# wrapping around to the beginning if necessary, so ’A’ shifted by 3 is ’D’
# and ’Z’ shifted by 1 is ’A’.
# Write a function called rotate_word that takes a string and an integer as
# parameters, and that returns a new string that contains the letters from the
# original string “rotated” by the given amount.
# For example, “cheer” rotated by 7 is “jolly” and “melon” rotated by -10
# is “cubed”.
# You might want to use the built-in functions ord, which converts a character
# to a numeric code, and chr, which converts numeric codes to characters.
#
# Potentially offensive jokes on the Internet are sometimes encoded in ROT13.
# If you are not easily offended, find and decode some of them.
# Solution: http://thinkpython.com/code/rotate.py.

# import string     # You need to do this to get the ord and chr functions
                  # See 

def rotate_word ( w, i ) :
    """Rotate the characters in string w by i places"""

    result = ""
    for c in w :        
        result = result + rotate_char ( c, i )
    return result

def rotate_char ( c, i ) :
    """rotate character c by i places.  If c is not an uppercase or lowercase
letter (e.g. if it is a number or punctuation) then do not rotate it. """
# At least Prof. Downey has that restriction in his example.  If you assumed
# that the character set is ASCII and did modulo 127 instead of modulo 26, then
# you could rotate any ASCII character.  Food for thought: how would you
# implement rotate_char for Unicode-8?  And for you budding cryptologists: why
# is this encryption system weak?
    if c.isupper():
        start = ord('A')    # Who remembers that the ASCII value for A is 65?
    elif c.islower():
        start = ord('a')    # Who remembers that the ASCII value for a is 97?
# If this is the kind of trivia that floats your boat and you are running UNIX
# or cygwin, give the command "man ascii" for assistance
    else:
        return c

    index = ord(c) - start
    new_char = chr ( (index + i) % 26 + start )
    return new_char
 

if __name__ == "__main__" :
    def test_rotate_word ( w , i ) :
        """This tests whether word w is rotated properly by rotating it, printing it,
then rotating it back and checking that it is unchanged"""
        cypher_text = rotate_word ( w, i )
        print "The cyphertext of %s is %s" % ( w, cypher_text )
        clear_text = rotate_word ( cypher_text, -i )
        if clear_text == w :
            print "%s works!" % w
        else :
            print "%s FAILS.  The recovered text is %s" % ( w, clear_text )


    test_rotate_word ("Jeff", 4 )
    test_rotate_word ("truck", 10 )
    test_rotate_word ("BLAM!!", 6 )
    test_rotate_word ("We rob the 3:10 at Yuma.", 17 )



    
