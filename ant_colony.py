#!/usr/bin/env python

from greedy import Greedy 
from helpers import compute_cost, neighbourhood_mix2t, concat_0, weighted_choice, split_by_value
from random import choice, random
from math import exp

ITER = 100
C = 1/1024
# decay coefficient =  C * exp (1 -(random path)/(current opt))



class AntColony:
  
  
    def __init__(self, dists, init_solution):
        
        self.dists = dists[:]
        self.best = self.current = self.last = init_solution
        self.cost = compute_cost(self.best, self.dists)
        self.cities = len(dists)
        
        #initial pheromone amount
        #for i in range (0, self.cities):
        #    for j in range (0, self.cities):
        #        if i != j:
        #          self.p[i][j] = 1/dists[i][j]
        self.update_pheromone(reduce(concat_0, init_solution, []) + [0])
        
        
    def pick_random_neighbour(self, curr, visited):
        possible = list((set(range(0,self.cities)) - set(visited)) - set([curr]))
        choices = []
        for i in range (0, len(possible)):
            choices.append( (possible[i],self.dists[curr][possible[i]]) )
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
        1
        #print("here i should update pheromone\n")
        #     update pheromone values taking into account solution and its weight 
        #     (decrease pheromone values on every edge - add pheromone on random chosen path)
    def solve(self):
        for i in range (0, ITER):
            path = self.random_path(0,0, [-1])
            self.update_pheromone(path)
            self.current = self.best = split_by_value(path,0)
            #TODO use real best as answer
            self.cost = compute_cost(self.current, self.dists)
        return self.best