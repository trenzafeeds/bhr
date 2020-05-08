"""
objects.py
"""

from header import *

class BHRGroup:

    def __init__(self, n, ggen=gt.DIHEDRAL):
        if ggen == gt.DIHEDRAL:
            self.group = ggen(n)
        else: app_error("Invalid group type.")

        self.order = self.group.order()
        self.elements = self.group.list()
        self.i = self.group.identity()
        
        self.bgroup = self.gen_bar_group()

    def gen_bar_group(self):
        bar_group = {}
        for item in self.group.list():
            if item != self.group.identity():
                bar_group[item] = frozenset([item, item.inverse()])
        return bar_group

class BHRGraph:
    
    def __init__(self, ugroup):
        self.ugroup = ugroup
        self.vertices = ugroup.elements
        self.edge_counts = self.gen_count_dict()
        self.edge_locs = self.gen_loc_dict()
        self.edges = self.gen_edges()

    def edge(self, base):
        return self.ugroup.bgroup[base]

    def gen_count_dict(self):
        count_dict = {}
        # NOTE: Dict uses g as key corresponding to the edge bgroup[g]
        for element in self.ugroup.bgroup.values():
            count_dict[element] = 0
        return count_dict

    def gen_loc_dict(self):
        loc_dict = {}
        # NOTE: Uses keys as count dict
        for element in self.ugroup.bgroup.values():
            loc_dict[element] = set()
        return loc_dict

    def record_edge(self, start, fin, edge_obj):
        if frozenset([start, fin]) not in self.edge_locs[edge_obj]:
            self.edge_counts[edge_obj] += 1
            self.edge_locs[edge_obj].add(frozenset([start, fin]))
            return True
        return False

    def gen_edges(self):
        edge_dict = {}
        for vertex in self.vertices:
            edge_dict[vertex] = {}
            for dest in self.vertices:
                vinverse = vertex.inverse()
                if (vinverse * dest) == self.ugroup.i:
                    edge_dict[vertex][dest] = None
                else:
                    edge_dict[vertex][dest] =\
                    self.ugroup.bgroup[vinverse * dest]
                    self.record_edge(\
                    vertex, dest, self.edge(vinverse * dest))
        return edge_dict
