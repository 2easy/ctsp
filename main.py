#!/usr/bin/env python
from greedy import Greedy
from stabu_search import SimpleTabooSearch
import simulated_annealing

# Generate simple example
from helpers import gen_dists, compute_cost
dists1 = gen_dists([(0,0), (-4,0), (1,4), (3,4), (3,2), (8,-6), (-2,-3), (-4,-3)])
#print(dists1)

greedy = Greedy(dists1)
g_sol = greedy.solve()
print("GREEDY SOLUTION:\t\t\t"+str(g_sol)+" ---> " + str(greedy.cost))
sts = SimpleTabooSearch(dists1)
sts_sol = sts.solve()
print("SIMPLE TABOO SEARCH SOLUTION:\t\t"+ str(sts_sol)+ " ---> "+ str(sts.cost))

sts1 = SimpleTabooSearch(dists1)
while sts1.step(): pass
sts1_sol = sts1.solution
print("SIMPLE TABOO SEARCH STEPbySTEP SOLUTION:\t\t"+ str(sts1_sol)+ " ---> "+ str(sts1.cost))

#sa_sol = simulated_annealing.solve(dists1)
#print("SIMULATED ANNEALING SOLUTION:\t\t"+ str(sa_sol)+ " ---> "+ str(compute_cost(sa_sol, dists1)))

