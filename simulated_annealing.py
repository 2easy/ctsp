#!/usr/bin/env python

from greedy import Greedy 
from helpers import compute_cost, neighbourhood_mix_n_t
from random import choice, random, randint
from math import exp, log

# TODO choose start temp wiser, by experiment
TEMP_START = 100000
GFACTOR = 10.0
LFACTOR = 10.0

class SimulatedAnnealing:
    def __init__(self, dists, init_solution):
        self.dists = dists[:]
        self.best = self.current = self.last = init_solution
        self.cost = compute_cost(self.best, self.dists)

    def neighbourhood(self,solution):
        return neighbourhood_mix_n_t(solution, log(8 * len (solution)), self.dists)

    def update_temp(self,temp, i):
        # heat up from time to time, so that we can escape the local minima
        if i % 100 == 0 and random() > 0.5:
            # heat up by random amount between two arbitrarily numbers
            return temp + randint(17,163)
        # if the temp is low - decrease geometricaly else lineary
        elif i > 10000:
            return temp - LFACTOR
        else:
            new_temp = temp/GFACTOR
            if new_temp < 1:
                return 1
            else:
                return new_temp

    def solve(self):
        res_file = open('annealingresults', 'w')
        i = 0
        temp = TEMP_START
        # TODO update stop condition to separate function
        while i < 3000:
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
            res_file.write(str(self.cost)+"\n")
        res_file.close()
        return self.best
