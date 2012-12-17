#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# Exercise 17-2  
# Write an init method for the Point class that takes x and y as optional
# parameters and assigns them to the corresponding attributes.
#
#
# Exercise 15-4
# World.py, which is part of Swampy (see Chapter 4), contains a class definition
# for a user-defined type called World. You can import it like this:
# 
# from World import World
# This version of the import statement imports the World class from the World
# module. The following code creates a World object and calls the mainloop method, which waits for the user.
# world = World()
# world.mainloop()
# A window should appear with a title bar and an empty square. We will use this
# window to draw Points, Rectangles and other shapes. Add the following lines
# before calling mainloop and run the program again.
#
# canvas = world.ca(width=500, height=500, background='white')
# bbox = [[-150,-100], [150, 100]]
# canvas.rectangle(bbox, outline='black', width=2, fill='green4')
# You should see a green rectangle with a black outline. The first line creates
# a Canvas, which appears in the window as a white square. The Canvas object
# provides methods like rectangle for drawing various shapes.
#
# bbox is a list of lists that represents the “bounding box” of the rectangle.
# The first pair of coordinates is the lower-left corner of the rectangle; the
# second pair is the upper-right corner.
#
# You can draw a circle like this:
# 
# canvas.circle([-25,0], 70, outline=None, fill='red')
# The first parameter is the coordinate pair for the center of the circle; the
# second parameter is the radius.
#
# If you add this line to the program, the result should resemble the national
# flag of Bangladesh (see wikipedia.org/wiki/Gallery_of_sovereign-state_flags).
#
#
# 1) Write a function called draw_rectangle that takes a Canvas and a Rectangle as
# arguments and draws a representation of the Rectangle on the Canvas.
# 2) Add an attribute named color to your Rectangle objects and modify
# draw_rectangle so that it uses the color attribute as the fill color.
# 3) Write a function called draw_point that takes a Canvas and a Point as
# arguments and draws a representation of the Point on the Canvas.
# 4) Define a new class called Circle with appropriate attributes and instantiate
# a few Circle objects. Write a function called draw_circle that draws circles
# on the canvas.
# 5) Write a program that draws the national flag of the Czech Republic. Hint: you
# can draw a polygon like this:
# points = [[-150,-100], [150, 100], [150, -100]]
# canvas.polygon(points, fill='blue')

from World import World

class Point(object) :
    """A class for a point"""

    def __init__ (self, x, y ):
        """A constructor for a point object"""
        self.x = x
        self.y = y

class Rectangle(object) :
    """A class for a rectangle"""
    pass

class Circle(object) :
    """A class for circles.  Attributes should be x, y for the center, r for the radius"""
    pass

def draw_rectangle( canvas, rect, color='yellow', outline='black', width=2 ):
    """A subroutine that draws a rectangle on canvas canvas"""
    assert isinstance( rect.llc, Point ) and isinstance ( rect.urc, Point ), "At least one of the \
corners of the rectangle is not a Point object"
    
    bbox = [[rect.llc.x, rect.llc.y],[rect.urc.x, rect.urc.y]]
    canvas.rectangle(bbox, fill=color, outline=outline, width=width )

def draw_point ( canvas, point, color='black') :
    """This draws a point at point on canvas canvas with color color"""
# canvas doesn't have a point method so I am going to simulate a point by drawing a 1x1 rectangle    
    assert isinstance( point, Point ), "argument point is not a Point"
    bbox = [[point.x, point.y],[point.x+1, point.y+1] ]
    canvas.rectangle(bbox, fill=color, outline=color, width=1 )

def draw_circle (canvas, center, radius, color='yellow', outline='black'):
    """This subroutine draws a circle centered at center with radius radius.  The fill color is
fill and the outline color is outline"""
    canvas.circle( [center.x, center.y], radius, outline=outline, fill=color )
    

world = World()
canvas = world.ca(width=500, height=500, background='white')
bbox = [[-225,-150], [75, 50]]
canvas.rectangle(bbox, outline='black', width=2, fill='green4')
canvas.circle([-75,-50], 70, outline=None, fill='red')
llc = Point(60,160)
urc = Point(60, 240)
rect = Rectangle()
rect.llc = llc
rect.urc = urc
draw_rectangle( canvas, rect, color='brown', width=3, outline='green')
print dir(canvas)
urc.x += 10
llc.x -= 10
draw_point( canvas, urc, color='blue')
draw_point( canvas, llc, color='red' )

# Draw the national flag of the Czech republic
points = [[140,-40], [140,-80], [200,-80], [200,-40],[140,-40]]
canvas.polygon(points, fill='white', outline='black', width=1 )
points = [[140,-40], [140,-80], [157.32, -60]]
canvas.polygon(points, fill='blue')
points = [[140, -80], [157.32,-60], [200,-60],[200,-80],[140,-80]]
canvas.polygon(points, fill='red')
# Draw a circle
c = Circle()
c.x = -100
c.y = 160
r = 80
draw_circle ( canvas, c, r, color='blue', outline=None )
draw_circle ( canvas, c, r/2, color='green', outline=None )
draw_circle ( canvas, c, r/4, color='yellow', outline=None )


world.mainloop()

