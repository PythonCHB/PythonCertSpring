from World import *
from TurtleWorld import *

import Lumpy
lumpy = Lumpy.Lumpy()
lumpy.make_reference()

world = TurtleWorld()
bob = Turtle(world)

lumpy.object_diagram()
lumpy.class_diagram()
