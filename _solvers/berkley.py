from solver import KCenterSolver    
import math, random

class BerkleySolver(KCenterSolver):
    def __init__(self, graph, radius):
        super().__init__(graph)
        self.starting_radius = radius

    def __print_solution(self, W:set):
        min_dist = self.graph.cardV * [math.inf]
        for center in W:
            for w, neigh in self.graph.get_neighbours(center):
                if w < min_dist[neigh]:
                    min_dist[neigh] = w
        print('-----BerkleySolver---------')
        print(sum(min_dist))

    def solve(self, k):
        radius = self.starting_radius
        W = set()
        C = set(self.graph.vertices)
        while len(C) > 0:
            node = random.sample(C, 1)[0]
            W.add(node)
            C.remove(node)
            for weight, neigh in self.graph.get_neighbours(node):
                if weight < radius and neigh in C:
                    C.remove(neigh)
        if len(W) > k:
            self.starting_radius += 10
            self.solve(k)
        else:
            self.__print_solution(W) 