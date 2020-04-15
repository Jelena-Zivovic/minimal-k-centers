from solver import KCenterSolver
from itertools import combinations
import math


class BruteForceSolver(KCenterSolver):
    def __init__(self, graph):
        super().__init__(graph)
        self.best_value = math.inf
    
    def __repr__(self):
        return "BruteForce: "

    def evaluate_brut(self, solution):
        min_dist = self.graph.cardV * [math.inf]
        for node in solution:
            min_dist[node] = 0
            for w, neigh in self.graph.get_neighbours(node):
                if min_dist[neigh] > w:
                    min_dist[neigh] = w

        return sum(min_dist)

    def solve(self, k):
        solutions = list(combinations(self.graph.vertices, k))
        values = map(self.evaluate_brut, solutions)
        best = sorted(list(values))[0]
        print(self, end=" ")

        print(best)
            
