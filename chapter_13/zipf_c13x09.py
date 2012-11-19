''' 20121117jdr
    Write a program that reads text from a file, counts word frequencies, and
    prints one line for each word, in descending order of frequency, with log(f)
    and log(r).'''

import math, critique_book_13_2

def sum_freq(c):
    ''' Given a list of words, return a dict of word/frequency as key/value.
        c: List of words (as in a book)
        d: Dict of word/frequency key/value pairs to return
        w: Each word in list c'''
    d = {}
    for w in c: d[w] = (d[w] if w in d else 0) + 1          # Insert/increment
    return d

def sort_val(d):
    ''' Given a dict of word/frequency key/value pairs, return a sorted list of
        frequency/word tuples.
        Note: this is tuples of values and keys, not tuples of keys and values.
        d: Dict of word/frequency pairs
        t: List of frequency/word tuples to make, fill, sort and return
        w: Each word (key) in dict d'''
    t = []
    for w in d: t.append((d[w], w))     # Append frequency/word tuples
    t.sort(reverse = True)              # Sord descending on frequency
    return t

def add_rank(t):
    ''' Given a list of frequency/word tuples that is sorted from highest to
        lowest frequency, calculate the rank for each frequency and replace the
        tuples with tuples of log(frequency)/log(rank)/word.
        t: List of frequency/word tuples, sorted descending on frequency, to be
           changed to a list of log(f)/log(r)/word tuples (same order)
        r: Rank--starts at 1 and increments by 1 at each drop in frequency
        i: Index of the for loop'''
    r = 1
    p = t[0][0]                         # The previous frequency to start with
    for i in range(len(t)):
        if  t[i][0] < p: r += 1         # Up r when f drops
        p = t[i][0]                     # Get previous frequency for next loop
        t[i] = (math.log(t[i][0]), math.log(r), t[i][1])

def out_file(t, csv):
    ''' Write the tuples in a given list to the specified file.
        Separate the columns with commas and the lines with newlines.
        t: List of log(f)/log(r)/word tuples to write
        csv: Path and name of csv file to write out
        fout: File handle
        i: Each tuple in list t'''
    fout = open(csv, 'w')
    fout.write(            'logf, logr, word\n')
    for i in t: fout.write('%f, %f, "%s"\n' % i)
    fout.close()

def zipf_csv(txt, csv):
    ''' Write out a Zipf's law csv file based on a list of words.
        txt: Path and name of text file (like a book) to evaluate
        csv: Path and name of resulting csv file to write out
        c: List of words in the given input file
        d: Dict of items and their frequency in c.
        s: List of frequency/word tuples, to be sorted (a form of Ranking) and
           then changed into a list of log(f)/log(r)/word tuples, to be output
           and graphed'''
    c = critique_book_13_2.file_to_word_list(txt)
    d = sum_freq(c)
    s = sort_val(d)
    add_rank(s)
    out_file(s, csv)

# Alice's Adventures in Wonderland by Lewis Carroll
# http://www.gutenberg.org/ebooks/11
zipf_csv('Alice.txt', 'c13x09.csv')
