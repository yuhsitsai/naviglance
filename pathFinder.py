from graphObjects import *

def findPathMap (building: buildingObj, start: roomObj, end: roomObj) :
    """
    Performs A* search on building starting at start. Completes when end is found or entire graph searched.

    Inputs:
        - building: a buildingObj (undirected graph) representing a building with rooms & walkways
        - start: a roomObj representing the starting room/location in building
        - end: a roomObj representing the ending room/location in building
    
    Returns: exact path in dictionary form where visited nodes map to the parents they came from
        (e.g. end is a key but not a value, while start is a value and not a key)
        will have issues if we try and map from a node to itself but we're ignoring that
    """

    # create dicts for g_cost, h_cost, f_cost, parent w/ corresponding values for start_node
    g_cost = {start : 0}
    h_cost = {start : straightDistance(start, end)}
    f_cost = {start : (g_cost[start] + h_cost[start])}
    parent = {start : None}
    
    # create lists for openset and closedset, with start in openset
    openset = [start]
    closedset = []
    
    # while openset is not empty...
    while len(openset) > 0:
        # find and remove the node with the lowest f_cost from openset
        current = popLowestF(openset, f_cost)
        
        # if that node is the end_node, return findExactPath on the parent
        if current == end:
            return findExactPath(parent, start, end)
        
        # else, check each neighbor of current
        for nbr in current.getNeighbors():
            # calculate the g_cost of nbr on path using curr_node
            g_to_nbr = g_cost[current] + current.distanceToNeighbor(nbr)
            
            # if nbr is in openset, check if g_to_nbr is lower than 
            # g_cost[nbr]; if so, update cost & parent values accordingly
            if nbr in openset:
                if g_cost[nbr] > g_to_nbr:
                    g_cost[nbr] = g_to_nbr
                    f_cost[nbr] = g_cost[nbr] + h_cost[nbr]
                    parent[nbr] = current
                    
            # else, if nbr is not in closedset, calculate cost & parent
            # values for the nbr and append nbr to openset
            elif nbr not in closedset:
                g_cost[nbr] = g_to_nbr
                h_cost[nbr] = straightDistance(nbr, end)
                f_cost[nbr] = g_cost[nbr] + h_cost[nbr]
                parent[nbr] = current
                openset.append(nbr)
         
        # append current to closedset
        closedset.append(current)

    # this is the case if start and end are not connected
    # should not occur if buildings are hard coded correctly
    return parent

# given the list of all nodes visited and their parents, weeds out the exact path used with no excess key,value pairs
def findExactPath(possPaths, start, end) :
    route = {}
    curr = end
    while curr is not start:
        route[curr] = possPaths[curr]
        curr = possPaths[curr]
    return route

def popLowestF(openset : list[roomObj], f_cost : dict[roomObj, float]):
    """
    Finds, removes, and returns the node with the lowest f_cost from an openset list.
    
    Inputs:
        - openset: a list containing roomObj nodes from a buildingObj graph
        - f_cost: a dictionary where roomObj nodes in a buildingObj graph map to their f_cost 
        to an ending node
    
    Returns: the node with the lowest associated f_cost
    """
    # choose arbitrary node as lowest_f_node
    lowest_f_node = openset[0]
    
    # for each node in openset, if its f_cost is lower, replace
    # lowest_f_node with the new node
    for node in openset:
        if f_cost[node] < f_cost[lowest_f_node]:
            lowest_f_node = node
    
    # remove the lowest_f_node from openset
    openset.remove(lowest_f_node)
    
    # return lowest_f_node
    return lowest_f_node
