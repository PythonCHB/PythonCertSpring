#! /usr/bin/env python
#
#
# Exercise 13-4
#
# Modify the previous program to read a word list (see Section 9.1) and then
# print all the words in the book that are not in the word list. How many of
# them are typos? How many of them are common words that should be in the word
# list, and how many of them are really obscure?


import critique_book_13_2
import sys



# This is pretty much all of exercise 9.1
def read_word_list() :
    """This function opens the file word.txt and reads it in, stripping all of
the newlines from it.  It then returns the contents of the file as a list"""
    fin = open("words.txt", "r")
    word_list = []
    for line in fin :
        word = line.strip()
        word_list.append(word)
    fin.close()
    return word_list

if __name__ == "__main__" :
    word_list = read_word_list()
    doc_word_list = critique_book_13_2.file_to_word_list( sys.argv[1] )
    census = critique_book_13_2.word_counter ( doc_word_list )
    for word in census :
        if word not in word_list :
            print word

    
