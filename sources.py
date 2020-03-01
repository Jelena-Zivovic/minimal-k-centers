import numpy as np
from queue import PriorityQueue


def generateData(n):
    weights = []
    adjacency_list = {k : [] for k in range(1, n+1)}
    for i in range(1,n+1):
        for j in range(i+1, n+1):
            weight = np.random.randint(1, 300)
            weights.append(weight)
            adjacency_list[i].append((weight, j))
            adjacency_list[j].append((weight, i))

    weights.sort()
    for (k, v) in adjacency_list.items():
        v.sort()

    return (weights, adjacency_list)