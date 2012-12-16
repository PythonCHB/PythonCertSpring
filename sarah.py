#! /usr/bin/python
# -*- coding: utf-8 -*-
#
#
sarah = u"הרש"



ali=u" علي اصغر‎"
	
sheshech=u"현륜식"


def decode_unicode(s) :
    """This function decodes a unicode string, character by character"""
    print s
    for c in s:
        print c, ord(c)

decode_unicode(sarah)
decode_unicode(ali)
decode_unicode(sheshech)



    
