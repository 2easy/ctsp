#!/usr/bin/env python

from greedy import Greedy 
from helpers import compute_cost, neighbourhood_mix2t
from random import choice, random
from math import exp




class AntColony:
    def __init__(self, dists, init_solution):
        # TODO make some initial pheromone values out of initial solution and dists
        self.dists = dists[:]
        self.best = self.current = self.last = init_solution
        self.cost = compute_cost(self.best, self.dists)
        
        
    
    def solve(self):
        # TODO pretty much everything
        # in loop
        #     make random search - it's dfs-like thing, but we dont take first neighbour but random one 
        #     (also we need to remember we need visit starting point after visitig three nodes)
        #     update pheromone values taking into account solution and its weight 
        #     (decrease pheromone values on every edge - add pheromone on random chosen path)
        
        
        