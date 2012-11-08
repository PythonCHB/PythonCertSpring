#! /usr/bin/python
# -*- coding: utf-8 -*-
#
# Exercise 9.2
# In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that
# does not contain the letter “e.” Since “e” is the most common letter in
# English, that’s not easy to do.  In fact, it is difficult to construct a
# solitary thought without using that most common symbol. It is slow going at
# first, but with caution and hours of training you can gradually gain facility.
# Write a function called has_no_e that returns True if the given word doesn’t
# have the letter “e” in it.
# Modify your program from the previous section to print only the words that
# have no “e” and compute the percentage of the words in the list have no “e.”

fin = open("words.txt", "r")
ctr = 0
w_ctr = 0
for line in fin :
    word = line.strip()
    w_ctr += 1
    if not ( 'e' in word or 'E' in word ) :
#        print "%s does not contain the letter 'e'" % word  # This takes too long, but is useful for debugging
        ctr += 1
print "There are %d words that do not contain the letter 'e' out of %d words" % (
    ctr, w_ctr )
print "That is %.2f %%" % (( 100.0 * float(ctr)/float(w_ctr) ),)

fin.close()
