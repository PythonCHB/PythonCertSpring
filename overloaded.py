#! /usr/bin/env python
#
# Operator overloading demonstration
import numbers

class Vector_3 ( object ) :
    """This class implements vector arithmetic for three dimensional vectors.
The class includes overloaded operators for addition, subtraction, and
multiplication (inner product)"""

    def __init__ (self, x, y, z ) :
        """Constructor"""
        self.x = x
        self.y = y
        self.z = z
        

    def __str__ ( self ) :
        return "["+str(self.x)+", "+str(self.y)+", "+str(self.z)+" ]"

    def __add__ (self, v ) :
        """Implements vector_3 addition"""
        assert isinstance ( v, Vector_3 ),"Passed something that was not a Vector_3 to __add__"
        xt = self.x + v.x
        yt = self.y + v.y
        zt = self.z + v.z
        r = Vector_3(xt, yt, zt)
        return r

    def __mul__ ( self, v ) :
        """Implements either vector inner product if v is a Vector_3 or linear
scaling if v is a float, int, or complex"""
        if isinstance(v, numbers.Number ) :     # numbers.Number is the base class
                                                # of ints, floats, and complex
            xt = self.x * v
            yt = self.y * v
            zt = self.z * v
            r = Vector_3(xt, yt, zt)
        elif isinstance(v, Vector_3) :
            r = self.x * v.x + self.y * v.y + self.z * v.z
        else :
            raise AssertionError("__mul__ was passed an argument that isn't a Vector_3 or a numeric")
        return r

    def __rmul__( self, v ):
        """Just like __mul__ only the arguments are reversed.  The combination
of __rmul__ and __mul__ make addition commutative"""
        return self.__mul__(v)
    
    def __eq__ ( self, v ) :
        """Compares two vectors for equality"""
        assert isinstance ( v, Vector_3 ),"Passed something that was not a Vector_3 to __eq__"
        return self.x == v.x and self.y == v.y and self.z == v.z

    def __ne__ ( self, v ) :
        """Compares two vectors for inequality"""
        assert isinstance ( v, Vector_3 ),"Passed something that was not a Vector_3 to __ne__"
        # De Morgan's laws http://en.wikipedia.org/wiki/De_Morgan's_laws
        return self.x != v.x or self.y != v.y or self.z != v.z
      
                 


if __name__ == "__main__" :
    z = Vector_3(0.0, 0.0, 0.0)
    one = Vector_3(3., 4., 5.)
    r = z + one
    print r,"should be [3.0, 4.0, 5.0]"
    assert r == Vector_3(3., 4., 5.), "First Equality or 2 operand vector addition failed"
    two = Vector_3(2.0, 1.0, 7.0 )
    r = one + two
    print r,"should be [6.0, 5.0, 12.0]"
    assert r == Vector_3(5.0, 5.0, 12.0 ), "Second Equality or 2 operand vector addition failed"
    r += Vector_3(1., 2., -3.0)
    print r,"should be [6.0, 7.0, 9.0]"
    assert r == Vector_3(6.0, 7.0, 9.0 ), "Equality or 1 operand vector addition failed"
    r *= 0.5
    t = Vector_3(3.0, 3.5, 4.5 )
    print r,"should be",t
    assert r == t, "Multiplication by floating scalar failed"
    r *= 4
    t = Vector_3(12.0, 14.0, 18.0)
    print r,"should be",t
    assert r == t, "Multiplication by integer scalar failed"
    r = 0.25 * t
    t = Vector_3(3.0, 3.5, 4.5 )
    print r,"should be",t
    assert r == t, "Reverse multiplication by a scalar failed"
    r *= 4.0*(2+1j)
    t = Vector_3((24.0+12j), (28.0+14j), (36.0+18j))
    print r,"should be",t
    assert r == t, "Multiplication by complex scalar failed"
    a = Vector_3(2, 3, 4)
    b = Vector_3(4, 5, 6)
    c = a * b
    t = 47  # (2*4) + (3*5) + (4*6) note that this is an integer
    print c,"should be",t
    assert c == t, "Multiplication by inner product failed"
    a *= b
    print a,"should be",t
    assert a == t, "Multiplication by inner product failed"
    a = Vector_3(2., 3., 4.)
    b = Vector_3(4., 5., 6.)
    c = a * b
    t = 47.  # (2*4) + (3*5) + (4*6) note that this is a float
    print c,"should be",t
    assert c == t, "Multiplication by inner product failed"
    a *= b
    print a,"should be",t
    assert a == t, "Multiplication by inner product failed"
    print "This should raise an AssertionError"
    v2 = (3, 4, 5)
    a = Vector_3(2., 3., 4.)
    try :
        a = a * v2
    except AssertionError,e :
        print "AssertionError exception was raised %s" % e
    print a
    
    
    
    

    
    
    
    
    
