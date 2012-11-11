#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Exercise 12-6
# Here’s another Car Talk Puzzler (http://www.cartalk.com/content/puzzler/transcripts/200651):
# What is the longest English word, that remains a valid English word, as you
# remove its letters one at a time?
# Now, letters can be removed from either end, or the middle, but you can’t
# rearrange any of the letters. Every time you drop a letter, you wind up with
# another English word. If you do that, you’re eventually going to wind up with
# one letter and that too is going to be an English word—one that’s found in the dictionary. I want to know what’s the longest word and how many letters does it have?
# I’m going to give you a little modest example: Sprite. Ok? You start off with
# sprite, you take a letter off, one from the interior of the word, take the r
# away, and we’re left with the word spite, then we take the e off the end,
# we’re left with spit, we take the s off, we’re left with pit, it, and I.
#
# Write a program to find all words that can be reduced in this way, and then
# find the longest one.
#
# This exercise is a little more challenging than most, so here are some
# suggestions:
#
# You might want to write a function that takes a word and computes a list of
# all the words that can be formed by removing one letter. These are the
# “children” of the word.
# Recursively, a word is reducible if any of its children are reducible. As a
# base case, you can consider the empty string reducible.
# The wordlist I provided, words.txt, doesn’t contain single letter words. So
# you might want to add “I”, “a”, and the empty string.
# To improve the performance of your program, you might want to memoize the
# words that are known to be reducible.
# Solution: http://thinkpython.com/code/reducible.py.

DEBUG = False
import anagrams_12_4

# To memoize the function children_of_word, we remember which words we already
# know to be children
children_dict = {}

def children_of_word ( word ) :
    """This function returns a list of children of the word.  A word is a "child"
of this word if it has 1 letter removed from this word and is in the word list"""
    global word_list   # word_list doesn't change and it is huge, so it is okay
                       # to pass globally
    children_of_word_list = []
# Here are some corner cases.                       
    if word == "I" or word == "a" or word == "A" or word == "":
        return [word]
    if word in children_dict :
        return children_dict[word]
    for i in range( 0, len ( word ) ) :
        if i == 0 :
            potential_child_word = word[1:]
        elif i==len(word)-1 :
            potential_child_word = word[:-1]
        else :
            potential_child_word = word[:i] + word[i+1:]
        if potential_child_word in word_list :  # Would this be faster in a dict?
            if DEBUG :
                print potential_child_word,
# since potential_child_word is known to be in the word list, technically, it is
# now a child_word and not a potential_child_word
            children_of_word_list.extend ( \
                children_of_word ( potential_child_word ) )
# momoize this list of children words of potential_child_word
            children_dict[potential_child_word] = children_of_word_list
    return children_of_word_list



if __name__ == "__main__" :
    word_list = anagrams_12_4.initialize_word_list()
    solutions={}
    for word in word_list :
        solutions[word] = children_of_word( word )
    for word in solutions.keys() :
        print word,":", solutions[word]

