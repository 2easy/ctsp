#!/usr/bin/env python
from greedy import greedy_solution
dists = [ [ 10,  0, 1, 2, 3, 4, 5 ],
          [ 11,  1, 0, 2, 3, 4, 5 ],
          [ 12,  2, 2, 0, 3, 4, 5 ],
          [ 13,  3, 3, 3, 0, 4, 5 ],
          [ 14,  4, 4, 4, 4, 0, 5 ],
          [ 9,   5, 5, 5, 5, 5, 0 ],
        ]

print(str(greedy_solution(dists)))
