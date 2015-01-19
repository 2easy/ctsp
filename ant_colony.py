#!/usr/bin/env python

from greedy import Greedy 
from helpers import compute_cost, neighbourhood_mix2t, concat_0
from random import choice, random
from math import exp

ITER = 100
C = 1/1024
# decay coefficient =  C * exp (1 -(random path)/(current opt))



class AntColony:
  
  
    def __init__(self, dists, init_solution):
        self.p = self.dists = dists[:]
        self.best = self.current = self.last = init_solution
        self.cost = compute_cost(self.best, self.dists)
        self.cities = len(dists)
        
        #initial pheromone amount
        for i in range (0, self.cities):
            for j in range (0, self.cities):
                if i != j:
                  self.p[i][j] = 1/dists[i][j]
        update_pheromone(reduce(concat_0, init_solution, [])).append(0))
        
        
    def pick_random_neighbour(self, visited):
        print("foo")
    
    
    def random_path(self, num, visited):
        if num == 3:
            return random_path(0, visited).append(0)
        else:
            random_n = pick_random_neighbour(self, visited)
            if random_n != 0:
                return random_path(0, visited.append(random_n)).append(random_n)
            else :
                return random_path()
        #     make random search - it's dfs-like thing, but we dont take first neighbour but random one 
        #     (also we need to remember we need visit starting point after visitig three nodes)
        
    def update_pheromone(self, path):
        print("foo")
        #     update pheromone values taking into account solution and its weight 
        #     (decrease pheromone values on every edge - add pheromone on random chosen path)
    def solve(self):
        for i in range (0, ITER):
            path = self.random_path(0, [])
            print("RANDOM PATH: " + str(path))
            self.update_pheromone(path)
            
        
        