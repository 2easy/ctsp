#!/usr/bin/env python
import greedy
from helpers import compute_cost
from random import shuffle

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
def neighbourhood(solution):
    return neighbourhood_mix2t(solution)

def exclude(solutions, taboo):
    res = []
    for s in solutions:
        if all([ set(s) != f for f in taboo]):
            res.append(s)
    return res

def best_from(solutions, dists, taboo):
    best = solutions.pop()
    for s in solutions:
        if compute_cost(s,dists) < compute_cost(best,dists):
            best = s
    taboo.append(set(best))
    return best,taboo

def solve(dists):
    i,taboo = 0,[]
    current = greedy.solve(dists)
    best = current[:]
    # TODO generalize stop condition by funciton
    while i < 1000:
        candidates = exclude(neighbourhood(current), taboo)
        if candidates:
            current,taboo = best_from(candidates, dists, taboo)
            i += 1
        else:
            break
        # keep the best solution so far
        if compute_cost(current, dists) < compute_cost(best, dists):
            best = current[:]
    return best
