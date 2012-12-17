#! /usr/bin/env python
#
#
from visual import *

scene.range = (256, 256, 256)
scene.center = (128, 128, 128)

# Download thinkpython.com/code/color_list.py and use the function read_colors
# to generate a list of the available colors on your system, their names and
# RGB values. For each named color draw a sphere in the position that corresponds
# to its RGB values.

import color_list
import re

if __name__ == "__main__" :
    # regular expressions to match numbers and color names
    number = r'(\d+)'
    space = r'[ \t]*'
    name = r'([ \w]+)'
    pattern = space + (number + space) * 3 + name
    prog = re.compile(pattern)

    for line in color_list.COLORS.split('\n'):
        ro = prog.match(line)
        if ro:
            r, g, b, name = ro.groups()
            rn = int(r)
            gn = int(g)
            bn = int(b)
            pos=(rn, gn, bn )
            color=(rn/256., gn/256., bn/256.)
            sphere(pos=pos, radius=10, color=color)
