#! /usr/bin/python
# -*- coding: utf-8 -*-
#
# Exercise 9.8
# “I was driving on the highway the other day and I happened to notice my
# odometer. Like most odometers, it shows six digits, in whole miles only. So,
# if my car had 300,000 miles, for example, I’d see 3-0-0-0-0-0.
# “Now, what I saw that day was very interesting. I noticed that the last 4
# digits were palindromic; that is, they read the same forward as backward. For
# example, 5-4-4-5 is a palindrome, so my odometer could have read 3-1-5-4-4-5.
#
# “One mile later, the last 5 numbers were palindromic. For example, it could
# have read 3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were
# palindromic. And you ready for this? One mile later, all 6 were palindromic!
#
# “The question is, what was on the odometer when I first looked?”
#
# I need the is_palindrome function that I wrote for chapter 8.  The software
# is organized by chapters so I had to create a symlink from chapter 9 to chapter 8
# with the linux command
#
# ln -s ../chapter_8/exercise_8_10.py .

from exercise_8_10 import is_palindrome


mile = 0
while mile <= 999999 :
    mile_str = "%06d" % mile
    if is_palindrome ( mile_str[-4:] ) :
#        print "%s has last 4 digits a palindrome" % mile_str
        res_str = mile_str + " "
        mile += 1
        mile_str = "%06d" % mile
        if is_palindrome ( mile_str[-5:] ) :
            res_str = res_str + mile_str + " "
            print "*** %s has last 5 digits a palindrome" % mile_str
            mile += 1
            mile_str = "%06d" % mile
            if is_palindrome ( mile_str[1:4] ) :
                res_str = res_str + mile_str + " "
                print "<><><><> %s has the middle 4 digits a palindrome" % mile_str
                mile += 1
                mile_str = "%06d" % mile
                if is_palindrome ( mile_str ) :
                    res_str = res_str + mile_str + " "
                    print "mile %d meets the confitions " % mile
                    print "!!!!!" + res_str
                    t = raw_input("Hit enter to continue" )
    mile += 1




