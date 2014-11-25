#!/usr/bin/env python3

from itertools import permutations
# TODO rethink if it's better to change tour class to module method creating tuples
dists = [ [ 10,  0, 1, 2, 3, 4, 5 ],
          [ 11,  1, 0, 2, 3, 4, 5 ],
          [ 12,  2, 2, 0, 3, 4, 5 ],
          [ 13,  3, 3, 3, 0, 4, 5 ],
          [ 14,  4, 4, 4, 4, 0, 5 ],
          [ 9,   5, 5, 5, 5, 5, 0 ],
        ]
# One tour cycle object
class Tour:
    def __init__(self, city1,city2,city3):
        # find best tour through this three cities
        self.tlen = float('+inf')
        for c1,c2,c3 in permutations([city1,city2,city3]):
            cur = self.__compute_len__(c1,c2,c3)
            if cur < self.tlen:
                self.tlen = cur
                self.c1,self.c2,self.c3 = c1,c2,c3

    def cities_list(self):
        return [self.c1, self.c2, self.c3]
    def __compute_len__(self, c1,c2,c3):
        return dists[c1][0] + dists[c1][c2] + dists[c2][c3] + dists[c3][0]
    def __str__(self):
        return str(self.c1) + "->" + str(self.c2) + "->" + str(self.c3) + " = " + str(self.tlen)
    def __cmp__(self, other):
        return cmp(self.tlen, other.tlen)

# generate all 3-cities tours
tours = []
NCITIES = len(dists)
for i in range(0, NCITIES):
    for j in range(i+1, NCITIES):
        for k in range(j+1, NCITIES):
            tours.append(Tour(i,j,k))
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
# print the result
print(str(res))
