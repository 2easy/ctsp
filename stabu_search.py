#!/usr/bin/env python
import greedy
from helpers import compute_cost, neighbourhood_mix2t


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
