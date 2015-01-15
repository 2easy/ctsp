from itertools import permutations
from math import sqrt
from random import shuffle, randint

def tour(city1, city2, city3, dists):
    """ creates shortest tour tuple from given cities
        where tour tuple is (cost,city1,city2,city3) """

    # find best tour through this three cities
    tlen = float('+inf')
    for c1,c2,c3 in permutations([city1,city2,city3]):
        cur = compute_cost([(c1,c2,c3)], dists)
        if cur < tlen:
            tlen = cur
            cr1,cr2,cr3 = c1,c2,c3
    return (tlen, cr1, cr2, cr3)

def compute_cost(solution, dists):
    """ computes cost of given solution -> array of city tuples """
    res = 0
    for t in solution:
        res += dists[0][t[0]] # base -> first city
        for c in range(len(t)-1):
            res += dists[t[c]][t[c+1]]
        res += dists[t[-1]][0] # last city -> base
        
    return res

def all_3tours(ct, dists):
    """generates all 3-lenght tours from ct -> cities tuple"""
    tours = []
    NCITIES = len(ct)
    for i in range(0, NCITIES):
        for j in range(i+1, NCITIES):
            for k in range(j+1, NCITIES):
                tours.append(tour(ct[i],ct[j],ct[k],dists))
    return tours
# NEIGHBOURHOOD helper functions
def mix(t1, t2):
    """ mixes two given cycles """
    new_pairs = []
    for i in range(len(t1)):
        for j in range(len(t2)):
            p1,p2 = list(t1[:]),list(t2[:])
            p1[i],p2[j] = t2[j], t1[i]
            new_pairs.append([tuple(p1),tuple(p2)])
    return new_pairs

def neighbourhood_mix2t(solution):
    """ computes neighbourhood of current solution
        by mixing cities in two randomly choosen tours"""
    scopy = solution[:]
    shuffle(scopy)
    t1,t2 = scopy.pop(), scopy.pop()

    res = []
    for tp in mix(t1, t2):
        tmp = scopy[:]
        tmp.extend(tp)
        res.append(tmp)
    return res

def gen_dists(points):
    """ creates distance matrix from given list of point tuples """
    res = []
    for p1 in points:
        sub_res = []
        x1,y1 = p1
        for p2 in points:
            x2,y2 = p2
            sub_res.append(round(sqrt(pow(x2-x1, 2)+pow(y2-y1, 2)), 2))
        res.append(sub_res)
    return res

def gen_random(length):
    res = []
    while length > 0 :
        res.append((randint(-2048, 2047),randint(-2048, 2047)))
        length = length - 1
    return res
  