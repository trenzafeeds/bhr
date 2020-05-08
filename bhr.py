"""
bhr.py
"""

from lib.objects import *
from lib.utils import *

DEFAULT_ARGS = [3, 6, gt.DIHEDRAL, []]
GROUP_TYPES = {'d': gt.DIHEDRAL,
               'dihedral': gt.DIHEDRAL}

# Setup returns command line args
# as a list. Must then be unpacked to
# be passed as variables.
def setup(args):
    global DEFAULT_ARGS
    global GROUP_TYPES
    arglist = deepcopy(DEFAULT_ARGS)
    bflag = False
    for i in [1, 2]:
        try: int(args[i])
        except:
            bflag = True
            break
    if bflag:
        if i == 2: arglist[1] = int(args[1])
    else:
        arglist[0] = int(args[1])
        arglist[1] = int(args[2])
        i += 1
    if len(args) > i:
        tflag = False
        for j in xrange(i, len(args)):
            if tflag:
                try: arglist[2] = GROUP_TYPES[args[j].lower()]
                except: app_error(\
                "Invalid group type {}.".format(args[j]))
                tflag = False
            elif args[j] in ['-t', '--type']:
                tflag = True
            else:
                arglist[3].append(args[j])
    return arglist
        

def main(lower, upper, gtype=gt.DIHEDRAL, options=[]):
    return 0

if __name__== '__main__':
    sys.exit(main(*setup(sys.argv)))
