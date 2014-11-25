#!/usr/bin/env python

from itertools import permutations
# TODO rethink if it's better to change tour class to module method creating tuples
# One tour cycle object
class Tour:
    def __init__(self, city1,city2,city3, dists):
        # find best tour through this three cities
        self.tlen = float('+inf')
        for c1,c2,c3 in permutations([city1,city2,city3]):
            cur = compute_len(c1,c2,c3, dists)
            if cur < self.tlen:
                self.tlen = cur
                self.c1,self.c2,self.c3 = c1,c2,c3

    def cities_list(self):
        return [self.c1, self.c2, self.c3]
    def __str__(self):
        return str(self.c1) + "->" + str(self.c2) + "->" + str(self.c3) + " = " + str(self.tlen)
    def __cmp__(self,other):
        return cmp(self.tlen, other.tlen)

def compute_len(c1,c2,c3, dists):
    return dists[c1][0] + dists[c1][c2] + dists[c2][c3] + dists[c3][0]
def greedy_solution(dists):
    # generate all 3-cities tours
    tours = []
    NCITIES = len(dists)
    for i in range(0, NCITIES):
        for j in range(i+1, NCITIES):
            for k in range(j+1, NCITIES):
                tours.append(Tour(i,j,k,dists))
    # and sort them according to their length
    tours.sort()
    # choose best 3-tours
    res = []
    visited = set([])
    for t in tours:
        if set(t.cities_list())&visited == set([]):
            for c in t.cities_list():
                visited.add(c)
            res.append(t.cities_list())
    # and append the cities that hadn't been choosen
    if NCITIES % 3 != 0:
        all_cities = set(range(0, NCITIES))
        not_visited = list(all_cities - visited)
        res.append(not_visited)
    return res
