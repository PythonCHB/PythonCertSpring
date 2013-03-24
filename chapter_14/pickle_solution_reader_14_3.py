#! /usr/bin/env python
#
#
# Exercise 12-3 part 2: the reader

#
import pickle

f=open("anagrams.pickle","r")   # This file was previously pickled
anagram_dict=pickle.load(f)     # A dictionary of lists of strings.  Each list of
                                # strings contains anagrams
f.close()

for key in anagram_dict:
    anagram_list = anagram_dict[key]
    if len(anagram_list) > 1 :
        print anagram_list
