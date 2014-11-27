#!/usr/bin/env python
import greedy
import stabu_search
dists = [ [ 10,  0, 10, 20, 3, 4, 5 ],
          [ 11,  10, 0, 2, 3, 4, 5 ],
          [ 12,  20, 2, 0, 3, 4, 5 ],
          [ 13,  3, 3, 3, 0, 4, 5 ],
          [ 14,  4, 4, 4, 4, 0, 5 ],
          [ 9,   5, 5, 5, 5, 5, 0 ],
        ]

#print(str(greedy.solve(dists)))

print(str(stabu_search.solve(dists)))
