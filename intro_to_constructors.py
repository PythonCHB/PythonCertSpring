#! /usr/bin/python
#
#
class C(object) :
    w = 18
    def __init__(self, x, y) :
        self.n = 16
        self.x = x
        self.y = y

i = C("Kg","Slug")

print i.x, i.y, i.n, i.w

j = C("slush", 32.3)
print j.x, j.y, j.n, j.w

j.w = "Hah!"

print j.w, i.w

C.w = "Ireland"

print j.w, i.w

del j.w

print j.w, i.w

try :
    k = C("yes","no","maybe")
except TypeError, e:
    print "This didn't work so good "+str(e)




