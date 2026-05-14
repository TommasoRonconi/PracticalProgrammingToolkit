# A first section in which you import stuff
from random import random as frand
import math
import sys

# A second section in which you define functions

def foo () :
    pass

def bar (arg1, kwarg1 = 42) :
    pass

# .. or classes

class baz () :

    def __init__ (self) :
        pass

    def do_something (self) :
        pass

# A last part in which you wrap everything togheter and make it work:
if __name__ == '__main__' :

    # here instructions that build the script
    n_samples = int(input('How many samples?'))
    print( f'running with {n_samples:d} samples' )
