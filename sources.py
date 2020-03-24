import numpy as np
from queue import PriorityQueue


def generateData(n):
    weights = []
    adjacency_list = {k : [] for k in range(0, n)}
    for i in range(0,n):
        for j in range(i, n):
            weight = np.random.randint(1, 300)
            weights.append(weight)
            adjacency_list[i].append((weight, j))
            adjacency_list[j].append((weight, i))

    weights.sort()
    for (k, v) in adjacency_list.items():
        v.sort()

    return (weights, adjacency_list)
