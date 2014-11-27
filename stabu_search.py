#!/usr/bin/env python
import greedy
from helpers import compute_cost
from random import shuffle

def mix(t1, t2):
    """ mixes two given cycles """
    new_pairs = []
    for i in range(len(t1)):
        for j in range(len(t2)):
            p1,p2 = t1[:],t2[:]
            p1[i],p2[j] = t2[j], t1[i]
            new_pairs.append([p1,p2])
    return new_pairs

def neighbourhood_mix2t(solution):
    """ computes neighbourhood of current solution
        by mixing cities in two randomly choosen tours"""
    shuffle(solution)
    t1,t2 = solution.pop(), solution.pop()

    res = []
    for tp in mix(t1, t2):
        tmp = solution[:]
        tmp.extend(tp)
        res.append(tmp)
    return res
def neighbourhood(solution):
    return neighbourhood_mix2t(solution)

def best_from(solutions, dists):
    best = solutions.pop()
    for s in solutions:
        if compute_cost(s,dists) < compute_cost(best,dists):
            best = s
    return best

def solve(dists):
    i = 0
    current = greedy.solve(dists)
    # TODO generalize stop condition by funciton
    while i < 1000:
        # TODO include taboo list
        print(str(current) + " --> " + str(compute_cost(current, dists)))
        current = best_from(neighbourhood(current), dists)
        i += 1
    return current
#for p in neighbourhood_mix2t([[0,1,2],[3,4,5],[6,7]]):
#    print(p)
