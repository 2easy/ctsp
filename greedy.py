import helpers

def solve(dists):
    # generate all 3-cities tours
    NCITIES = len(dists) - 1 # do NOT count the base
    tours = helpers.all_3tours(range(1,len(dists)), dists)
    # and sort them according to their length
    tours.sort()
    # choose best 3-tours
    res,visited = [],set([])
    for t in tours:
        if set(t.cities_tuple())&visited == set([]):
            for c in t.cities_tuple():
                visited.add(c)
            res.append(t.cities_tuple())
    # and then append the cities that hadn't been choosen
    if len(dists) % 3 != 0:
        all_cities = set(range(1, NCITIES)) # do NOT include base
        not_visited = tuple(all_cities - visited)
        res.append(not_visited)
    return res
