"""
utils.py
"""

from objects import *

def fswitch(f, g, n):
    letter = 'g'
    if f != None:
        f.close()
    if g == gt.DIHEDRAL:
        letter = 'd'
    return open("log/{}{}.log".format(letter, n), "w+")

def gen_paths(graph):
    return permutations(graph.vertices)

def gen_multisets(graph):
    return all_msets(graph.ugroup.bset,\
                        r=(graph.ugroup.order - 1))

def path_to_set(path, graph):
    mset = []
    for i in xrange(0, len(path) - 1):
        mset.append(graph.edges[path[i]][path[i + 1]])
    return multiset(mset)

def record_sets(plist, graph, ofile=None):
    multisets = set([])
    for p in plist:
        mset = path_to_set(p, graph)
        multisets.add(mset)
        # if ofile: ofile.write('- {}\n'.format(mset.visual()))
    return multisets

def find_fails(wset, allsets, verbose=False, ofile=None):
    total_msets = 0
    fails = set([])
    for tup in allsets:
        total_msets += 1
        mtup = multiset(tup)
        if mtup not in wset:
            fails.add(mtup)
            if ofile: ofile.write('- {}\n'.format(mtup.visual()))
    return fails
            
    
def calculate(n, generator, verbose=False, silent=False, ofile=None):
    
    if verbose: printf("Generating group for n = {}... ".format(n))
    G = BHRGroup(n, ggen=generator)
    if verbose: printf("done.\nGenerating graph for n = {}... "\
                       .format(n))
    V = BHRGraph(G)
    if verbose: printf("done.\n")
    if not silent and not verbose:
        printf("Generating paths and multisets... ")
    if verbose: printf("Generating paths... ")
    paths = gen_paths(V)
    if verbose: printf("done.\nGenerating all possible multisets... ")
    all_multisets = gen_multisets(V)
    if verbose: printf("done.\nCalculating working multisets... ")
    working_multisets = record_sets(paths, V, None)
    if not silent: printf("done.\nCalculating failing multisets... ")
    fail_set = \
    find_fails(working_multisets, all_multisets, verbose, ofile)
    if not silent: printf("done.\n")
    if not silent: printf("Found {} failing multisets.\n"\
                          .format(len(fail_set)))
    # THIS NUMBER NOT ACCURATE -- what's wrong with the generator?
    # if not silent: printf("Found {} successful multisets.\n"\
    #                      .format(len(working_multisets)))
    return fail_set


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
        if i == 2: arglist[0],arglist[1] = int(args[1]),int(args[1]) + 1
    else:
        arglist[0],arglist[1] = int(args[1]),int(args[2])
        i += 1
    if len(args) > i:
        tflag = False
        for j in xrange(i, len(args)):
            if tflag:
                try: arglist[2] = GROUP_TYPES[args[j].lower()]
                except: app_error(\
                "Invalid group type {}.".format(args[j]))
                tflag = False
            elif args[j] in ['-t', '--type']: tflag = True
            elif args[j] in ['-v', '--verbose']: arglist[4][0] = True
            elif args[j] in ['-s', '--silent']: arglist[4][1] = True
            else: arglist[4].append(args[j])
    return arglist
    
    
