import os
from Terminal.constants import ATTR as ATTRIBUTE
from Terminal.constants import *
from importlib import import_module

ATTR = 1
PATH = 'Programs'


def do_remove(self, args) -> 'Currently WIP and does not work':
    if args:
        try:
            f = import_module(PROGRAM_PATH + args)
            attr = getattr(f, ATTRIBUTE)
            if attr != 1:
                name = f.__name__
                name = name[9:]
                name = name + ".py"
                print("Programs/" + name)
                os.removedirs(name)
                self.write("Removed: " + args)
                return
            else:
                self.write("Cannot remove " + ATTRTYPE[attr].lower() + " program: " + args)
                return
        except ImportError:
            self.write("Program not found.")
            return
    else:
        return
