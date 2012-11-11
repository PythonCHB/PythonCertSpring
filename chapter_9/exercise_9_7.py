#! /usr/bin/python
# -*- coding: utf-8 -*-
#
# Exercise 9.7
# Give me a word with three consecutive double letters. I’ll give you a couple
#of words that almost qualify, but don’t. For example, the word committee,
# c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’ that sneaks in there.
# Or Mississippi: M-i-s-s-i-s-s-i-p-p-i. If you could take out those i’s it
# would work. But there is a word that has three consecutive pairs of letters
# and to the best of my knowledge this may be the only word. Of course there
# are probably 500 more but I can only think of one. What is the word?

def double_letter ( word ) :
    """ Returns True if word begins with a double character """
    if len( word ) < 2 :
        return False
    return word[0] == word[1]

fin = open("words.txt", "r")
for line in fin :
    word = line.strip()
    rep_ctr = 0
    i = 0
    while i < len ( word )  :
        if double_letter ( word[i:] ) :
            rep_ctr += 1
            i += 2
        else :
            rep_ctr = 0     # The double letters have to be consecutive
            i += 1
        if rep_ctr >= 3 :
            print "%s has three repeating double characters" % word
fin.close()

