#!/usr/bin/env python

from greedy import Greedy 
from helpers import compute_cost, neighbourhood_mix2t, concat_0, weighted_choice, split_by_value
from random import choice, random
from math import exp
import copy

ITER = 3000
C = 1.0/512.0
PHEROMONE_STR = 1.0/2.0
# decay coefficient =  C * exp (1 -(random path)/(opt))

class AntColony:
  
    def __init__(self, dists, init_solution):
        
        self.dists = dists[:]
        self.p = copy.deepcopy(dists)
        self.best = self.current = self.last = init_solution
        self.cost = compute_cost(self.best, self.dists)
        self.cities = len(dists)
        
        #initial pheromone amount
        for i in range (0, self.cities):
            for j in range (0, self.cities):
                if i != j:
                  self.p[i][j] = C*exp(1 - self.dists[i][j]/self.cost)
        print(str(self.p))
        self.update_pheromone(reduce(concat_0, init_solution, []) + [0])
        print(str(self.p))
        
        
    def pick_random_neighbour(self, curr, visited):
        possible = list((set(range(0,self.cities)) - set(visited)) - set([curr]))
        choices = []
        for i in range (0, len(possible)):
            choices.append( (possible[i],self.p[curr][possible[i]]) )
        return weighted_choice(choices)
      
    def random_path(self, num, curr, visited):
        
        if len(visited) == self.cities:
          return [0]
        
        if num == 3:
            return self.random_path(0, 0, visited) + [0]
        else:
            random_n = self.pick_random_neighbour(curr, visited)
            if random_n != 0:
                return self.random_path(num+1, random_n, visited + [random_n]) + [random_n]
            else :
                return self.random_path(0, 0, visited) + [0]
        #     make random search - it's dfs-like thing, but we dont take first neighbour but random one 
        #     (also we need to remember we need visit starting point after visitig three nodes)
        
    def update_pheromone(self, path):
        psi = C * exp(1 - compute_cost(self.current, self.dists)/self.cost) 
        for i in range (0, self.cities):
            for j in range (0, self.cities):
                if i != j:
                  self.p[i][j] *= (1-psi)
                  
        for i in range(0, self.cities - 1):
            self.p[path[i]][path[i+1]] += PHEROMONE_STR * psi
        
    def solve(self):
        for i in range (0, ITER):
            if i % 1000 == 0:
              print("ITER " + str(i))
            path = self.random_path(0,0, [-1])
            
            self.current = split_by_value(path,0)
            if compute_cost(self.current, self.dists) < self.cost :
                self.best = self.current
                self.cost = compute_cost(self.current, self.dists)
            self.update_pheromone(path)
        return self.best