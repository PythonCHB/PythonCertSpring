#! /usr/bin/python
#
#
import multiple_inheritence as mi

def test_instance_of ( obj, obj_name, obj_class ) :
    print obj_name, "is", "" if isinstance(obj, obj_class) else "not", \
            "an instance of ", obj_class.__name__


test_instance_of ( mi.e, 'e', mi.E )
test_instance_of ( mi.a, 'a', mi.E )
test_instance_of ( mi.e, 'e', mi.A )
test_instance_of ( mi.b, 'b', mi.A )

def dispatcher ( g ):
    if isinstance(g, mi.A) :
        print g.a
    elif isinstance(g, mi.C) :
        print g.c
    else :
        print g.e

dispatcher ( mi.a )
dispatcher ( mi.b )
dispatcher ( mi.c )
dispatcher ( mi.d )
dispatcher ( mi.e )
try :
    dispatcher ( "gee" )
except AttributeError, err :
    print "WHOOPS!", err

    
    
