"""
header.py
"""
import sys, time
from enum import Enum
from copy import deepcopy
from itertools import permutations
from itertools import combinations_with_replacement as all_msets
from collections import Counter
from pprint import PrettyPrinter

import sage.all
from sage.groups.perm_gps.permgroup_named import *

VERBOSE = False
SILENT = False

class gt(Enum):
    DIHEDRAL = DihedralGroup
#                                             verbose, silent
DEFAULT_ARGS = [3, 6, gt.DIHEDRAL, 'out.log', [False, False]]
GROUP_TYPES = {'d': gt.DIHEDRAL,
               'dihedral': gt.DIHEDRAL}

def app_error(message, code=1):
    print "Error:", message
    sys.exit(code)

def printf(message):
    sys.stdout.write(message)
    sys.stdout.flush()
    return 0

def timer(start=None):
    if start == None: return time.clock()
    else: return time.clock() - start
