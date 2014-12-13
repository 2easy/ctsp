#!/usr/bin/env python
from greedy import Greedy
from stabu_search import SimpleTabooSearch
import simulated_annealing

# Generate simple example
from helpers import gen_dists, compute_cost
dists1 = gen_dists([(0,0), (-4,0), (1,4), (3,4), (3,2), (8,-6), (-2,-3), (-4,-3)])
#print(dists1)

# example usage of greedy algorithm sovle
greedy = Greedy(dists1)
g_sol = greedy.solve()
print("GREEDY SOLUTION:\t\t\t"+str(g_sol)+" ---> " + str(greedy.cost))

# example usage of SimpleTabooSearch find solution at once
sts = SimpleTabooSearch(dists1)
sts_sol = sts.solve()
print("SIMPLE TABOO SEARCH SOLUTION:\t\t"+ str(sts_sol)+ " ---> "+ str(sts.cost))

# example usage of SimpleTabooSearch step by step with access to intermediate values
#sts1 = SimpleTabooSearch(dists1)
#while sts1.step():
#    #print(str(sts1.i)+" step --best-->\t"+str(sts1.best))
#    print(str(sts1.i)+" step --current-->\t"+str(sts1.current))
#sts1_sol = sts1.solution
#print("SIMPLE TABOO SEARCH STEPbySTEP SOLUTION:\t\t"+ str(sts1_sol)+ " ---> "+ str(sts1.cost))

# example usage of Simulated Annealing find solution at once
#sa_sol = simulated_annealing.solve(dists1)
#print("SIMULATED ANNEALING SOLUTION:\t\t"+ str(sa_sol)+ " ---> "+ str(compute_cost(sa_sol, dists1)))
