#!/usr/bin/env python

from greedy import Greedy 
from helpers import compute_cost, neighbourhood_mix2t
from random import choice, random
from math import exp

# TODO choose start temp wiser, by experiment
TEMP_START = 1000

class SimulatedAnnealing:
    def __init__(self, dists):
        self.dists = dists[:]
        self.best = self.current = self.last = Greedy(dists).solve()
        
    def neighbourhood(self,solution):
        return neighbourhood_mix2t(solution)

    def update_temp(self,temp, i):
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
