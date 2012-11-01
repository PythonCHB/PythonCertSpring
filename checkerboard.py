#! /usr/bin/env python
#
# This simulates a checkerboard or a chess board

def set_square_color ( a, r, c ):
    "This sets the square color to what it is supposed to be"
    a[r][c] = "*" if (r+c)%2 == 0 else " " 

def return_checkerboard() :
    """This function returns an 8x8 checkboard.  The white spaces are white and
the black spaces are "*" """
    a=[]
    for r in range(8):
        a.append([])
        for c in range(8) :
            a[r].append([])
            set_square_color( a, r, c)     
    return a

def print_checkerboard( b ) :
    "This prints an 8x8 checkboard"
    for r in range(8) :
        for c in range(8) :
            print b[r][c],
        print

a = return_checkerboard()
print_checkerboard(a)
print

a[0][0] = "Q"
a[1][2] = "Q"
a[2][4] = "Q"
a[3][6] = "Q"

print_checkerboard(a)




