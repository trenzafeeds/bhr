"""
header.py
"""
import sys
from enum import Enum
from copy import deepcopy

import sage.all
from sage.groups.perm_gps.permgroup_named import *

class gt(Enum):
    DIHEDRAL = DihedralGroup

def app_error(message, code=1):
    print "Error:", message
    sys.exit(code)

