#! /usr/bin/python
#
# http://greenteapress.com/thinkpython/html/thinkpython008.html
# Chapter 7 exercise 4
#

def eval_loop () :
    while True :
        e = raw_input(" Enter an expression to evaluate (be gentle) or 'done' if done " )
        if e == "done" :
            break
        r = eval( e )
        print r

eval_loop()
