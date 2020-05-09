"""
bhr.py
"""

from lib.utils import *

def main(lower, upper, gtype=gt.DIHEDRAL, opath=None, options=[]):
    VERBOSE = options[0]
    SILENT = options[1]
    of = None

    if VERBOSE: printf("Running verbosely.\n")
    
    for num in xrange(lower, upper):
        of = fswitch(of, gtype, num)
        if VERBOSE: printf("Writing to file '{}'.\n".format(of.name))
        if not SILENT: printf("--- {} for n = {} ---\n"\
                              .format(gtype.__name__, num))
        of.write("---{} for n = {} ---\n"\
                 .format(gtype.__name__, num))
        calculate(num, gtype, VERBOSE, SILENT, of)

    of.close()

if __name__== '__main__':
    sys.exit(main(*setup(sys.argv)))
