#!/usr/bin/env python
import greedy
import stabu_search
import simulated_annealing

# Generate simple example
from helpers import gen_dists, compute_cost
dists1 = gen_dists([(0,0), (-4,0), (1,4), (3,4), (3,2), (8,-6), (-2,-3), (-4,-3)])
#print(dists1)


g_sol = greedy.solve(dists1)
print("GREEDY SOLUTION:\t\t\t"+str(g_sol)+" ---> " + str(compute_cost(g_sol, dists1)))
sts_sol = stabu_search.solve(dists1)
print("SIMPLE TABOO SEARCH SOLUTION:\t\t"+ str(sts_sol)+ " ---> "+ str(compute_cost(sts_sol, dists1)))
sa_sol = simulated_annealing.solve(dists1)
print("SIMULATED ANNEALING SOLUTION:\t\t"+ str(sa_sol)+ " ---> "+ str(compute_cost(sa_sol, dists1)))

