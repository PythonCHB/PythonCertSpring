#! /usr/bin/python
#
#
import multiple_inheritence as mi

def test_instance_of ( obj, obj_name, obj_class ) :
    print obj_name, "is", "" if isinstance(obj, obj_class) else "not", \
            "an instance of ", obj_class.__name__



def dispatcher ( g ):
    if isinstance(g, mi.A) :  
        print g.a
    elif isinstance(g, mi.C) :
        print g.c
    else :
        print g.e

test_instance_of ( mi.e, 'e', mi.E )
test_instance_of ( mi.a, 'a', mi.E )
test_instance_of ( mi.e, 'e', mi.A )
test_instance_of ( mi.b, 'b', mi.A )

dispatcher ( mi.a )
dispatcher ( mi.b ) # b is of type class B which inherits from A
dispatcher ( mi.c )
dispatcher ( mi.d ) # d is of type class D which inherits from C
dispatcher ( mi.e ) # e is of type class E which inherits from B (and from A)
                    # and D (and from C), so dispatcher never prints e.e
try :
    dispatcher ( "gee" )
except AttributeError, err :
    print "WHOOPS!", err

    
    
