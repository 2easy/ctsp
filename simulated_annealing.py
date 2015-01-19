#!/usr/bin/env python

from greedy import Greedy 
from helpers import compute_cost, neighbourhood_mix2t
from random import choice, random, randint
from math import exp

# TODO choose start temp wiser, by experiment
TEMP_START = 100000

class SimulatedAnnealing:
    def __init__(self, dists, init_solution):
        self.dists = dists[:]
        self.best = self.current = self.last = init_solution
        self.cost = compute_cost(self.best, self.dists)

    def neighbourhood(self,solution):
        return neighbourhood_mix2t(solution)

    def update_temp(self,temp, i):
        # heat up from time to time, so that we can escape the local minima
        if i % 100 == 0 and random() > 0.5:
            # heat up by random amount between two arbitrarily numbers
            return temp + randint(17,163)
        else:
            return temp - i

    def solve(self, it):
        i = 0
        temp = TEMP_START
        # TODO update stop condition to separate function
        while i < 1000:
            self.current = choice(self.neighbourhood(self.current))
            dcost = float(compute_cost(self.current, self.dists) - compute_cost(self.last, self.dists))

            if compute_cost(self.best, self.dists) > compute_cost(self.current, self.dists):
                self.best = self.current
                self.cost = compute_cost(self.best, self.dists)

            if dcost < 0:
                self.last = self.current
            else:
                if random() >= exp(-(dcost/temp)): # SA secret formula
                    self.last = self.current
                else:
                    self.current = self.last

            temp = self.update_temp(temp, i)
            i += 1
        if it == 0 :
            return self.best
        else:
            return self.solve(it-1)
