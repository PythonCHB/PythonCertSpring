#! /usr/bin/python
#!
# This is from http://greenteapress.com/thinkpython/html/thinkpython006.html
# This program tests Fermat's last theorem that, for any n > 2, there are no
# integers a,b,c such as a**n + b**b = c**n


def test_fermat ( a, b, c, n ) :
    if n>2 and ( a**n + b**n == c**n ) :
        print "Holy smokes!  Fermat was wrong!"
    else :
        print "No, that doesn't work"


while True :
    a = int ( raw_input("Enter a ") )
    b = int ( raw_input("Enter b ") )
    c = int ( raw_input("Enter c ") )
    n = int ( raw_input("Enter n ") )

    test_fermat ( a, b, c, n )
    
