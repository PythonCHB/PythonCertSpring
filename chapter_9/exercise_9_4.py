#! /usr/bin/python
# -*- coding: utf-8 -*-
#
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list. Can you
# make a sentence using only the letters acefhlo? Other than “Hoe alfalfa?”
# "Cool each fella" is such a sentence.

TEST = False

def uses_only ( word, string ) :
    """uses_only returns true if the word word contains only letters in the string
string"""
    for c in word :
        if c not in string :
            return False
    return True

if TEST :
    def test_uses_only ( word, string, expected ) :
        r = uses_only ( word, string )
        if r == expected :
            print "%s %s works as expected" % ( word, string )
        else :
            print "%s %s FAILS, returned %s expected %s" % ( word, string, str(r), str(expected) )


    test_uses_only ( "Mississippi", "Misp", True )
    test_uses_only ( "apple", "ape", False )
    test_uses_only ( "apple", "aple", True )

else :
    only_chars = raw_input("Enter letters ")
    fin = open("words.txt", "r")
    for line in fin :
        word = line.strip()
        if uses_only ( word, only_chars ) :
            print "%s uses only %s" % (word, only_chars )


