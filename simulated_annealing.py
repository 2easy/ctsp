#!/usr/bin/env python

import greedy
from helpers import compute_cost, neighbourhood_mix2t
from random import choice, random
from math import exp

# TODO choose start temp wiser, by experiment
TEMP_START = 1000

def neighbourhood(solution):
    return neighbourhood_mix2t(solution)

def update_temp(temp, i):
    return temp - i

def solve(dists):
    best = greedy.solve(dists)
    current,last = best, best
    i = 0
    temp = TEMP_START
    # TODO update stop condition to separate function
    while i < 1000:
        current = choice(neighbourhood(current))
        dcost = float(compute_cost(current, dists) - compute_cost(last, dists))
        # TODO keep best solution so far
        if dcost < 0:
            last = current
        else:
            if random() >= exp(-(dcost/temp)): # SA secret formula
                last = current
        temp = update_temp(temp, i)
        i += 1
    # TODO return best solution
    return last
