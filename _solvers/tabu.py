from solver import KCenterSolver
import random


class TabuSolver(KCenterSolver):
    def __init__(self, graph):
        super().__init__(graph)


    def __initalize(self, k):
        idx = random.sample(range(self.graph.cardV), k)
        self.current_solution = self.graph.cardV * [False]
        for i in idx:
            self.current_solution[i] = True

    


    def get_neighbours(self):
        neighbours = set()

        transformed_solution = self.transform_solution(self.current_solution)
        for point in transformed_solution:
            closest_negihbour = -1
            closest_distance = float('inf')
            for neigh in self.graph.get_neighbours(point):
                if neigh[0] < closest_distance:
                    closest_distance, closest_negihbour = neigh

            neighbours.add(closest_negihbour)
        print(neighbours)
        return neighbours

    @staticmethod  
    def get_allowed(A:set, B:set):
        allowed = set()
        for a in A:
            if a not in B:
                allowed.add(a)
        return random.sample(allowed, 1)

    def solve(self, k):
        self.__initalize(k)
        self.best_value = self.evaluate(self.current_solution)    
        T = set()
        while True:
            ind_to_change = TabuSolver.get_allowed(self.get_neighbours(), T)

            print(new_solution)
            break