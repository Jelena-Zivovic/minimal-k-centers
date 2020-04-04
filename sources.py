import numpy as np
from queue import PriorityQueue
from itertools import combinations
from math import sqrt


def transform(pts):
    pt1 = pts[0]
    pt2 = pts[1]
    return sqrt((pt1[0] + pt2[0])**2 + (pt1[1] + pt2[1])**2)


def getWeights(n):
    #generate n random point in 2d plane
    points = [(np.random.uniform(0, 3000), np.random.uniform(0, 3000)) for _ in range(n)]
    pairs_of_citis = list(combinations(points, 2))
    distances = list(map(transform, pairs_of_citis))
    return distances

def generateData(n):
    weights = getWeights(n)
    adjacency_list = {k : [] for k in range(0, n)}
    t = 0
    for i in range(0,n):
        for j in range(i+1, n):
            adjacency_list[i].append((weights[t], j))
            adjacency_list[j].append((weights[t], i))
            t += 1
    
    weights.sort()
    for (k, v) in adjacency_list.items():
        v.sort()
    
    return (weights, adjacency_list)
