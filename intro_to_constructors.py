#! /usr/bin/python
#
#
class C(object) :
    def __init__(self, x, y) :
        self.x = x
        self.y = y

i = C("Kg","Slug")

print i.x, i.y
