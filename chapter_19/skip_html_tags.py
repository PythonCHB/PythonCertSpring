#! /usr/bin/env python
#
# skip_html_tags.py
# This module has some helper functions for processing HTML (and XHTML and XML)
# The only function implemented so far is skip_html_tags which accepts a string,
# which is an HTML file, and removes all of the HTML (or XML or XHTML) tags from
# it.  This is rather naive.  An improved version is planned which will remove
# the header and also get all of the images.
import re

def skip_html_tags ( html ) :
    """This function strips all of the HTML tags from string html and returns
a string which is html with all the tags removed"""
# Create a new string with all of the HTML tags removed.  The regex <.+?> matches
# any string that begins with a <, has at least one character, and ends with a >
# using a not-greedy match.
    q = re.sub(r"<.+?>","", html)
    return q

def skip_html_header ( html ) :
    """This function skips all of the text between the <head> tag and the </head>
tag."""
    q = re.sub(r"<head>.*</head>","", html)
    return q
    

if __name__ == "__main__" :
    html = """<html><head><meta title="A random title"></head>
<body>
some text
<ul>
<li>List item 1</li>
<li>List item 2</li>
</ul>
<p>This is a paragraph
<p>This is a paragraph, too, although it is compliant with the HTML 3.0 specification
which calls for a required closing &lt;/p&gt; tag.</p>
</body>
</html>"""
    stripped = skip_html_tags( html )
    print "The input is ",html
    print "\n\nThe output of skipped_html_tags is", stripped

    html_body = skip_html_header( html )
    print "The input is ",html
    print "\n\nThe output of skip_html_header is", html_body
    
    
    
