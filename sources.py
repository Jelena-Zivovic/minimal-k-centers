import numpy as np
from queue import PriorityQueue
from itertools import combinations
from math import sqrt
import multiprocessing


def genRandom(x):
    return np.random.uniform(100, 200)


def getWeights(n):
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    #generate n random point in 2d plane
    return pool.map(genRandom, range(n * (n-1) // 2))

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
