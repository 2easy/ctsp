import helpers

def solve(dists):
    # generate all 3-cities tours
    tours = helpers.all_3tours(range(0,len(dists)),dists)
    # and sort them according to their length
    tours.sort()
    # choose best 3-tours
    res,visited = [],set([])
    for t in tours:
        if set(t.cities_list())&visited == set([]):
            for c in t.cities_list():
                visited.add(c)
            res.append(t.cities_list())
    # and append the cities that hadn't been choosen
    if len(dists) % 3 != 0:
        all_cities = set(range(0, NCITIES))
        not_visited = list(all_cities - visited)
        res.append(not_visited)
    return res
