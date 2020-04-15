from abc import ABC, abstractmethod
from graph import Graph
import numpy as np


class KCenterSolver(ABC):
    def __init__(self, graph: Graph):
        self.graph = graph
        self.solution = self.graph.cardV * [False]

    def evaluate(self, individual):
        min_dist = self.graph.cardV * [float('inf')]
        for ind in range(len(individual)):
            if individual[ind]:
                min_dist[ind] = 0
                for (w, i) in self.graph.get_neighbours(ind):
                    if w < min_dist[i]:
                        min_dist[i] = w
        return sum(min_dist)

    def transform_solution(self, solution:list):
        transformed = []
        for i in range(len(solution)):
            if solution[i]:
                transformed.append(i)

        return transformed

    def __repr__(self):
        return "n: " + self.graph.cardV;

    @abstractmethod
    def solve(self, k):
        pass
