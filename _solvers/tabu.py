from solver import KCenterSolver
import random


class TabuSolver(KCenterSolver):
    def __init__(self, graph, iters, type_of_choice):
        super().__init__(graph)
        self.__iters = iters
        self.type_of_choice = type_of_choice

    def __repr__(self):
        return f"Tabu; Iterations {self.__iters} {self.type_of_choice}"

    def __initalize(self, k):
        idx = random.sample(range(self.graph.cardV), k)
        self.current_solution = self.graph.cardV * [False]
        for i in idx:
            self.current_solution[i] = True

    def get_neighbours(self):
        neighbours = list()

        transformed_solution = self.transform_solution(self.current_solution)
        for point in transformed_solution:
            closest_negihbour = -1
            closest_distance = float('inf')
            for neigh in self.graph.get_neighbours(point):
                if neigh[0] < closest_distance:
                    closest_distance, closest_negihbour = neigh

            neighbours.append(closest_negihbour)
        # print(transformed_solution, neighbours)
        return zip(transformed_solution, neighbours)


    def invert(self, idx1, idx2):
        tmp = self.current_solution[idx1]
        self.current_solution[idx1] = self.current_solution[idx2]
        self.current_solution[idx2] = tmp

    @staticmethod
    def get_allowed(A: list, B: list, current_solution):
        
        allowed = list()
        for a in A:
            current_solution.invert(a[0], a[1])
            if current_solution not in B:
                allowed.append(a)            
            current_solution.invert(a[1], a[0])
        if current_solution.type_of_choice == 1:
            return sorted(allowed, key= lambda t: current_solution.evaluate(t))
        else:
            return random.sample(allowed, len(allowed))

    def solve(self, k):
        self.__initalize(k)
        self.best_value = self.evaluate(self.current_solution)
        self.current_value = self.best_value
        self.best_solution = self.current_solution[:]
        T = list()
        i = 0
        occured = 0
        while i < self.__iters:

            indexes = TabuSolver.get_allowed(list(self.get_neighbours()), T, self)
            for (old_part, new_part) in indexes:
                if new_part not in self.current_solution:
                    break
            tmp_solution = self.current_solution[:]
            tmp_solution[old_part] = False
            tmp_solution[new_part] = True
            tmp_value = self.evaluate(tmp_solution)
            if  tmp_value < self.current_value:
                self.current_solution = tmp_solution[:]
            else:
                T.append(self.transform_solution(tmp_solution[:]))        
            if tmp_value < self.best_value:
                self.best_value = tmp_value
            i += 1
            

        print(self)
        print(self.best_value)
