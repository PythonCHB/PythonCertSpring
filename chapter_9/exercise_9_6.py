#! /usr/bin/python
#
# Exercise 9.6
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok). How many
# abecedarian words are there?

TEST = False

def sort_string( s ) :
    """This function sorts string s so that the characters in the string are
in order"""
# This implementation is somewhat cheating because it uses lists.  If I get some
# time, I will write an all strings version.  That's hard because strings are
# immutable.  Perhaps a bubble sort...
    l = list(s)
    l.sort()
    s = "".join(l)
    return s

if TEST :
    while True :
        s = raw_input("Enter a string ")
        t = sort_string(s)
        if t == s :
            print "%s is an abecedarian word" % s
        else :
            print "%s is NOT an abecedarian word" % s


else :            
    fin = open("words.txt", "r")
    abecedarian_ctr = 0
    for line in fin :
        word = line.strip()
        t = sort_string( word)
        if word == t :
            abecedarian_ctr = abecedarian_ctr + 1
            print "%s is abecedarian" % word
    
        
    print "There are %d abecedarian words" % (
         abecedarian_ctr )
