#!/usr/bin/env python
from greedy import Greedy
from helpers import compute_cost, neighbourhood_mix2t

class SimpleTabooSearch:
    def __init__(self, dists):
        self.dists = dists[:]
        self.i = 0
        self.taboo = []
        self.current = Greedy(dists).solve()
        self.best = self.current[:]
        self.cost = compute_cost(self.best, self.dists)
        self.solution = self.best

    def neighbourhood(self, solution):
        return neighbourhood_mix2t(solution)

    def exclude(self, solutions, taboo):
        res = []
        for s in solutions:
            if all([ set(s) != f for f in taboo]):
                res.append(s)
        return res

    def best_from(self, solutions, dists, taboo):
        best = solutions.pop()
        for s in solutions:
            if compute_cost(s,dists) < compute_cost(best,dists):
                best = s
        taboo.append(set(best))
        return best,taboo

    def step(self):
        if self.i < 1000:
            candidates = self.exclude(self.neighbourhood(self.current), self.taboo)
            if candidates:
                self.current,self.taboo = self.best_from(candidates, self.dists, self.taboo)
                self.i += 1
                # keep the best solution so far
                if compute_cost(self.current, self.dists) < compute_cost(self.best, self.dists):
                    self.best = self.current[:]
                    self.cost = compute_cost(self.best, self.dists)
                    self.solution = self.best
            # tell the caller step was evaluated
            else:
                return False
            return True
        else:
            # tell the caller we are already done
            self.solution = self.best
            self.cost = compute_cost(self.best, self.dists)
            return False

    def solve(self):
        # TODO generalize stop condition by funciton
        while self.i < 1000:
            candidates = self.exclude(self.neighbourhood(self.current), self.taboo)
            if candidates:
                self.current,self.taboo = self.best_from(candidates, self.dists, self.taboo)
                self.i += 1
            else:
                break
            # keep the best solution so far
            if compute_cost(self.current, self.dists) < compute_cost(self.best, self.dists):
                self.best = self.current[:]
                self.cost = compute_cost(self.best, self.dists)
                self.solution = self.best
        return self.best
