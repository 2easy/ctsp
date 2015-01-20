import helpers

class Greedy:
    def __init__(self, dists):
        self.dists = dists[:]
        self.ncities = len(self.dists) 
        self.solution = []
        self.cost = 0

    def solve(self):
        # generate all 3-cities tours
        tours = helpers.all_3tours(range(1,len(self.dists)), self.dists)
        # and sort them according to their length
        tours.sort()
        # choose best 3-tours
        visited = set([])
        for t in tours:
            if set(t[1:])&visited == set([]):
                for c in t[1:]:
                    visited.add(c)
                self.solution.append(t[1:])
        # and then append the cities that hadn't been choosen
        if len(self.dists) % 3 != 1:
            all_cities = set(range(1, self.ncities)) # do NOT include base
            not_visited = tuple(all_cities - visited)
            self.solution.append(not_visited)
        self.cost = helpers.compute_cost(self.solution, self.dists)
        return self.solution[:]
