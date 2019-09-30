import numpy as np

def bellman_ford_algorithm(table, source=0, commission=0):
    # The Bellman Ford Algorithm.
    
    n = len(table)

    table = -np.log((1/(1 + 0.01*commission))*table)

    # Initialize.
    distance = np.array([np.inf for m in range(n)])

    predecessor = np.array([source for m in range(n)])

    distance[source] = 0

    # Find shortest paths.
    for i in range(n-1):
        for u in range(n):
            for v in (x for x in range(n) if x != u):
                if distance[u] + table[v][u] < distance[v]:
                    distance[v] = distance[u] + table[v][u]
                    predecessor[v] = u

    # Determine if there is a negative-weight cycle.
    for u in range(n):
        for v in (x for x in range(n) if x != u):
            if distance[u] + table[v][u] < distance[v]:
                predecessor[v] = u
                return(True, distance, predecessor, v)
    return (False, distance, predecessor, np.nan)

def print_bellman_ford_output(is_cycle=False, distance=[], predecessor=[], v=np.nan):
    print()
    print("is negative weight cycle =", is_cycle)
    print("distance =", distance)
    print("prdecessor =", predecessor)
    print("trace back from element", v)
    print()

def find_cycle(table, source=0, commission=0):
    # Algorithm A.
    
    is_cycle, distance, predecessor, v = bellman_ford_algorithm(table, source,
                                                                commission)
    # Determine the negative-weight cycle.
    cycle = []
    if is_cycle:
        n = len(predecessor)
        sub_vc = v
        sub_cycle = []
        for i in range(n):
            if not np.isnan(sub_vc):
                if sub_vc not in sub_cycle:
                    sub_cycle.append(sub_vc)
                    sub_vc = predecessor[sub_vc]
                else:
                    start = sub_cycle.index(sub_vc)
                    cycle = sub_cycle[start:]
                    cycle.append(sub_vc)
                    break
    return cycle

def print_cycle(cycle=[]):
    # Print the negative-weight cycle.
    print()
    print("cycle", end=' = ')
    for c in cycle[:-1]:
        print(c, end="->")
    print(cycle[-1])
    print()
