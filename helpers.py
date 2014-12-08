from itertools import permutations
from math import sqrt
# TODO rethink if it's better to change tour class to module method creating tuples

# One tour cycle object
class Tour:
    def __init__(self, city1,city2,city3, dists):
        # find best tour through this three cities
        self.tlen = float('+inf')
        for c1,c2,c3 in permutations([city1,city2,city3]):
            cur = compute_cost([(c1,c2,c3)], dists)
            if cur < self.tlen:
                self.tlen = cur
                self.c1,self.c2,self.c3 = c1,c2,c3

    def cities_tuple(self):
        return (self.c1, self.c2, self.c3)
    def __str__(self):
        return str(self.c1) + "->" + str(self.c2) + "->" + str(self.c3) + " = " + str(self.tlen)
    def __cmp__(self,other):
        return cmp(self.tlen, other.tlen)

def compute_cost(solution, dists):
    res = 0
    for t in solution:
        res += dists[0][t[0]] # base -> first city
        for c in range(len(t)-1):
            res += dists[t[c]][t[c+1]]
        res += dists[t[-1]][0] # last city -> base
    return res

def all_3tours(ct, dists):
    """generate all 3-lenght tours from ct = cities tuple"""
    tours = []
    NCITIES = len(ct)
    for i in range(0, NCITIES):
        for j in range(i+1, NCITIES):
            for k in range(j+1, NCITIES):
                tours.append(Tour(ct[i],ct[j],ct[k],dists))
    return tours

def gen_dists(points):
    res = []
    for p1 in points:
        sub_res = []
        x1,y1 = p1
        for p2 in points:
            x2,y2 = p2
            sub_res.append(round(sqrt(pow(x2-x1, 2)+pow(y2-y1, 2)), 2))
        res.append(sub_res)
    return res
