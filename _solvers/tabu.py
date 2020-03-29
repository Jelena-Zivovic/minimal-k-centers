from solver import KCenterSolver
import random


class TabuSolver(KCenterSolver):
    def __init__(self, graph, iters):
        super().__init__(graph)
        self.__iters = iters

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
        print(transformed_solution, neighbours)
        return zip(transformed_solution, neighbours)

    @staticmethod
    def get_allowed(A: set, B: set):
        allowed = set()
        for a in A:
            if a[1] not in B:
                allowed.add(a)
                
        return random.sample(allowed, len(allowed))

    def solve(self, k):
        self.__initalize(k)
        self.best_value = self.evaluate(self.current_solution)
        self.current_value = self.best_value
        self.best_solution = self.current_solution[:]
        T = set()
        i = 0
        occured = 0
        while i < self.__iters:
            indexes = TabuSolver.get_allowed(self.get_neighbours(), T)
            for (old_part, new_part) in indexes:
                if new_part not in self.current_solution:
                    break
            tmp_solution = self.current_solution[:]
            tmp_solution[old_part] = False
            tmp_solution[new_part] = True
            tmp_value = self.evaluate(tmp_solution)
            if  tmp_value < self.current_value:
                self.current_solution = tmp_solution

            if tmp_value < self.best_value:
                self.best_value = tmp_value
            i += 1
            

        print('------------TABU-------------')
        print(self.best_value)