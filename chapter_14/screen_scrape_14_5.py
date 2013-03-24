#! /usr/bin/env python
#
# Exercise 14-5.  This program demonstrates how to refer to an object on the web
# using the file interface
#
# The urllib module provides methods for manipulating URLs and downloading
# information from the web. The following example downloads and prints a secret
# message from thinkpython.com:
import urllib


def extract_substring( fullstring, preamble, postamble ) :
    """This function returns the string in fullstring between string preamble
and string postamble"""
# See http://docs.python.org/2/library/stdtypes.html#string-methods
    try :
        start_idx = fullstring.index(preamble) + len(preamble)
        end_idx = fullstring.index(postamble)
    except ValueError :
        print """There is a problem screen scraping.  There is a line that contains
%s but not %s, so the indexing functions failed""" % ( preamble, postamble)
    extract = fullstring[start_idx:end_idx]
    return extract
    


conn = urllib.urlopen('http://www.uszip.com/zip/02492')
preamble_population = r"Population:</b></td><td>"
preamble_location = r"<title>Zip code for "
for line in conn.fp:
    if preamble_population in line :
        population = extract_substring( line, preamble_population, \
                        """ <span style="font-size:10px">""" )
    elif preamble_location in line :
        location = extract_substring ( line, preamble_location, " - " )
    else :
        pass

print "The population of %s is %s" % (location, population)
                                        

    
