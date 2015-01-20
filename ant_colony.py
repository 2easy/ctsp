#!/usr/bin/env python

from greedy import Greedy 
from helpers import compute_cost, neighbourhood_mix2t, concat_0, weighted_choice, split_by_value
from random import choice, random, shuffle
from math import exp
import copy

ITER = 3000
C = 0.1
ANT_NUMBER = 8


class AntColony:
  
    def __init__(self, dists, init_solution):
        
        self.dists = dists[:]
        self.p = copy.deepcopy(dists)
        self.best = self.current = self.last = init_solution
        self.cost = compute_cost(init_solution, self.dists)
        self.cities = len(dists) 
        #initial pheromone amount
        
        for i in range (0, self.cities):
            for j in range (0, self.cities):
                if i != j:
                  self.p[i][j] =1.0 /self.cities
                  
        #print(str(self.p))
        self.update_pheromone(1.0/self.cities)
        #print(str(self.p))
        self.greedy = self.best
        self.best = self.current = self.last = [(0,0,0)]
        self.cost = 2000000000000000l
        
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
        
    def update_pheromone(self, factor):
        
        path = reduce(concat_0, self.best, []) + [0]
        #print(str(path))
        psi = C
        #as we need be in base every few cities, i should change pheromone management for from/to base edges
        base_trip_factor = 12 * path.count(0)
        
        for i in range (0, self.cities):
            for j in range (0, self.cities):
                if i != j:
                  self.p[i][j] *= (1-psi)
            
        for i in range(0, len(path) - 1):
            
            #as we should have one edge in, and one out, btu we have base_trip_number to/from base, we should scale a bit pheromone on those edges
            if path[i] == 0 or path[i+1] == 0:
                self.p[path[i]][path[i+1]] += (1.0 / base_trip_factor) * factor
            else : 
                
                self.p[path[i]][path[i+1]] += factor
                
                  
    
    def run_ants(self):
      b = [0]
      c = 200000000000000l
      for i in range (0, ANT_NUMBER):
          path = self.random_path(0,0, [-1])
          #print(str(split_by_value(path, 0)))
          cost = compute_cost(split_by_value(path, 0), self.dists)
          if cost < c :
              b = path
              c = cost
          #self.update_pheromone(1/c)
      return b
    
    def solve(self):
        for i in range (0, ITER):
            if i % 100 == 0:
              print("ITER " + str(i) + " solution " + str(self.cost))
              if compute_cost(self.greedy, self.dists) < self.best :
                  tmp = self.best
                  self.best = self.greedy
                  self.update_pheromone(1.0/compute_cost(self.greedy, self.dists))
                  self.best = tmp
              #print self.p
            path = self.run_ants()
            
            self.current = split_by_value(path,0)
            cost = compute_cost(self.current, self.dists) 
            if  cost < self.cost :
                self.best = self.current
                self.cost = cost
            self.update_pheromone(1/(self.cost))
        #print(str(self.p))
        return self.best