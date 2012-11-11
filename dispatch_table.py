#! /usr/bin/env python
#
# This demonstrates a weird data structure, a dictinary of functions


def f_1() :
    print "In function", f_1.func_name
   
def f_2() :
    print "In function", f_2.func_name

def f_3() :
    print "In function", f_3.func_name

def f_4() :
    print "In function", f_4.func_name

def f_5() :
    print "In function", f_5.func_name

def initialize_dispatch_table() :
    """The dispatch table is a dictionary of functions keyed by integers"""
    dt = dict()
    dt[1] = f_1
    dt[2] = f_2
    dt[3] = f_3
    dt[4] = f_4    
    dt[5] = f_5
    return dt

if __name__ == "__main__" :
    dispatch_table = initialize_dispatch_table()

    while True :
        event = int(raw_input("Enter an event between 1 and 5 inclusive "))
        if 1 <= event <= 5 :
            dispatch_table[event]()
    
                

