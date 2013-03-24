# 20121111jdr os_path_walk.py

BASE_DIR = r"C:\_dev\aaa"
MAKE_LOC =  "Number of levels to make (or return for none): "
TAKE_LOC =  "Number of levels to take (or return for none): "

import os

def get_input(L):
    ''' Obtain input from the user for the number of levels.'''
    L = raw_input(L)
    return int(L if L else 0)

def make_tree(L):
    ''' Make a file and folder tree for demonstration purposes.'''
    s = os.getcwd()                 # remember   starting directory
    os.chdir(BASE_DIR)
    for x in range(L + 1):
        d = "dir%d" % (L - x)
        os.mkdir(d)
        os.chdir(d)
        print "In %s" % os.getcwd()
        for y in range(L - x):
            f = "fil%d" % (y + 1)
            fout = open(f, "w"); fout.write("Hello, world!\n"); fout.close()
        
    os.chdir(s)                     # go back to starting directory
    print "Back in %s" % os.getcwd()

def del_files(L):
    ''' Delete files level L and lower. Delete empty folders.'''
    for r, d, f in os.walk(BASE_DIR, topdown = False):
        for name in f:
            if int(name[-1]) <= L:
                try:
                    os.remove(os.path.join(r, name))
                except OSError, e:
                    print "Hit OSError: %s" % e
                except Exception, e:
                    print e
        for name in d:
            try:
                os.rmdir(os.path.join(r, name))
            except OSError, e:
                print "Hit OSError: %s" % e
            except Exception, e:
                print e

make_tree(get_input(MAKE_LOC))
del_files(get_input(TAKE_LOC))