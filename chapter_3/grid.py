#! /usr/bin/python
# Chapter 3 exercise 4
"""Write a program that draws an 2x2 grid.  Each cell of the grid is bounded by
a string with pattern " - - - - ".  The corners of the cells are marked by +

For example, a 2 x 2 grid looks like:

+ - - - - +  - - - - +
|         |          |
|         |          |
|         |          |
|         |          |
+ - - - - +  - - - - +
|         |          |
|         |          |
|         |          |
|         |          |
+ - - - - +  - - - - +

"""

def draw_horizontal_line() :
    """Draw a horizontal line.  The leading plus sign is not printed here, and
must be printed by the caller.  The trailing newline is not printed and must
be added by the caller"""
    print "+ - - - - + - - - -",

def draw_vertical_lines() :
    """Draw two vertical lines at the right spacing to make the cells.  The
trailing | and possibly the trailing newline is not printed and must be
added by the caller"""
    print "|         |        ",

def draw_1_row_of_2() :
    """Draw a row of 2 grid cells. """
    draw_vertical_lines()
    print "|"   #Print trailing | and newline"
    draw_vertical_lines()
    print "|"
    draw_vertical_lines()
    print "|"
    draw_vertical_lines()
    print "|"
    draw_horizontal_line()
    print "+"      # print the trailing plus and newline
    

def draw_1_row_of_4() :
    """Draw a row of 4 grid cells. """
    draw_vertical_lines()   
    draw_vertical_lines()
    print "|"   #Print trailing | and newline"
    draw_vertical_lines()
    draw_vertical_lines()
    print "|"
    draw_vertical_lines()
    draw_vertical_lines()
    print "|"
    draw_vertical_lines()
    draw_vertical_lines()
    print "|"
    draw_horizontal_line()
    draw_horizontal_line()
    print "+"      # print the trailing plus and newline
    

draw_horizontal_line()
print "+"      # print the trailing + and the trailing newline

draw_1_row_of_2()
draw_1_row_of_2()

print "*"*80
draw_horizontal_line()
draw_horizontal_line()
print "+"      # print the trailing + and the trailing newline
draw_1_row_of_4()
draw_1_row_of_4()
draw_1_row_of_4()
draw_1_row_of_4()
